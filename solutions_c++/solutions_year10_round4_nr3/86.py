
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cassert>
using namespace std;

int main(){
	int nn;scanf("%d",&nn);
	for(int npr=1;npr<=nn;npr++){
		int n;scanf("%d",&n);
		char buf[210][210];memset(buf,0,sizeof(buf));
		for(int i=0;i<n;i++){
			int x1,y1;scanf("%d%d",&x1,&y1);
			int x2,y2;scanf("%d%d",&x2,&y2);
			for(int i=x1;i<=x2;i++)for(int k=y1;k<=y2;k++)buf[i+1][k+1]=1;
		}
		int cnt=0;
		for(int i=0;i<210;i++)for(int k=0;k<210;k++)if(buf[i][k])cnt++;

		int ans=0;
		while(cnt){
			for(int i=210-1;i>=1;i--)for(int k=210-1;k>=1;k--){
				if(buf[i][k]==0 &&  (buf[i-1][k]&buf[i][k-1])){buf[i][k]=1;cnt++;}
				if(buf[i][k]==1 && !(buf[i-1][k]|buf[i][k-1])){buf[i][k]=0;cnt--;}
			}
			ans++;
		}

		printf("Case #%d: %d\n",npr,ans);
	}
	return 0;
}
