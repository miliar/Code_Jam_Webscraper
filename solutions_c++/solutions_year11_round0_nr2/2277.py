//BISMILLAHIRRAHMANIRRAHIM



#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cctype>
#include <climits>
#include <cmath>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define pii pair < int , int >
#define i64 long long

char cm[300][300];
bool op[300][300];

int main(int argc, char **argv)
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,I,q,c,r,i,j;
	char wd[500];
	cin>>T;
	for(I=1;I<=T;I++) {
		memset(cm,0,sizeof cm);
		memset(op,0,sizeof op);
		cin>>q;
		while(q--) {
			cin>>wd;
			cm[wd[0]][wd[1]]=cm[wd[1]][wd[0]]=wd[2];
		}
		cin>>q;
		while(q--) {
			cin>>wd;
			op[wd[0]][wd[1]]=1;
			op[wd[1]][wd[0]]=1;
		}
		vector < char > g;
		int n;
		cin>>n>>wd;
		bool f;
		for(i=0;i<n;i++) {
			if(g.size()) {
				if(cm[g.back()][wd[i]]) {
					g.back()=cm[g.back()][wd[i]];
				}
				else {
					f=1;
					for(j=0;j<g.size();j++) if(op[wd[i]][g[j]]) {
						g.clear();
						f=0;
						break;
					}
					if(f) g.push_back(wd[i]);
				}
			}
			else g.push_back(wd[i]);
		}
		printf("Case #%d: [",I);
		if(g.size()) {
			cout<<g[0];
			for(i=1;i<g.size();i++) cout<<", "<<g[i];
		}
		puts("]");
	}
	return 0;
}

