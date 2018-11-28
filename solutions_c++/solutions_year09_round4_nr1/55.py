#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <assert.h>
using namespace std;

typedef long long LL;
typedef vector <string> vs;
typedef vector <int> vi;
typedef vector <LL> vll;
typedef vector <double> vd;
typedef pair <int,int> pii;


vs token(string s, string d)
{
	string t;
	vs res;
	int pos;
	while (true)
	{
		pos = s.find(d);
		if (pos == -1) break;
		t = s.substr(0, pos);
		s = s.substr(pos+d.length());
		if (t != "") res.push_back( t );
	}
	if (s != "") res.push_back( s );
	return res;
}

vs token(string s)
{
	return token(s, " ");
}

vi s2vi(string s, string d)
{
	vs tvs = token(s, d);
	vi res;
	int i;
	for (i=0; i<tvs.size(); i++) res.push_back( atoi(tvs[i].c_str()) );
	return res;
}

vi s2vi(string s)
{
	return s2vi(s, " ");
}

////////////////////////////////////////////

int tc, ntc;
int n;
char mat[50][50];
int ar[50];

int main()
{
	FILE* fi = fopen("A-large.in", "r");
	FILE* fo = fopen("A-large.out", "w");

	fscanf(fi, "%d", &ntc);
	int i, j;
	for (tc = 1; tc <= ntc; tc++)
	{
		fscanf(fi, "%d", &n);
		for (i=0; i<n; i++) fscanf(fi, "%s", mat[i]);
		for (i=0; i<n; i++)
		{
			for (j=n-1; j>=0; j--) if (mat[i][j] == '1') break;
			ar[i] = j;
		}

		int res = 0;
		for (i=0; i<n; i++)
		{
			if (ar[i] <= i) continue;
			for (j=i+1; j<n; j++) if (ar[j] <= i) break;

			for (; j>i; j--)
			{
				res++;
				swap(ar[j], ar[j-1]);
			}
		}

		printf("Case #%d: %d\n", tc, res);
		fprintf(fo, "Case #%d: %d\n", tc, res);
	}


	fclose(fi); fclose(fo);
}