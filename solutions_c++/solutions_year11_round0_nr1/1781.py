#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int opos,j,t,bpos,ans,i,n,Tcases,opre,bpre;
	char op;
	//freopen("input.in","r",stdin);
	//ofstream fout("output.txt");
	cin>>Tcases;
	for( j = 1 ; j <= Tcases ; j++)
	{
		cin>>n;
		bpos = opos = 1 ;
		for ( ans = i = opre = bpre = 0 ; i < n ; i++)
		{
			scanf(" %c %d",&op,&t);
			if ( op == 'O' )
			{
				if( t > opos )
				{
					if( t > opos + opre )	
					{
						ans += t-opos-opre+1;
						bpre += t-opos-opre+1;
					}
					else
					{
						ans++;
						bpre++;
					}
				}
				else
				{
					if( t + opre > opos )
					{
						bpre++;
						ans++;
					}
					else
					{
						ans += opos+1-t-opre;
						bpre += opos+1-t-opre;
					}
				}
				opos = t ;
				opre = 0 ;
			}
			else
			{
				if( t > bpos )
				{
					if( t > bpos + bpre )	
					{
						ans += t-bpos-bpre+1;
						opre += t-bpos-bpre+1;
					}
					else
					{
						ans++;
						opre++;
					}
				}
				else
				{
					if( t + bpre > bpos )
					{
						opre++;
						ans++;
					}
					else
					{
						ans += bpos+1-t-bpre;
						opre += bpos+1-t-bpre;
					}
				}
				bpos = t ;
				bpre = 0 ;
			}
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
	return 0;
}