#include <iostream>
#include <cstring>
using namespace std;

#define N 1010
bool a[N];
int pri[N];
int num;

void Prime(){
    memset(a,0,sizeof(a));
    int i,j;
    for (i=2;i<N;++i){
		if (!a[i]) pri[num++]=i;
        for(j=0;j<num && i*pri[j]<N;++j){
            a[i*pri[j]]=1;
            if(!(i%pri[j])) break;
        }
    }
}
int p[N];                                   //p[i] represent father of i
int rank[N];                              //rank[i] represent the depth/rank of i 

int findset(int x){
	int px=x;
	
	while (px!=p[px]) px=p[px];             //find root
	return px;
}

void unionset(int x,int y){
	x=findset(x);
	y=findset(y);
	if (rank[x]>rank[y]) p[y]=x;
	else{
		p[x]=y;
		if (rank[x]==rank[y]) rank[y]++;
	}
}
		

bool ans[N];

int main()
{
	int i,j,k,t,div,a,b,l;
	int res;
	
	Prime();
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);

	scanf("%d",&t);
	for (k=1;k<=t;++k)
	{
		memset(ans,0,sizeof(ans));
		scanf("%d%d%d",&a,&b,&div);
		for (l=0;pri[l]<div;++l);
		for (i=a;i<=b;++i)
		{
			p[i]=i;
			rank[i]=0;
		}
		for (;pri[l]<b/2;++l)
		{
			for (i=a;i<=b;++i)
				if (i%pri[l]==0) break;
			if (i>b) continue;
		
			for (j=i;j<=b;++j)
				if (j%pri[l]==0)
					unionset(i,j);
		}
		for (i=a;i<=b;++i)
			ans[findset(i)]=true;
		for (res=0,i=a;i<=b;++i)
			if (ans[i]) ++res;
		printf("Case #%d: %d\n",k,res);
	}
	return 0;
}




