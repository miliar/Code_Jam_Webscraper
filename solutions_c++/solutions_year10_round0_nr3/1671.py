#include<iostream>
#include<map>
#include<queue>
#include<vector>
#include<set>
#include<sstream>
#include<cmath>
#include<algorithm>
#define oo (int)1e9
#define s(n)scanf("%d",&n)
using namespace std;
#include<string.h>
#include<cstdio>
#define gcd __gcd
#define lcm(a,b) (a/gcd(a,b))*b
#define mod 1000000007

int n,k;
int cs;
int R;
vector<int>v;

int main()
{
	
//	freopen("C.in","r",stdin);
//	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);	
	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);	
	
	int runs,tmp;
	s( runs );
	while( runs-- )
	{
		long long soln = 0;
		s( R );s( k );s( n );
		map< vector<int> , long long>m;
		vector< vector<int> >VV;
		v.clear();
		for(int i=0;i<n;i++)
		{
			s( tmp );
			v.push_back( tmp );
			
		}
		
		while( R-- )
		{
			
			//for(int i=0;i<n;i++) printf( "%d " , v[i]  );printf( "\n" );
			long long sum = 0;
			int pos = -1;
			for(int i=0;i<n ;i++ )
			{
				if( sum + v[i] <= k )
					sum += v[i];
				else
				{
					pos = i;
					break;
				}
			}
			
			//cout << pos << endl;
			
			if( pos == -1 )
			{
				soln += sum*(R+1)	;
				break;
			}
			else
			{
				map< vector<int> , long long> :: iterator ii = m.find( v );
				
				if( ii == m.end() )
				{
					m[v] = sum;
					soln += sum;
					VV.push_back( v );
				}
				else
				{
					
					int pp2 = -1;
					for(int j=0;j<VV.size();j++)
					{
						if( VV[j] == v )
						{
							pp2 = j;
							break;
						}
					}
					
					/*for(int j=0;j<VV.size();j++)
					{
						vector<int>govt = VV[j];
						
						for(int K=0;K<govt.size();K++)cout << govt[K] << " ";cout << endl;
						
					}
					cout << endl;
					cout << soln << endl;*/
					vector< long long >tt;
					while( pp2 != VV.size()  )
					{
						long long ttt = m[ VV[pp2] ];
						tt.push_back( ttt );
						//soln += ttt;
						pp2++;
					}
					R++;
					if( R > 0 )
					{
						long long gg = 0;
						for(int i=0;i<tt.size();i++)
						gg += tt[i];
						
						gg *= (R/tt.size());
						int till = R % tt.size();
						
						for(int i=0;i<till;i++)
						gg += tt[i];
						
						soln += gg;
					}
					
					break;
					
				}
				
				vector<int>tt;
				int xx = pos;
				for(;pos<n;pos++)tt.push_back( v[pos] );
				for(int i=0;i<xx;i++)tt.push_back( v[i] );
				
				v = tt;
			}
		
		
		
	
		}
		printf( "Case #%d: %lld\n" , ++cs , soln );
		
		
	}
}
