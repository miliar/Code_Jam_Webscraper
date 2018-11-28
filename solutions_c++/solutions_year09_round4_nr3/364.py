#include <iostream>
#include <vector>
#include <string>
#include <cmath>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)

using namespace std;

typedef long long ll;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <ll> VL;
typedef vector <VL> VVL;


int n,k;
VVI pr;
VVI ok;
int res;
VVI lg;


bool bien (int a, int b)
{
	fi (k-1)
	{
		if (pr[a][i]>=pr[b][i] and pr[a][i+1]<=pr[b][i+1])
			return false;
		if (pr[a][i]<=pr[b][i] and pr[a][i+1]>=pr[b][i+1])
			return false;
	}
	return true;
}

int mn (int a, int b)
{
	return a<b?a:b;
}

void back (int a)
{
	if (lg.size()>=res)
		return;
	if (a==n)
	{
		res=mn(res,int(lg.size()));
		return;
	}
	bool cb=false;
	fi (lg.size())
	{
		bool pc = true;
		for (int j=0;j<lg[i].size() and pc;j++)
		{
			if (not ok[a][lg[i][j]])
				pc=false;
		}
		if (pc)
		{
			lg[i].push_back(a);
			back(a+1);
			lg[i].pop_back();
			cb=true;
		}
	}
	if (not false)
	{
		VI nv (1,a);
		lg.push_back(nv);
		back(a+1);
		lg.pop_back();
	}
}

int calc ()
{
	cin >> n >> k;
	pr = VVI (n,VI(k));
	fi (n)
		fj (k)
			cin >> pr[i][j];
	ok=VVI(n, VI (n));
	fi (n)
	{
		fj (n)
		{
			ok[i][j]=bien(i,j);
		}
	}
	res=n;
	lg=VVI(0);
	back(0);
	return res;
}

int main()
{
	int C;
	cin >> C;
	for (int caso=1;caso<=C;caso++)
	{
		cout << "Case #" << caso << ": " << calc() << endl;
	}
}
