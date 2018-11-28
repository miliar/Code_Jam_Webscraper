#include <iostream>
using namespace std;

char imap[100][100];
int nr,nc;
void readin()
{
	int i;
	scanf("%d%d\n",&nr,&nc);
	for(i = 0;i<nr;++i)
		gets(imap[i]);
}
bool alter(int r,int c)
{
	if(r == nr-1 || c == nc-1 )return false;
	if( (imap[r][c] !='#') || (imap[r+1][c]!='#')||(imap[r][c+1]!='#')||
		(imap[r+1][c+1]!='#'))return false;
	imap[r][c] = '/';
	imap[r][c+1] = '\\';
	imap[r+1][c] = '\\';
	imap[r+1][c+1] = '/';
	return true;
}
void work(int CaseNum)
{
	bool flag = true;
	int i,j;
	for(i = 0;i< nr && flag;++i)
		for(j = 0;j< nc && flag;++j)
			if(imap[i][j] =='#')
		{
			flag = alter(i,j);
		}
    printf("Case #%d:\n",CaseNum);
	if(flag == false)
	{
		printf("Impossible\n");
	}
	else 
	{
		for(i = 0;i<nr;++i)
		{
			puts(imap[i]);
		}
	}
}
int main()
{
	int tcase;
	int i;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&tcase);
	for(i = 1;i<=tcase;++i)
	{
		readin();
		work(i);
	}
	return 0;
}