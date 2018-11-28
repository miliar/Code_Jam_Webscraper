
#include <vector>
#include <stdlib.h>
#include <list>
#include <algorithm>
#include <stack>
#include <string>
#include <iostream>
#include <stdio.h>
#include <math.h>


using namespace std;

int mAbs(int x)
{
	if ( x < 0 ) return -x;
	return x;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int t;
	cin>>t;
	for (int tt = 1; tt <= t ;tt++)
	{
		int c;
		cin>>c;
		char cs[37][4];
		for (int x = 0 ; x < c ; x++) cin>>cs[x];

		int d;
		cin>>d;
		char ds[37][3];
		for (int x = 0 ; x < d ; x++) cin>>ds[x];

		int n;
		cin>>n;

		char rez[101];
		int i = 0;
		for (int x = 0 ; x < n ; x++)
		{
			cin>>rez[i];
			i++;
			if (i > 1)
			{
				for (int y = 0 ; y < c ; y++)
				{
					if ( (cs[y][0] == rez[i-1] && cs[y][1] == rez[i-2]) || (cs[y][1] == rez[i-1] && cs[y][0] == rez[i-2]) )
					{
						i-=1;
						rez[i-1] = cs[y][2];
						goto end;
					}
				}
				for (int y = 0 ; y < d ; y++)
				{
					for (int z = 0 ; z < i - 1; z++)
					{
						if ( (rez[z] == ds[y][0] && rez[i - 1] == ds[y][1]) || (rez[z] == ds[y][1] && rez[i - 1] == ds[y][0]) )
						{
							i = 0;
							goto end;
						}
					}
				}
			}
			end:;
		}

		printf("Case #%d: [",tt);
		for (int x = 0 ; x < i ; x++) 
		{
			if (x!=0) printf(", ");
			printf("%c",rez[x]);
		}
		cout<<"]"<<endl;
	}

}

