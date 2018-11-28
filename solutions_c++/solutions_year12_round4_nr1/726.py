#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<vector>
using namespace std;
char anstr[][4]={"NO","YES"};
int f[10240],d[10240],l[10240],n,D;
int solve(){
	memset(f,0,sizeof(f));
	scanf("%d",&n);
	for(int i=0;i<n;++i)scanf("%d%d",d+i,l+i);
	scanf("%d",&D);
	f[0]=d[0];
	if(d[0]*2>=D)return 1;
	for(int i=1;i<n;++i){
		for(int j=0;j<i;++j)
			if(d[i]<=d[j]+f[j])
				f[i]=max(f[i],min(l[i],d[i]-d[j]));
		if(f[i]+d[i]>=D)return 1; 
	}
	return 0;
}
int main(){
	int Tc;
	scanf("%d",&Tc);
	for(int ti = 1;	ti<= Tc;++ti){
		printf("Case #%d: %s\n",ti,anstr[solve()]);
	}
	return 0;
}
