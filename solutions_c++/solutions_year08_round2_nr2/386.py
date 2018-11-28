#include <cstdio>

using namespace std;

int factors[1001][1001];
int c[1001],a,b,c2[1001],p;

void factorize(int arg){
	int p=2,n=arg;
	factors[arg][0]=0;
	while(arg>1){
		if(arg%p==0)factors[n][++factors[n][0]]=p;
		while(arg%p==0)arg/=p;
		p++;
	}
}

int havecommon(int a,int b){
	for(int i=1;i<=factors[a][0];i++)
		for(int j=1;j<=factors[b][0];j++)
			if(factors[a][i]==factors[b][j] && factors[a][i]>=p)return 1;
	return 0;
}

void paint(int c1,int c2){
	for(int i=a;i<=b;i++)
		if(c[i]==c2)c[i]=c1;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int n,i,j,q,k,ans;
	scanf("%d",&q);
	for(k=1;k<=q;k++){
		scanf("%d%d%d",&a,&b,&p);
		for(i=a;i<=b;i++){
			factorize(i);
			c[i]=i;
		}
		for(i=a;i<b;i++)
			for(j=a;j<=b;j++)
				if(havecommon(i,j) && c[i]!=c[j])paint(c[i],c[j]);
		for(i=0;i<1001;i++)c2[i]=0;
		for(i=a;i<=b;i++)c2[c[i]]++;
		ans=0;
		for(i=0;i<1001;i++)if(c2[i])ans++;
		printf("Case #%d: %d\n",k,ans);
	}

	return 0;
}


//compiled with Visual Studio 2005
