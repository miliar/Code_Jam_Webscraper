#include <iostream>
#include <vector>
#include <string.h>
using namespace std;
int test;
int v[50][50];
int d[50][50];
void go()
{
	cout << "Case #" << ++test << ": ";
	memset(v, 0, sizeof(v));
	memset(d, 0, sizeof(d));
	int n;
	cin >> n;
	while (n--)
	{
		string sir; cin >> sir;
		v[sir[0]-'A'][sir[1]-'A'] = sir[2];
		v[sir[1]-'A'][sir[0]-'A'] = sir[2];
	}
	cin >> n;
	while (n--)
	{
		string sir; cin >> sir;
		d[sir[0]-'A'][sir[1]-'A'] = 1;
		d[sir[1]-'A'][sir[0]-'A'] = 1;
	}
	vector<int> vv;
	cin >> n;
	string x; cin >> x;
	for (int i = 0; i < x.size(); ++i)
	{
		if (x[i] != 'Q' && x[i] != 'W' && x[i] != 'E'
				&&
		x[i] != 'R' && x[i] != 'A' && x[i] != 'S'
			&&
		x[i] != 'D' && x[i] != 'F' && x[i] != 'F') continue;
		if (vv.size() == 0) {vv.push_back(x[i]); continue;}
		int lst = vv[vv.size() - 1] - 'A';
		if (v[lst][x[i]-'A'])
		{
			vv[vv.size() - 1] = v[lst][x[i]-'A'];
			continue;
		}
		int ok = 0;
		for (int j = 0; j < vv.size(); ++j)
		if (d[vv[j] - 'A'][x[i]-'A'])
		{
			vv.clear();
			ok = 1;
			break;
		}
		if (ok == 0)
		vv.push_back(x[i]);
	
	}
	cout << '[';
	for (int i = 0; i < vv.size(); ++i)
	{
		if (i) cout << ", ";
		cout << (char)vv[i];
	}
	cout << "]\n";
}

int main()
{
	int t; cin >> t;
	while (t--) go();
	return 0;
}
