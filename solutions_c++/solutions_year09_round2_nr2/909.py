#include<cstdio>
#include<algorithm>
using namespace std;

int main()
{
	int T,t,i,j,k,d;
	char S[32],aux;

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	scanf("%d",&T);
	for(t=1;t<=T;++t)
	{
		scanf("%s",S);
		d=strlen(S);
		for(i=d-2;i>=0;--i)
		{
			for(j=i+1;j<d;++j)
				if(S[j]>S[i]) break;
			if(j<d) break;
		}

		if(i>=0)
		{
			for(k=j+1;k<d;++k)
				if(S[k]>S[i] && S[k]<S[j]) j=k;

			aux=S[i]; S[i]=S[j]; S[j]=aux;
			sort(S+i+1,S+d);
		}
		else
		{
			S[d++]='0'; S[d]=NULL;
			sort(S,S+d);
			for(i=0;S[i]=='0';++i);
			aux=S[0]; S[0]=S[i]; S[i]=aux;
		}
		printf("Case #%d: %s\n",t,S);
	}

	return 0;
}
