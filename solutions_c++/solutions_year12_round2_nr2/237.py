#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<windows.h>
#include<set>
using namespace std;

int t,H,n,m;
int c[110][110];
int f[110][110];
int tv[110][110];
int a[110][110];
int q[1200000],qb,qe;

int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};

int main(){
	int h,i,j,k,l;
	int x,y;
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%d%d%d",&H,&n,&m);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf("%d",&c[i][j]);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf("%d",&f[i][j]);
		a[0][0]=1;
		qb=0;qe=1;
		q[0]=0;
		while(qb!=qe){
			x=q[qb]/1000;y=q[qb]%1000;
			for(i=0;i<4;i++){
				if(x+dx[i]>=0 && x+dx[i]<n && y+dy[i]>=0 && y+dy[i]<m){
					if(a[x+dx[i]][y+dy[i]]==0 &&
						H+50<=c[x+dx[i]][y+dy[i]] && 
						f[x+dx[i]][y+dy[i]]+50<=c[x+dx[i]][y+dy[i]] &&
						f[x][y]+50<=c[x+dx[i]][y+dy[i]] &&
						f[x+dx[i]][y+dy[i]]+50<=c[x][y]){
							a[x+dx[i]][y+dy[i]]=1;
							q[qe++]=(x+dx[i])*1000+y+dy[i];
					}
				}
			}
			qb++;
		}
		qb=qe=0;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++){
				if(a[i][j]==1){
					q[qe++]=i*1000+j;
					tv[i][j]=0;
				}else{
					tv[i][j]=1e9;
				}
			}
		while(qb!=qe){
			x=q[qb]/1000;y=q[qb]%1000;
			for(i=0;i<4;i++){
				if(x+dx[i]>=0 && x+dx[i]<n && y+dy[i]>=0 && y+dy[i]<m){
					if(f[x+dx[i]][y+dy[i]]+50<=c[x+dx[i]][y+dy[i]] &&
						f[x][y]+50<=c[x+dx[i]][y+dy[i]] &&
						f[x+dx[i]][y+dy[i]]+50<=c[x][y]){
							if(c[x+dx[i]][y+dy[i]]-50<H-tv[x][y]){
								j=H-tv[x][y]-(c[x+dx[i]][y+dy[i]]-50);
							}else{
								j=0;
							}
							if(H-tv[x][y]-j-f[x][y]>=20){
								k=tv[x][y]+j+10;
							}else{
								k=tv[x][y]+j+100;
							}
							if(k<tv[x+dx[i]][y+dy[i]]){
								tv[x+dx[i]][y+dy[i]]=k;
								if(a[x+dx[i]][y+dy[i]]==0){
									a[x+dx[i]][y+dy[i]]=1;
									q[qe++]=(x+dx[i])*1000+y+dy[i];
								}
							}
					}
				}
			}
			a[x][y]=0;
			qb++;
		}
		printf("Case #%d: %.1lf\n",h,tv[n-1][m-1]/10.0);
	}
	//Sleep(1000);
	return 0;
}