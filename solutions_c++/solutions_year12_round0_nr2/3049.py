#include<iostream>
using namespace std;

int totals[105];

struct score
{
	int sz[2]; //surprise score total
};
score scores[11];
int main()
{
	freopen("in.in" , "r" ,stdin);
	freopen("out.txt" ,"w",stdout);
    memset(scores , 0 ,sizeof(scores));
	for(int i = 2; i <= 10 ; ++i)
	{
		score s;
		s.sz[0] = 3 * i - 3;
		s.sz[1] = 3*i - 4;
		scores[i] = s;
	}

	int t ,n ,s ,p;
	cin >> t;
	for(int i = 1 ; i <= t; ++i)
	{
		int ans = 0;
		cin >> n >> s >> p;
		int small = 3 *p -2;
		if(p == 0) small = 0;
		//int a,b,c;
		//if(p >= 2)
		/*
		int a = 3*p-3;
		int b = 3*p - 4;
		int c = 3 *p -2;
		*/
		int z = 0 ; //记下suprize数个数
		for(int j = 1; j <= n ; ++j)
		{

			cin >> totals[j];
			if(totals[j] >= small )
			{
				++ans;
			}
			else
			{
				if(p == 1)
				{
					    if(totals[j] >0 )
						{
							++z;
							++ans;
						}
				}
				else if( totals[j] == scores[p].sz[0] || totals[j] == scores[p].sz[1])
				{
					++ans;
					++z;
				}

			}
		}
		if(z > s)
			ans = ans - z + s;
        cout << "Case #" << i  << ": "<<ans << endl;
	}
	return 0;
}