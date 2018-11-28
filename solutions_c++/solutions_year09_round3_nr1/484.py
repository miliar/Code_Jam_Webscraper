#include <fstream>
#include <string>
#include <math.h>

using namespace std;

ifstream fin ("input.txt");
ofstream fout("output.txt");

long long x = 1;
string s;
int n;

const int MAX = 36;

long long mx = 0;
long long ans = 0;

bool w[MAX];
bool t[70];

int main()
{
	fin >> n;
	for (int jj = 0; jj < n; ++jj)
	{
		ans = 0;
		x = 1;
		mx = 0;
		fin >> s;

		memset(w, false, sizeof(w));
		memset(t, false, sizeof(t));
		
		char c = s[0]; s[0] = '1'; w[1] = true; int pos = 0; t[0] = true;
		for (int i = 1; i < s.size(); ++i)
			if (s[i] == c)
			{
				t[i] = true;
				s[i] = '1';
			}
		for (int i = 1; i < s.size(); ++i)
		{
			if (t[i]) continue;
			c = s[i]; t[i] = true; 
			if (pos > 10) s[i] = 'a'+pos-10;
				else s[i] = '0'+pos;
			for (int j = i+1; j < s.size(); ++j)
				if (s[j] == c && !t[j])
				{
					if (pos > 10) s[j] = 'a'+pos-10;
						else s[j] = '0'+pos;
					t[j] = true;
				}
			w[pos] = true;
			++pos; while (w[pos]) ++pos;
		}

		for (int i = 0; i < (int)s.size(); ++i)
			mx = max(mx, (long long)(min(abs(s[i]-'0'), abs(s[i]-'a'+10))));

		++mx;

		for (int i = (int)s.size()-1; i >= 0; --i)
		{
			ans += (long long)(min(abs(s[i]-'0'), abs(s[i]-'a'+10)))*x;
			x *= mx;
		}

		fout << "Case #" << jj+1 << ": " << ans << endl;
	}

	return 0;
}