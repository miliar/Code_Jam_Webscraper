#include <cstdio>
#include <map>
#include <set>
#include <string>

using namespace std;

char buf[256];

int main(){
	int tcN;
	scanf("%d", &tcN);
	for(int tc=0; tc<tcN; ++tc){
		string res;
		map<pair<char, char>, char> com;
		set<pair<char, char> > opo;
		map<pair<char, char>, char>::iterator iter;
		int c, d, n;
		scanf("%d", &c);
		for(int i=0; i<c; ++i){
			scanf("%s", buf);
			com[make_pair(buf[0], buf[1])] = buf[2];
			com[make_pair(buf[1], buf[0])] = buf[2];
		}
		scanf("%d", &d);
		for(int i=0; i<d; ++i){
			scanf("%s", buf);
			opo.insert(make_pair(buf[0], buf[1]));
			opo.insert(make_pair(buf[1], buf[0]));
		}
		scanf("%d", &n);
		scanf("%s", buf);
		for(char *p=buf; *p; ++p){
			if(res.size()){
				iter = com.find(make_pair(res[res.size()-1], *p));
				if(iter != com.end()){
					res.erase(res.size()-1, 1);
					res += iter->second;
					continue;
				}else{
					res += *p;
				}
			}else{
				res += *p;
			}
			for(int i=0; i<res.size()-1; ++i){
				if(opo.find(make_pair(res[i], *p)) != opo.end()){
					res = "";
					break;
				}
			}
		}
		printf("Case #%d: [", tc+1);
		if(res.size())
			printf("%c", res[0]);
		for(int i=1; i<res.size(); ++i)
			printf(", %c", res[i]);
		printf("]\n");
	}
}
