#include<cstdio>
#include<cstdlib>
#include<cstring>

#define MAX 2051
#define MM 1000000000

int p,n,ppp[30],M[MAX],visit[MAX][MAX],price[MAX];
long long f[MAX][MAX];


int Get(int now) {
	int k = -1;
	while (ppp[k+1]<=now) k++;
	return k;
}


long long Min(long long a,long long b) {
     if  (a<b) return a;
       else return b;
}

long long Solve(int i,int last) {
    int t=0; 
	if(Get(i)==p)
	{
		while(1)
		{
			++t,last -= last & (-last);
			if (last == 0) break;
		}
		if(M[i-ppp[p]]<p-t) return MM;
		return 0;
	}
	if (visit[i][last]) return f[i][last];
	visit[i][last] = 1;
	long long
    t1 = Solve(i*2,last)+Solve(i*2+1,last),
    t2 = price[i]+Solve(i*2,last|(1<<Get(i)))+Solve(i*2+1,last|(1<<Get(i)));
	f[i][last] = Min(t1,t2);
	return f[i][last];
}

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int i,j,k,test,ttest;
	scanf("%d",&test);
	ppp[0]=1;
	for(k = 1; k<=15; k++)
		ppp[k] = ppp[k-1]*2;	
	for (ttest = 1; ttest<=test; ttest++) {
        memset(visit,0,sizeof visit);
		memset(f,0,sizeof f);
		scanf("%d",&p);
		int t = 1<<p;
		for( i = 0; i<t ; i++)
			scanf("%d",&M[i]);
			
		for(i = p-1;i>=0;i--)
			for(j = ppp[i]; j<ppp[i+1]; j++)
				scanf("%d",&price[j]);
		printf("Case #%d: %I64d\n",ttest,Solve(1,0));
	}
	return 0;
}
