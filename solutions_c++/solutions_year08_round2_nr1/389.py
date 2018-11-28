#include <cstdio>
#include <algorithm>
#include <memory.h>
using namespace std;
long long p[111111][2];
long long cnt[5][5];
int forsort[2][5];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int tc=1; tc<=t; tc++){
		memset(p,0,sizeof(p));
		memset(cnt,0,sizeof(cnt));
		int n;
		long long A,B,C,D,X0,Y0,M;
		scanf("%d %lld %lld %lld %lld %lld %lld %lld\n",&n,&A,&B,&C,&D,&X0,&Y0,&M);
		p[1][0] = X0;
		p[1][1] = Y0;
		for(int i=2; i<=n; i++){
			X0 = (A*X0+B)%M;
			Y0 = (C*Y0+D)%M;
			p[i][0] = X0;
			p[i][1] = Y0;
		}
		for(int i=1; i<=n; i++){
			cnt[p[i][0]%3][p[i][1]%3]++;
		}
		long long ans=0;
		for(int l1=0; l1<=2; l1++){
			for(int l2=0; l2<=2; l2++){
				for(int l3=0; l3<=2; l3++){
					for(int l4=0; l4<=2; l4++){
						for(int l5=0; l5<=2; l5++){
							for(int l6=0; l6<=2; l6++){
								if((l1+l3+l5)%3==0 && (l2+l4+l6)%3==0){
									pair<int,int> t1,t2,t3;
									t1.first=l1;
									t1.second=l2;
									t2.first=l3;
									t2.second = l4;
									t3.first=l5;
									t3.second=l6;
									if(t1<=t2 && t2<=t3){
										if(t1!=t2 && t2!=t3 && t3!=t1){
											if(cnt[l1][l2]>0 && cnt[l3][l4]>0 && cnt[l5][l6]>0){
												ans += (cnt[l1][l2])*(cnt[l3][l4])*(cnt[l5][l6]);
											}
										}
										else if(t1==t2 && t2!=t3 && t3!=t1){
											if(cnt[l1][l2]>1 && cnt[l3][l4]>1 && cnt[l5][l6]>0){
												ans += (cnt[l1][l2])*(cnt[l3][l4]-1)*(cnt[l5][l6])/2;
											}
										}
										else if(t1!=t2 && t2==t3 && t3!=t1){
											if(cnt[l1][l2]>0 && cnt[l3][l4]>1 && cnt[l5][l6]>1){
												ans += (cnt[l1][l2])*(cnt[l3][l4])*(cnt[l5][l6]-1)/2;
											}
										}
										else if(t1==t2 && t2==t3 && t3==t1){
											if(cnt[l1][l2]>2 && cnt[l3][l4]>2 && cnt[l5][l6]>2){
												ans += (cnt[l1][l2])*(cnt[l3][l4]-1)*(cnt[l5][l6]-2)/6;
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
		printf("Case #%d: %lld\n",tc,ans);
	}

	return 0;
}