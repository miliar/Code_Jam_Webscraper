#include<iostream>
#include<cstring>
#include<string>
#include<math.h>
#include<vector>
#include<map>
#include<algorithm>
using namespace std;
long a,b,c,d,e,p;
long t1,t2,t3,t4;
long r,k,n;
long i,j;
long g[1024];
long f[1024][2];
int main(){
	freopen("C-small.in","r",stdin);freopen("C-small.out","w",stdout);
	//freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	int ncases=0;
	scanf("%d",&ncases);
	for(int cc=1;cc<=ncases;cc++){
		scanf("%ld %ld %ld",&r,&k,&n);
		for(i=0;i<n;i++){
			cin>>g[i];
		}
		for(i=0;i<n;i++){
			c=0;d=0;
			for(j=i;(c+g[j%n]<=k)&&(d<n);j=(j+1)%n){c+=g[j%n];d++;}
			f[i][0]=c;f[i][1]=d-1;
			//printf("i=%ld %ld %ld\n",i,c,f[i][1]);
		}
		e=0;p=0;
		for(i=0;i<r;i++){
			p+=f[e][0];
			e=(e+f[e][1]+1)%n;
		}
		printf("Case #%d: %ld\n",cc,p);
	}
}