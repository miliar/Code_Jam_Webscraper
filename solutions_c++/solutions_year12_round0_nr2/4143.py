#include<stdio.h>
#include<vector>
#include<map>
#include<string>
#include<string.h>
#include<sstream>
#include<queue>
#include<math.h>
#include<iostream>

using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n, s, p, t, pts[111], mp[111];
	cin >> t ;
	for(int tc=1 ; tc<=t ; tc++ )
	{
		cin >> n >> s >> p ;
		for(int i=0 ; i<n ; i++)
			cin >> pts[i] ;
		int cnt=0 ;
		for(int i=0 ; i<n ; i++)
		{
			int b = pts[i]/3;
			if ( pts[i]%3==0 )
			{
			  if (b >= p)
				  cnt++;
			  else
			  {
				if (s > 0 && b > 0 && b + 1 >= p)
				{            
				  cnt++;
				  s--;
				}            
			  }
			}

			else if ( pts[i]%3==1 )
			{
			  if (b >= p || b+1 >= p)
				  cnt++;
			  else
			  {
				if (s > 0 && b + 1 >= p)
				{
				  cnt++;
				  s--;
				}
			  }
			}

			else
			{          
			  if (b + 1 >= p || b >= p)
				cnt++;
			  else
			  {
				if (s > 0 && b + 2 >= p)
				{
				  cnt++;
				  s--;
				}
			  }
			}
		}
		cout << "Case #" << tc << ": " << cnt << endl ;
	}
	//while(1);
}