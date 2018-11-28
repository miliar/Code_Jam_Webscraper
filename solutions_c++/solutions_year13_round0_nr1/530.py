#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int T;
char s[6][6];

bool check(char c)
{
	bool ans=false;
	for (int i=0;i<4;i++)
	{
		bool flag=true;
		for (int j=0;j<4;j++) if (s[i][j]!='T' && s[i][j]!=c) flag=false;
		ans|=flag;
	}
	for (int i=0;i<4;i++)
	{
		bool flag=true;
		for (int j=0;j<4;j++) if (s[j][i]!='T' && s[j][i]!=c) flag=false;
		ans|=flag;
	}
	bool flag=true;
	for (int i=0;i<4;i++) if (s[i][i]!='T' && s[i][i]!=c) flag=false;
	ans|=flag;
	flag=true;
	for (int i=0;i<4;i++) if (s[i][3-i]!='T' && s[i][3-i]!=c) flag=false;
	ans|=flag;
	return ans;
}

bool full()
{
	for (int i=0;i<4;i++)
		for (int j=0;j<4;j++)
			if (s[i][j]=='.') return false;
	return true;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
    scanf("%d\n",&T);
    for (int ww=1;ww<=T;ww++)
	{
		printf("Case #%d: ",ww);
		for (int i=0;i<4;i++)
			scanf("%s\n",s[i]);
		bool xw=false,ow=false,fl=false;
		xw=check('X');
		ow=check('O');
		fl=full();
		if (xw) printf("X won\n");
		else if (ow) printf("O won\n");
		else if (fl) printf("Draw\n");
		else printf("Game has not completed\n");
	}
    return 0;
}
