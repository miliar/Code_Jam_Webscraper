#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stdio.h>
#include <math.h>

using namespace std;

#define CLEAR(x,with) memset(x,with,sizeof(x))  
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define sz(a) int((a).size())

typedef pair<int,int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

int main()
{
	int N;

	cin >> N;
	for(int c=1; c<=N; c++)
	{
		double ans = 0;
		int N;
		cin >> N;
		int x[3], y[3], r[3];

		for(int i=0; i<N; i++)
			cin >> x[i] >> y[i] >> r[i];

		if(N == 1) ans = r[0];
		else if(N == 2)
		{
			if(r[0] < r[1]) ans = r[1];
			else ans = r[0];
		}
		else
		{
			double min = -1;
			for(int i=0; i<3; i++)
			{
				for(int j=i+1; j<3; j++)
				{
					double check = sqrt((double)(x[i] - x[j]) * (double)(x[i] - x[j]) + (double)(y[i] - y[j]) * (double)(y[i] - y[j])) + (double)r[i] + (double)r[j];
					check /= 2.;
					if( min == -1 || check < min )
					{
						for(int k=0; k<3; k++)
						{
							if(k==i || k==j) continue;
							if( r[k] < check )
								min = check;
							else
							{
								if(r[k] > check && (min == -1 || r[k] < min))
									min = r[k];
							}
						}
					}
				}
			}
			ans = min;
		}
		cout << "Case #" << c << ": " << ans << endl;
	}

	return 0;
}
