#include<cstdio>
#define LMAX 16
#define DMAX 5000
#define Sigma 26
using namespace std;
bool Good[LMAX][Sigma];
char Words[DMAX][LMAX];
int L,D,N;

int main()
{
	char pattern[421];
	int i,j,t,ans;

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	scanf("%d%d%d",&L,&D,&N);
	for(i=0;i<D;++i)
		scanf("%s",Words[i]);

	for(t=1;t<=N;++t)
	{
		scanf("%s",pattern);
		for(i=0;i<L;++i)
			for(j=0;j<Sigma;++j)
				Good[i][j]=0;

		for(i=j=0;i<L;++i,++j)
			if(pattern[j]=='(')
				for(++j;pattern[j]!=')';++j)
					Good[i][pattern[j]-'a']=1;
			else
				Good[i][pattern[j]-'a']=1;

		for(ans=i=0;i<D;++i)
		{
			for(j=0;j<L && Good[j][Words[i][j]-'a'];++j);
			ans+=j==L;
		}
		printf("Case #%d: %d\n",t,ans);
	}

	return 0;
}
