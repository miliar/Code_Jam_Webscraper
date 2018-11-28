#include <iostream>
using namespace std;
#define tiao system("pause")

char dict[5001][55];
bool p[55][300];
int n,l,d,cnt(0);

bool ok(int t)
{
	for (int i=0; i<l; i++)
		if (!p[i][dict[t][i]]) return false;
	
	return true;
}
int main(void)
{
	int i,j,k,ci,cici,cicici,pos;
	char ch;
	
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	scanf("%d%d%d",&l,&d,&n);
	for (i=1; i<=d; i++) scanf("%s",dict[i]);
	getchar();

	for (int cb=1; cb<=n; cb++)
	{
		memset(p,0,sizeof(p));
		pos = 0;
		
		ch = getchar();
		while(ch != '\n')
		{
			if (ch == '(')
			{
				ch = getchar();
				while(ch != ')')
				{
					p[pos][ch] = true;
					ch = getchar();
				}
				
				pos++;
			}
			else
			{
				p[pos][ch] = true;
				pos++;
			}
			
			ch = getchar();
		}	
		
		cnt = 0;
		for (i=1; i<=d; i++)
			if (ok(i)) cnt++;
		
		printf("Case #%d: %d\n",cb,cnt);
	}

//	tiao;
	return 0;
}
