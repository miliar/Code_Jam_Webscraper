#include<iostream>
#include<algorithm>
#include<vector>
#include<set>

using namespace std;

struct Triple	{
    int d, x, y;
    Triple( int d, int x, int y ) : d( d ), x( x ), y( y ) {}
};

Triple egcd( int a, int b )		{
	if( b==0 ) return Triple( a,  1,  0 );
    Triple q = egcd( b, a % b );
    return Triple( q.d, q.y, q.x - a / b * q.y );
}

int main()
{
    int T,totalcase;
    cin>>T;
    totalcase=T;
    
    while(T)
    {
 		int n,l,h;
		 cin>>n>>l>>h;
		 
		 vector<int> f;
		 
		 for(int i =0;i<n;i++)
		 {
				int j;
				cin>>j;
				f.push_back(j);
				
		}
		
		int i;
		for( i=l;i<=h;i++)
		{
			int flag = 1;
			
			for(int j=0;j<f.size();j++)
			{
				if(f[j]%i==0 ||i%f[j]==0)
				{
				}
				else
				{
					flag =0;
				}
			}
			
			if(flag == 1)
			{
				cout<<"Case #"<<totalcase - T+1<<": "<<i<<endl;
				break;
			}
		}
		
		if(i>h)
		{
			cout<<"Case #"<<totalcase - T+1<<": NO"<<endl;
		}
            
            
            T--;
    }
    
    return 0;
    
}
