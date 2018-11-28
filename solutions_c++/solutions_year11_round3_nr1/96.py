#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;

const int nmax = 55;
string a[nmax];
int n,m;

bool solve()
{
	for (int i = 0;i < n; ++i)
		for (int j = 0;j < m; ++j)
			if (a[i][j] == '#')
			{
				a[i][j] = '/';
				if (i+1 < n && a[i+1][j] == '#') a[i+1][j] = '\\';
				else return false;

				if (j+1 < m && a[i][j+1] == '#') a[i][j+1] = '\\';
				else return false;

				if (a[i+1][j+1] == '#') a[i+1][j+1] = '/';
				else return false;
			}
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int nn;
	cin >> nn;
	for (int test = 1;test <= nn; ++test){

		
		cin >> n >> m;

		for (int i = 0;i < n; ++i) cin >> a[i];	
		
		printf("Case #%i:\n",test);		

		if (!solve()) printf("Impossible\n");
		else
		{
			for (int i = 0;i < n; ++i) cout << a[i] << endl;
		}
	}
	
	return 0;
}