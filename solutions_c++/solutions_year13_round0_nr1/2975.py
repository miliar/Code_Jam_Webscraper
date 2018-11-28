#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int Maxn=6;

char a[Maxn][Maxn];
int T;

bool Check(char ch)
{
	for (int i=0;i<4;++i)
	{
		int cnt=0;
		for (int j=0;j<4;++j)
			if (a[i][j]==ch || a[i][j]=='T') ++cnt;
		if (cnt==4) return true;
		cnt=0;
		for (int j=0;j<4;++j)
			if (a[j][i]==ch || a[j][i]=='T') ++cnt;
		if (cnt==4) return true;
	}
	
	int cnt=0;
	for (int i=0;i<4;++i)
		if (a[i][i]==ch || a[i][i]=='T') ++cnt;
	if (cnt==4) return true;
	cnt=0;
	for (int i=0;i<4;++i)
		if (a[i][3-i]==ch || a[i][3-i]=='T') ++cnt;
	return (cnt==4);
}

	
int main()
{
	freopen("A2.in","r",stdin);
	freopen("A2.out","w",stdout);

	scanf("%d",&T);
	for (int ii=1;ii<=T;++ii)
	{
		printf("Case #%d: ",ii);

		int tot=0;
		for (int i=0;i<4;++i)
		{
			scanf("%s",a[i]);
			for (int j=0;j<4;++j)
				if (a[i][j]=='.') ++tot;
		}

		if (Check('O')) printf("O won\n");
		else if (Check('X')) printf("X won\n");
		else if (!tot) printf("Draw\n");
		else printf("Game has not completed\n");
	}

	return 0;
}
