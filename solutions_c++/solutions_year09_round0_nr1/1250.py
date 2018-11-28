#include<stdio.h>
#include<iostream>

using namespace std;

int l,d,n;

int av[30][30];
string dict[6000];
char buff[2000];


int main(int argc,char ** argv)
{

	freopen (argv[1], "r",stdin);
	freopen ("alien.out", "w",stdout);

	scanf("%d",&l);
	scanf("%d",&d);
	scanf("%d",&n);

	for( int i=0;i<d;i++)
	{
		cin >> dict[i];
	}
	for( int tt=0;tt<n;tt++)
	{
		memset(av,0,sizeof(av));
		
		scanf("%s",buff);
		
		

		int poz = 0;
		for( int i=0;i<l;i++,poz++)
		{
			if( buff[poz] != '(' )
				av[i][buff[poz]-'a'] = 1;
			else
			{
				poz++;
				while( buff[poz] != ')' )
				{
					av[i][buff[poz]-'a'] = 1;
					poz++;
				}
			}
				
		
		}
		
		

		int tot = 0;
		for(int i=0;i<d;i++)
		{
			int good = 1;
			for(int j = 0; j<l;j++)
			{
				if( !av[j][dict[i][j] - 'a'])
				{
					good=0;
					break;
				}
			}
			tot+= good;
		}
		
		printf("Case #%d: %d\n",tt+1,tot);

	}
	
	return 0;
}

