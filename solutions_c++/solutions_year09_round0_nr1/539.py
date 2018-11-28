#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

typedef vector <int> vi;

int len;
int nlis;
string lis[5000];
char buf[10000];
int tc, ntc;

vi parse(string s)
{
	int i, j;
	vi res;
	for (i=0; i<s.length(); i++)
	{
		if (s[i] == '(')
		{
			int m = 0;
			for (j=i+1; s[j] != ')'; j++)
				m |= 1<<(s[j]-'a');
			res.push_back( m );
			i = j;
		}
		else
		{
			res.push_back( 1<<(s[i]-'a') );
		}
	}
	return res;
}

bool ok(const vi& v, const string& s)
{
	int i;
	for (i=0; i<s.length(); i++)
	{
		if (v[i] & (1<<(s[i]-'a'))) continue;
		return false;
	}
	return true;
}

int calc(string s)
{
	int res = 0;
	vi vmask = parse( s );
	int i;
	for (i=0; i<nlis; i++) if (ok(vmask, lis[i])) res++;
	return res;
}

int main()
{
	FILE* fi = fopen("A-large.in", "r");
	FILE* fo = fopen("A-large.out", "w");

	fscanf(fi, "%d %d %d", &len, &nlis, &ntc);
	int i;
	for (i=0; i<nlis; i++)
	{
		fscanf(fi, "%s", buf);
		lis[i] = buf;
	}

	for (tc=1; tc<=ntc; tc++)
	{
		fscanf(fi, "%s", buf);
		int res = calc(buf);
		
		printf("Case #%d: %d\n", tc, res);
		fprintf(fo, "Case #%d: %d\n", tc, res);
	}

	fclose(fi); fclose(fo);
}