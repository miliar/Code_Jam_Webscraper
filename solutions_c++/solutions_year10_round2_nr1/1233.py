#include<iostream>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<set>


using namespace std;

#define ps system("PAUSE")
typedef long long int  longlong;

set<string> dirs;



int main() { 
	int t,n,m,dc;
	string path,p2c;
	freopen("C:/TestData/A-large.in","r",stdin);freopen("C:/TestData/A-large.out","w",stdout);
	scanf("%d",&t);

	for(int ti=1;ti<=t;ti++) {

		dirs.clear();

		scanf("%d%d",&n,&m);

		for(int i=0;i<n;i++) {
			cin>>path;
			for(int j=1,s=path.size();j<s;j++) {
				if(path[j] == '/') {
					dirs.insert(path.substr(0,j));
				}

			}
			dirs.insert(path);
		}

		dc = 0 ;
		for(int i=0;i<m;i++) {
			cin>>path;
			for(int j=1,s=path.size();j<s;j++) {
				if(path[j] == '/') {
					p2c = path.substr(0,j);
					if( dirs.count(p2c) == 0 ) {
						dirs.insert(path.substr(0,j));
						dc++;
					}
				}
			}

			if( dirs.count(path) == 0 ) {
				dc++;
				dirs.insert(path);	
			}

		}
		printf("Case #%d: %d\n",ti,dc);
	}
	return 0;	
}