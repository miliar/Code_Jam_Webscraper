#include <stdio.h>
#include <map>
#include <string>

using namespace std;

#define SMAX 102
#define QMAX 1002
#define INF 0x3f3f3f3f

int din[QMAX][SMAX];
int v[QMAX];
map<string,int> h;
char ch[128];
string s;

void solve(int T)
{
	int S,Q,mn;

	scanf("%d\n",&S);
        h.clear();

	for (int i=1;i<=S;i++)
	{
		fgets(ch,128,stdin);
		
		s.clear();
		for (int j=0;ch[j]!='\n';j++)
			s+=ch[j];
		h[s]=i;
	}

	scanf("%d\n",&Q);
	for (int i=1;i<=Q;i++)
	{
		fgets(ch,128,stdin);
		
		s.clear();
		for (int j=0;ch[j]!='\n';j++)
			s+=ch[j];
		v[i]=h[s];
	}

	mn=0;
	for (int i=1;i<=Q;i++)
	{
		for (int j=1;j<=S;j++)
			if (j==v[i]) din[i][j]=INF;
				else din[i][j]=min(din[i-1][j],mn+1);
		mn=INF;
		for (int j=1;j<=S;j++)
			mn=min(mn,din[i][j]);
	}
	printf("Case #%d: %d\n",T,mn);
}

int main()
{
	freopen("univ.in","r",stdin);
	freopen("univ.out","w",stdout);

	int n,i;

	for (scanf("%d\n",&n),i=1;i<=n;i++) solve(i);
	return 0;
}
