#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<iostream>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<list>
#include<algorithm>
#include<limits>
using namespace std;
const int N=10000,M=1000000007;
int a[5000],d[20];

inline int min(int a,int b){return a<b?a:b;}
inline int max(int a,int b){return a>b?a:b;}
int main(){
	int dummy,T,R,P,i,j,k,l,m,n,tmpn,c=0,s,t=0,maxc=0,maxr=0,x1,x2,y1,y2,b,start,end,p;
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	scanf("%d",&T);
	for(i=1;i<=T;i++){
		memset(a,0,sizeof(a));
		scanf("%d",&P);
		n=1<<P;
		c=0;
		for(j=0;j<n;j++){
			scanf("%d",&d[j]);
			c+=(d[j]=P-d[j]);
		}
		for(j=P-1;j>=0;j--)
			for(k=0;k<1<<j;k++)
				scanf("%d",&dummy);

		t=0;
		while(c>0){
			m=-1;
			for(j=0;j<n;j++)
				if(d[j]>m){
					m=d[j];
					p=j;
				}
			s=1;
			R=d[p];
			for(j=0,l=0;j<R&&l<P;){
				if(a[s]==1){
					;
				}else{
					a[s]=1;
					t++;
					j++;
					start=end=s;
					for(k=l;k<P;k++){
						start+=start;
						end+=end+1;
					}
					start-=1<<P;
					end-=1<<P;
					for(k=start;k<=end;k++){
						if(d[k]>0){
							d[k]--;
							c--;
						}
					}
				}
				if(p&(1<<P-l-1))
					s+=s+1;
				else
					s+=s;
				l++;
			}
		}	
		printf("Case #%d: %d\n",i,t);
	}
	return 0;
}

