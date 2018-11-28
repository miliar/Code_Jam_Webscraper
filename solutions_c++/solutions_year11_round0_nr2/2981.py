#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

char combine[256][256];
char oppose[256];

int main () {
	fstream cin("B-small-attempt0.in");
	ofstream cout("output.txt");
	int T;
	cin>>T;
	for (int run=1;run<=T;++run) {
		memset (combine,0,sizeof(combine));
		memset (oppose,0,sizeof(oppose));
		int N,D,C;
		cin>>C;
		for (int i=0;i<C;++i) {
			string str;
			cin>>str;
			combine[str[1]][str[0]] = combine[str[0]][str[1]] = str[2];	
		}
		cin>>D;
		for (int i=0;i<D;++i) {
			string str;
			cin>>str;
			oppose[str[0]] = str[1];
			oppose[str[1]] = str[0];
		}
		vector<char> res;
		res.clear ();
		cin>>N;
		string str;
		cin>>str;
		res.push_back (str[0]);
		int M = 1;
		for (int i=1;i<N;++i) {
			res.push_back (str[i]);
			M++;
			
			while (M>1&& combine[res[M-1]][res[M-2]] > 0) {
				res[M-2]=combine[res[M-1]][res[M-2]];
				M--;
				res.pop_back ();
			}
			for (int j=0;j<M-1;++j)
				if (res[j]==oppose[res[M-1]]) {
					M=0;
					res.clear ();
					break;
				}
			//for (int i=0;i<M;++i) cout<<res[i]<<" ";cout<<endl;
		}
		cout<<"Case #"<<run<<": [";
		if (res.size()>0) {
			for (int i=0;i<res.size()-1;++i) 
				cout<<res[i]<<", ";
			cout<<res[res.size()-1];
		}
		cout<<"]"<<endl;
	}
	cin>>T;
	return 0;	
}
