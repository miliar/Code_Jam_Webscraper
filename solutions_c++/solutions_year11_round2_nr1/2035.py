#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

vector <string> a;
vector <double> wp;
vector <double> owp;
vector <double> oowp;
vector <double> rpi;
vector <set <int> > played;

void calc_wp(int n)
{
	int i, j, c = 0, w = 0;
	for(i = 0; i < n; i ++)
	{
		c = 0;
		w = 0;
		set <int> temp;
		for(j = 0; j < n; j ++)
		{
			if(a[i][j] != '.')
			{
				temp.insert(j);
				c ++;
				if(a[i][j] == '1')
					w ++;
			}
		}
		//printf("w = %d c = %d\n", w, c);
		played.push_back(temp);
		wp.push_back(((double) w) / ((double) c));
	}
}

void calc_owp(int n)
{
	int i, j;
	set <int> :: iterator it;
	for(i = 0; i < n; i ++)
	{
		double owinp = 0.0;
		//printf("for team %d: ", i);
		for(it = played[i].begin(); it != played[i].end(); it ++)
		{
			double temp = played[*it].size() * wp[*it];
			if(a[i][*it] == '0')
				temp -= 1.0;
			//printf("%d %lf ", *it, temp);
			temp /= (double) (played[*it].size() - 1);
			//printf("%lf ", temp);
			owinp += temp;
		}
		//printf("\n");
		owinp /= (double)played[i].size();
		owp.push_back(owinp);
	}
}

void calc_oowp(int n)
{
	int i, j;
	set <int> :: iterator it;
	for(i = 0; i < n; i ++)
	{
		double oowinp = 0.0;
		for(it = played[i].begin(); it != played[i].end(); it ++)
		{
			oowinp += owp[*it];
		}
		oowinp /= (double)played[i].size();
		oowp.push_back(oowinp);
	}
}

void calc_rpi(int n)
{
	int i;
	for(i = 0; i < n; i ++)
	{
		rpi.push_back(1.0 / 4.0 * wp[i] + 1.0 / 2.0 * owp[i] + 1.0 / 4.0 * oowp[i]);
	}
}

int main()
{
	int t, z;
	scanf(" %d", &t);
	for(z = 0; z < t; z ++)
	{
		int n, i, j;
		string temp;
		scanf(" %d", &n);
		for(i = 0; i < n; i ++)
		{
			cin >> temp;
			a.push_back(temp);
		}
		calc_wp(n);
		calc_owp(n);
		calc_oowp(n);
		calc_rpi(n);
		/*for(i = 0; i < n; i ++)
		{
			printf("for team %d %lf %lf %lf\n", i, wp[i], owp[i], oowp[i]);
		}*/
		printf("Case #%d:\n", z + 1);
		for(i = 0; i < n; i ++)
			printf("%lf\n", rpi[i]);
		wp.clear();
		played.clear();
		a.clear();
		owp.clear();
		oowp.clear();
		rpi.clear();
	}
}
