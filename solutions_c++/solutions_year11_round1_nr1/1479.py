#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

int GCD(int a, int b)
{
	if(b==0) return a;
	return GCD(b, a%b);
}

const double eps = 1e-10;

int main()
{
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("A-small-attempt2.out", "w", stdout);
	//freopen("XXX-large.out", "w", stdout);
	int test, cas = 1;
	cin>>test;
	while(test--)
	{
		int N, Pd, Pg;
		cin>>N>>Pd>>Pg;
		int i;
		bool flag = false;
		for(i=1; i<=N; i++)
		{
			if(i*Pd % 100 != 0) continue;
			int D = i;
			int winD = i*Pd/100;

			for(int G=i; G<=100000; G++)
			{
				if(G*Pg % 100 != 0) continue;

				int winG = G*Pg / 100;
				if(winG>=winD && G-D>=winG-winD)
				{
					//cout <<winD << " " << D << " "<< winG << " " << G << endl;
					flag = true;
					break;
				}
			}
			//int a = 100;
			//int b = Pg;
			//int c = D*Pg - 100*winD;
			//if(c<0) c = -c;

			//double y = (100*1.0 - Pg*D*1.0 + 100*winD*1.0)/(1.0*Pg);
			//
			//if(c%GCD(a, b) == 0 && (y>1.0 || fabs(y-1.0) < eps))
			//{
			//	cout << D << " " << winD <<" " << c << " " << GCD(a, b)<< endl;
			//	flag = true;
			//	break;
			//}
		}
		cout << "Case #" << cas++ << ": ";
		if(flag) cout << "Possible" << endl;
		else cout << "Broken" << endl;
	}
	return 0;
}