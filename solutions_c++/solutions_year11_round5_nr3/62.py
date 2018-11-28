#include <iostream>
#include <fstream>
#include <vector>
#include <string>


using namespace std;


vector <int> edg[100011];

int r, c;

void Load()
{
	cin >> r >> c;
	string s;
	getline(cin, s);
	int i, j;
	for (i = 0; i < r*c; i++) edg[i].clear();
	for (i = 0; i < r; i++) {
		
		getline(cin, s);
	//	cerr << s << "\n";
		for (j = 0; j < c; j++) 
		{
			int v[2];
			switch(s[j]) {
				case '-': 
					v[0] = (i*c+(j+1)%c);
					v[1] = (i*c+(j+c-1)%c);
				break;
				case '|': 
					v[0] = ((i+1)%r*c+j);
					v[1] = ((i+r-1)%r*c+j);
				break;
				case '\\': 
					v[0] = ((i+1)%r*c+(j+1)%c);
					v[1] = ((i+r-1)%r*c+(j+c-1)%c);
				break;
				case '/': 
					v[0] = ((i+r-1)%r*c+(j+1)%c);
					v[1] = ((i+1)%r*c+(j+c-1)%c);
				break;
			}
			edg[v[0]].push_back(v[1]);
			edg[v[1]].push_back(v[0]);
			//cerr << "\n" << v[1] << ' '<< v[0] << "\n";
		}
	}

}

int tt;


int was[100001];

int ne, nv;

void Dfs(int v) {
	was[v] = tt;
	nv++;
	for (int i = 0; i < (int)edg[v].size(); i++) {
		ne++;
		int j = edg[v][i];
		if (was[j] != tt)
			Dfs(j);
	}
}

void Solve()
{
	int ans = 1;
	int i;
	for (i = 0; i < r*c; i++) {	
		if (was[i] != tt) {
			ne = nv = 0;
			Dfs(i);
			ne /= 2;
			if (ne != nv) ans = 0;
			ans = (ans*2) % 1000003;
		}
	}
	cout << ans << "\n";
}

int main()
{
	int nt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
