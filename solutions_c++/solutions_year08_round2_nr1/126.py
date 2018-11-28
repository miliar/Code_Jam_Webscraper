#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("output.txt");
ifstream fin("input.txt");


long long tots[9];

int main(void)
{
	int ttt;
	cin >> ttt;
	int ct = 0;
	while(ttt>0)
	{
		ct++;
		ttt--;
		long long i,j,k,a,b,n,m;
		long long x,y,c,d;
		cin >> n >> a >> b >> c >> d >> x >> y >> m;
		memset(tots,0,sizeof(tots));
		for(i=0; i<n; i++)
		{
			tots[3*(x%3)+(y%3)]++;
			//cout << x << " " << y << " ";
			x=(a*x+b)%m;
			y=(c*y+d)%m;
		}
		//cout << endl;
		long long ans = 0;
		for(i=0; i<9; i++)
		{
			for(j=i; j<9; j++)
			{
				for(k=j; k<9; k++)
				{
					if( (i%3 + j%3 + k%3)%3!=0 || (i/3 + j/3 + k/3)%3!=0)
						continue;
					//cout << i << " " << j << " " << k << endl;
					if(i==j && j==k)
					{
						ans+=(tots[i]*(tots[i]-1)*(tots[i]-2))/6;
					}
					else if(i==j)
					{
						ans+=(tots[i]*(tots[i]-1))/2*tots[k];
					}
					else if(j==k)
					{
						ans+=(tots[j]*(tots[j]-1))/2*tots[i];
					}
					else
					{
						ans+=tots[i]*tots[j]*tots[k];
					}
				}
			}
		}
		
		
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
	}

	
	return 0;
}

