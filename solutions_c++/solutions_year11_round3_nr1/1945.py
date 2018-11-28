#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 



using namespace std; 

template<class T> T gcd(T a,T b){return a==0?b:gcd(b%a,a);}
FILE *f;
int main()
{
	int t;
	int r;
	int c;
	char f[51][51];
	
	freopen("do.txt","r",stdin);
	freopen("fian.txt","w",stdout);
    cin>>t;
	for(int i=0;i<t;i++)
	{
		int b=0;
		cin>>r>>c;
		for(int j=0;j<r;j++)
			for(int k=0;k<c;k++)
				cin>>f[j][k];
		for(int j=0;j<r;j++)
			for(int k=0;k<c;k++)
			{
				if(f[j][k]=='#')
				{
					if(j==r-1||k==c-1)
					{
							b=1;
							break;					
					}
					f[j][k]='/';
					if(f[j+1][k]=='#'&&f[j+1][k]=='#'&&f[j+1][k+1]=='#')					
					{
						f[j+1][k]='\\';
						f[j][k+1]='\\';
					    f[j+1][k+1]='/';
						continue;
					}
					b=1;
					break;
				
				}
			}
				if(b==1)cout<<"Case #"<<i+1<<":"<<endl<< "Impossible"<<endl;
				else
				{
					cout<<"Case #"<<i+1<<":"<<endl;
					for(int j=0;j<r;j++)
	             	{
							for(int k=0;k<c;k++)
				            cout<<f[j][k];
							cout<<endl;

					}
		
				}
			}

		

		
		
	

}