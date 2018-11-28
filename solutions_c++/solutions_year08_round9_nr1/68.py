#include <iostream>
#include <vector>

using namespace std;



int n;
long double a[11000], b[11000], c[11000];
int cc[11000], aa[11000], bb[11000];

long double curc;
int curcc;
int ans = 0;


void Load()
{
	cin >> n;
	int i;
	for (i = 0; i < n; i++)
	{
		cin >> aa[i] >> bb[i] >> cc[i];
		a[i] = aa[i] / 10000.0;
		b[i] = bb[i] / 10000.0;
		c[i] = cc[i] / 10000.0;
	}
}

void Solve()
{
	int i, j;
	ans = 0;
//	cerr << "case\n";

	vector <pair <long double ,int> > ev;
	for (i = 0; i < n; i++)
	{
		curcc = cc[i];
	    curc = c[i];
//	    cerr << curc<< " curc\n";
	    ev.clear();
	    for (j = 0; j < n; j++)
	    {
	    	if (cc[j] > curcc) continue;
	    	long double l, r;
	    	if (curcc < 10000)
	    	{
	    		l = a[j]/(1-curc);
		    	r = 1-b[j]/(1-curc);
		    }
		    else 
		    {
		    	if (aa[j] != 0 || bb[j] != 0) continue;
		    }
	//    	cerr << l << " " << r << "\n";
	    	if (l < r+1e-6)
	    	{
		    	ev.push_back(make_pair(l, -1));
		    	ev.push_back(make_pair(r, 1));
		    }
	    }
	    if (ev.size() > 0) sort(ev.begin(), ev.end());
	    int k = 0;
	    for (j = 0; j < ev.size(); j++)
	    {
	    	if (-k > ans) ans = -k;
	    	k += ev[j].second;
	    	if (-k > ans) ans = -k;
	    }
	}
	cout << ans << "\n";
}


int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
