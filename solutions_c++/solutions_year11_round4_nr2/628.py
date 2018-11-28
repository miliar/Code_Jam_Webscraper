#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <set>

using namespace std;
const int maxn = 1000;
int mas[maxn][maxn];

void init()
{
	for(int i = 0 ; i < maxn ;i++)
		for(int j = 0 ; j < maxn;j++)
				mas[i][j] =0;
}
int to_int(char ch)
{
	return ch - '0';
}
void test(int T)
{
	
	init();	
	int r,c,d;
	cin >> r >> c >> d;
	char ch;

	for(int i = 0 ;i < r ; i++)
		for(int j = 0 ; j < c ; j++)
		{
			cin>> ch ;
			mas[i][j] = to_int(ch);
		}

	int res ,result;
	double sx,sy;
	bool check = false;
	for(res=min(r,c);res>2&& check == false;res--)
	{
		for(int i=0;i+res<=r&& check == false;i++)
		{
			for(int j=0;j+res<=c&& check == false;j++)
			{
				sx=0;
				sy=0;
				
				for(int x=0;x<res&& check == false;x++)
					for(int y=0;y<res && check == false;y++)
					{
						sx+=(x-0.5*(res-1))*mas[i+x][j+y];
						sy+=(y-0.5*(res-1))*mas[i+x][j+y];
					}
				sx-=(0-0.5*(res-1))*mas[i][j];
				sy-=(0-0.5*(res-1))*mas[i][j];

				sx-=(0-0.5*(res-1))*mas[i][j+res-1];
				sy-=(0.5*(res-1))*mas[i][j+res-1];

				sx-=(0.5*(res-1))*mas[i+res-1][j];
				sy-=(0-0.5*(res-1))*mas[i+res-1][j];

				sx-=(0.5*(res-1))*mas[i+res-1][j+res-1];
				sy-=(0.5*(res-1))*mas[i+res-1][j+res-1];

				if(sx==0.0 && sy==0.0)
				{
					cout << "Case #" << T << ": " << result << '\n';
					return;
				}
			}
		}
	}
		cout << "Case #" << T << ": IMPOSSIBLE\n";
}

int main()
{
	freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	int t;
	cin>>t;

	for(int i = 0 ; i < t;i++)
	{	
		test(i + 1);
	}

	return 0;
}