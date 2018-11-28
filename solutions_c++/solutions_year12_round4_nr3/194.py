#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>

using namespace std;


int n;
vector <int> a, x;

/*
bool gen(int l, int r) 
{
	x[l] = 0;
	int i = l;
	while(i < r) {
		if (a[i] > r) return false;
		if (!gen(i+1, a[i])) return false;
		long double mx = 0.0;
		for (int j = i+1; j < a[i]; j++) {
			mx = max(mx, (long double)(x[j]-x[i])/(j-i));
		}
		mx = 1;
		if (mx > 1) cerr << "botva\n";
		long double h = (a[i]-i)*mx+x[i];
		if (h-1e-9 > 1000000000) return false;
		x[a[i]] = (int) (h-1e-9) + 1;
		i = a[i];
	}
	return true;
}
*/


vector<int> fst;
vector<int> nxt;
vector<int> val;


void AddEdge(int a, int b) 
{
//	cerr << a << ' ' << b << "\n";
	nxt.push_back(fst[a]);
	fst[a] = (signed)nxt.size() - 1;
	val.push_back(b);
}


int was[3000];
int ord[3000];
int time;


void Dfs(int u) {
	was[u] = 1;
	for (int j = fst[u]; j != -1; j = nxt[j])  {
	    int v = val[j];
		if (was[v] == 0)
			Dfs(v);
	}
	time++;
	ord[u] = time;
}


void Dfs2(int u) {
	int i;
	i = a[u];
	if (was[i] != 2) {
		was[i] = 2;
		x[i] = (i - u) * ord[u] + x[u];
		Dfs2(i);
	}
	for (i = 0; i < u; i++) {
		if (a[i] == u && was[i] != 2) {
			was[i] = 2;
			x[i] = (i - u) * ord[i] + x[u];
			Dfs2(i);
	    }
	}
}


void Solve()
{
	cin >> n;
	a.resize(n);
	x.resize(n);
	int i, j;
    for (i = 0; i < n-1; i++) {
    	was[i] = 0;
		cin >> a[i];
        a[i]--;
    }
    was[n-1] = 0;
    nxt.clear();
    val.clear();
    fst.clear(); fst.resize(n, -1);
    for (i = 0; i < n-1; i++) {
    	if (a[i] < n-1)
    		AddEdge(i, a[i]);
    	for (j = i+1; j < a[i]; j++) {
    		if (a[j] == a[i])
    			AddEdge(j, i);
    		if (a[j] > a[i] || a[j] <= j) {
    			cout << "Impossible\n";
    			return;
    		}
    	}
    }

    time = 0;
    for (i = 0; i < n; i++) {
    	if (was[i] == 0) {
    		Dfs(i);
    	}
    }

    /*cerr << "ord: " ;
    for (i = 0; i < n-1; i++) {
    	cerr << ord[i] << " ";
    }
    cerr << "\n";
    */
    x[0] = 0;
    was[0] = 2;
    Dfs2(0);

	bool bad = false;
	for (i = 0; i < n-1; i++) {
		for (j = i+1; j < a[i]; j++) {
			if (((long long)x[j]-x[i]) * (a[i]-i) > ((long long)x[a[i]]-x[i])*(j-i))
				bad = true;
		}
		for (j = a[i]+1; j < n; j++) {
			if (((long long)x[j]-x[i]) * (a[i]-i) > ((long long)x[a[i]]-x[i])*(j-i))
				bad = true;
		}
	}
	if (bad) cerr << "botva2\n";
	int mn= 0;
	for (i = 0; i < n; i++) 
		if (mn > x[i]) mn = x[i];

	for (i = 0; i < n; i++)
		cout << x[i]-mn << " ";
	cout << "\n";

}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Solve(); 
	}
	return 0;
}
