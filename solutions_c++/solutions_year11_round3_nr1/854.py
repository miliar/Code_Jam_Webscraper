#include<algorithm>
#include<iostream>
#include<iomanip>
#include<string>
#include<cmath>
using namespace std;

#define coutfpre(n,f) (setiosflags(ios::fixed)<<setprecision(n)<<f) 
#define zero(n) memset(n,0,sizeof(n))
#define m1set(n) memset(n,-1,sizeof(n))
#define p1set(n) memset(n,1,sizeof(n))

#define min(m,n) ((m<n)?m:n)
#define max(m,n) ((m>n)?m:n)


char iCin[51][51];
char iCout[51][51];
int R,C;
int set(int i,int j)
{

	if((i+1)>=R || (j+1)>=C)
		return -1;

	iCin[i][j] = '.';
	iCout[i][j] = '/';

	if(iCin[i][j+1] == '#')
	{
		iCin[i][j+1] = '.';
		iCout[i][j+1] = '\\';
	}
	else
	{
		return -1;
	}

	if(iCin[i+1][j] == '#')
	{
		iCin[i+1][j] = '.';
		iCout[i+1][j] = '\\';
	}
	else
	{
		return -1;
	}

	if(iCin[i+1][j+1] == '#')
	{
		iCin[i+1][j+1] = '.';
		iCout[i+1][j+1] = '/';
	}
	else
	{
		return -1;
	}
	return 1;

}
int main()
{
	int T;
    freopen("A.in" , "r" , stdin);
    freopen("A.out" , "w" , stdout);
    cin>>T;
    for(int caseID = 1 ; caseID <= T ; caseID ++)
    {
		
		int impossible = 0;
		memset(iCout,'.',sizeof(iCout));
		cin>>R;
		cin>>C;
		for(int i=0;i<R;i++)
		{
			for(int j=0;j<C;j++)
			{
				cin>>iCin[i][j];
			}
		}
		
		for(int i=0;i<R;i++)
		{
			for(int j=0;j<C;j++)
			{
				if(iCin[i][j] == '#')
				{
					if(i==0)
					{
						if(j==0)
						{
							if(-1 == set(i,j))
							{
								impossible = 1;
								break;
							}
						}
						else if(iCin[i][j-1] == '.')
						{
							if(-1 == set(i,j))
							{
								impossible = 1;
								break;
							}
						}
					}
					else if(iCin[i-1][j] == '.')
					{
						if(j==0)
						{
							if(-1 == set(i,j))
							{
								impossible = 1;
								break;
							}
						}
						else if(iCin[i][j-1] == '.')
						{
							if(-1 == set(i,j))
							{
								impossible = 1;
								break;
							}
						}
					}
				}
			}
			if(impossible == 1)
			{
				break;
			}
		}
		cout<<"Case #"<<caseID<<": "<<endl;
		if(impossible)
		{
			cout<<"Impossible"<<endl;
		}
		else
		{
			for(int i=0;i<R;i++)
			{
				for(int j=0;j<C;j++)
				{
					if(iCout[i][j]!='/'&&iCout[i][j]!='\\')
					{
						cout<<'.';
					}
					else
						cout<<iCout[i][j];
				}
				cout<<endl;
			}
		}
	
    }
    return 0;
}
