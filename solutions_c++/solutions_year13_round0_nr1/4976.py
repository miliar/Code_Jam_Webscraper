#include<iostream>
char s[5][5];
void ans(int T,char s[])
{
	printf("Case #%d: %s\n",T,s);
}

bool row(int j,char ch)
{
	for(int i=0;i<4;i++)
		if(s[j][i]!=ch&&s[j][i]!='T') return false;
	return true;
}
bool column(int j,char ch)
{
	for(int i=0;i<4;i++)
		if(s[i][j]!=ch&&s[i][j]!='T') return false;
	return true;
}
bool f(char ch)
{
	for(int i=0;i<4;i++)
		if(s[i][i]!=ch&&s[i][i]!='T') return false;
	return true;
}
bool g(char ch)
{
	for(int i=0;i<4;i++)
		if(s[i][4-i-1]!=ch&&s[i][4-i-1]!='T') return false;
	return true;
}
void solve(int T)
{
	int i,j,empty=0;
	for(i=0;i<4;i++)
	{
		scanf("%s",s[i]);
		for(j=0;j<4;j++) if(s[i][j]=='.') empty++;
	}
	for(i=0;i<4;i++) 
	{
		if(row(i,'O')||column(i,'O')) return ans(T,"O won");
		if(row(i,'X')||column(i,'X')) return ans(T,"X won");
	}
	if(f('O')||g('O')) return ans(T,"O won");
	if(f('X')||g('X')) return ans(T,"X won");
	if(empty) return ans(T,"Game has not completed");
	ans(T,"Draw");
}

int main()
{
	int i,T;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for(i=1;i<=T;i++) solve(i);
	return 0;
}