#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <map>

#define ONLINEJUDGE

using namespace std;

bool p[1<<10][1<<10];
map<int,char> C;
char str[1<<10];

int main(){

#ifdef ONLINEJUDGE
	freopen("dataB.in","r",stdin);
	freopen("dataB.txt","w",stdout);
#endif

	int T,N;
	scanf("%d",&T);
	
	for (int Test=1;Test<=T;Test++){
		memset(p,0,sizeof(p));
		C.clear();
		scanf("%d",&N);
		for (int i=0;i<N;i++){
			scanf("%s",str);
			C[(str[0]<<10)+str[1]] = str[2];
			C[(str[1]<<10)+str[0]] = str[2];
		}
		scanf("%d",&N);
		for (int i=0;i<N;i++){
			scanf("%s",str);
			p[str[0]][str[1]] = 1;
			p[str[1]][str[0]] = 1;
		}
		vector<char> elist;
		elist.clear();
		scanf("%d%s",&N,str);
		for (int i=0;i<N;i++){
			elist.push_back(str[i]);
			int len = elist.size();
			while ((len=elist.size())>1)
				if (C[(elist[len-2]<<10)+elist[len-1]]){
					elist[len-2] = C[(elist[len-2]<<10)+elist[len-1]];
					elist.erase(elist.end()-1);
				}
				else break;
			for (int i=0;i+1<elist.size();i++)
				if (p[elist[i]][*(elist.end()-1)]) {
					elist.clear();
					break;
				}
		}
		printf("Case #%d: [",Test);
		for (int i=0;i+1<elist.size();i++)
			printf("%c, ",elist[i]);
		if (elist.size()) putchar(*elist.rbegin());
        puts("]");
	}
		
	return 0;
}
