#include<cstdio>
using namespace std;

char Dic[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int T;
char S[5000000];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d ",&T);
	int t;
	for (t=1;t<=T;t++)
	{
		gets(S);
		for (unsigned i=0;S[i];i++)
			if (S[i]!= ' ')
				S[i] = Dic[S[i] - 'a'];
		printf("Case #%d: %s\n",t,S);
		
	}
	return 0;
}
	
