#include <iostream>
#include <stdlib.h>
#include <stdio.h>

#define cyc(i,n) for (i=0; i<n; i++)

using std::cin;
using std::cout;
using std::string;

int t_,T_;
double X,S,R;
int n,N;
double t,ans;
double B,E,w_temp;
double L[1000];
double w[1000];
bool used[1000];

int findminWW()
{
	int n;
	int ans = 0;
	double min_w = 200.0; // infinity

	cyc(n,N)
	{
		if ( w[n] < min_w && !used[n] )
		{
			min_w = w[n];
			ans = n;
		}
	}

	used[ans] = true;
	if (min_w < 200.0)
		return ans;
	else
		return 1001;
}

int main()
{
	cin >> T_;
	
	cyc(t_,T_)
	{
		cin >> X >> S >> R >> t >> N;

		ans = X / S;

		cyc(n,N)
		{
			cin >> B >> E >> w_temp;
			L[n] = E - B;
			w[n] = w_temp;
			used[n] = false;

			X -= L[n];
			ans += (L[n]/(w[n] + S) - L[n]/S);
		}

		// use up nonwalkway runtime
		// if it can't be used, use most of it

		if ( X / R > t )
		{
			ans -= t * ( R/S - 1.0 );
			t = 0.0;
		}
		else
		{
			ans -= X * (R-S) / (S * R);
			t -= X / R;
		}

		while ( t > 0.0 )
		{
			// find first minimal speed WW

			n = findminWW();
			if (n == 1001)
				break;

			// if it can be used up use it up
			// else use most of it

			if ( L[n] / (R + w[n]) > t )
			{
				ans -= t * ( (R + w[n]) / (S + w[n]) - 1.0 );
				t = 0.0;
			}
			else
			{
				ans -= L[n] * (R-S) / ((S+w[n])*(R+w[n]));
				t -= L[n] / (R + w[n]);
			}
		}

		printf("Case #%d: %.6f\n",t_+1,ans);
	}
	return 0;
}
