#include <stdlib.h>
#include <iostream>
#include <vector>
#include <map>
#include <stdio.h>


using namespace std;


int score=0;

class Dir {
public:	
	map<string,Dir> subdirs;
	~Dir() {
		subdirs.clear();
	}
	
	
	void dump() {
		map<string,Dir>::iterator it;
		for ( it=subdirs.begin() ; it != subdirs.end(); it++ ) {
		    cout << (*it).first << endl;
		     (*it).second.dump();
		}
	}
	
	
	void addSubdir(string dname) {
		size_t p=dname.find("/", 1);
		
		string ldir (dname.substr(1,p-1));
		
//		cout << "processing: "<< dname << "  ldir='" << ldir << "'";
		
		if (subdirs.find(ldir)==subdirs.end()) {
			score++;
//			cout << " -> new!" << score;
			}
		
//		cout << "\n";
		
		subdirs[ldir];
		
		if (p!=-1)
			subdirs[ldir].addSubdir(dname.substr(p));
	}
};


Dir root;


int main ()
{
	int T, N, M;
	int tcase=0;
	int res;
	char buf[150];
	
//	root.addSubdir("/abc/a/b/c");
//	root.addSubdir("/abc/a/d/d");
	
//	printf("score:%d\n", score);
	
	scanf("%d", &T);
	
	while (T-->0) {
		root.subdirs.clear();
		
		scanf("%d%d", &N, &M);
		
		while (N-->0) {
			scanf("%s", buf);
			for (int i=0;i<120;i++) {
				if (buf[i]=='\n'||buf[i]=='\r') {buf[i]=0; break;}
			}
			string dname(buf);
			root.addSubdir(buf);
			
		}
		score=0;
//		cout << "dumping\n";
//		root.dump();
		
		while (M-->0) {
			scanf("%s", buf);
			for (int i=0;i<120;i++) {
				if (buf[i]=='\n'||buf[i]=='\r') {buf[i]=0; break;}
			}
			string dname(buf);
			root.addSubdir(buf);
			
		}
//		cout << "dumping2\n";
//		root.dump();
		printf("Case #%d: %d\n", ++tcase, score);
	}
	return 0; 
}
