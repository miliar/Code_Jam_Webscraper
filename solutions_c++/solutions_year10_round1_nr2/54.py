
#include <iostream>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

const int A=256;
const int inf=0x7f7f7f7f;

int main(){
	int nn;scanf("%d",&nn);
	for(int npr=1;npr<=nn;npr++){
		int D,I,M,n;scanf("%d%d%d%d",&D,&I,&M,&n);
		int v[n];
		for(int i=0;i<n;i++)scanf("%d",v+i);

		int now[A+1];memset(now,0x7f,sizeof(now));
		now[A]=0;
		for(int i=0;i<n;i++){

			//INSERT
			while(1){
				int cand[A+1];memcpy(cand,now,sizeof(cand));
				
				for(int i=0;i<A;i++){
					for(int t=0;t<=A;t++)if(t==A || abs(i-t)<=M){
						cand[i]=min(cand[i],now[t]+I);
					}
				}

				if(memcmp(cand,now,sizeof(cand))==0)break;
				memcpy(now,cand,sizeof(cand));
			}
			//for(int i=0;i<=A;i++)cout<<now[i]<<" ";cout<<endl;

			int next[A+1];memset(next,0x7f,sizeof(next));

			//DEL
			for(int k=0;k<=A;k++)if(now[k]!=inf){
				next[k]=min(next[k],now[k]+D);
			}

			//for(int i=0;i<=A;i++)cout<<now[i]<<" ";cout<<endl;

			//CHANGE
			for(int k=0;k<A;k++){
				for(int t=0;t<=A;t++)if(t==A || abs(k-t)<=M){
					next[k]=min(next[k],now[t]+abs(v[i]-k));
				}
			}
			memcpy(now,next,sizeof(next));

			//for(int i=0;i<=A;i++)cout<<now[i]<<" ";cout<<endl;
		}

		int ans=inf;
		for(int i=0;i<=A;i++)ans=min(ans,now[i]);

		printf("Case #%d: %d\n",npr,ans);
	}
	return 0;
}
