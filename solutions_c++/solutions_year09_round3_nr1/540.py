#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

void print_r(vector<int> vi)
{
	for (int i = 0; i < vi.size(); i++)
		cout<< "[" << vi[i] << "]";
}

int main()
{
	freopen("A.in","rt",stdin);
	freopen("A.out","wt",stdout);
	int t, ti;
	cin >> t;
	for (ti = 1; ti <= t; ti++)
	{
		string s;
		cin >> s;
		
		vector<int> p; p.clear(); p.resize(s.size());
		
		int c[256], base = 0;
		for (int i = 0; i < 256; i++) c[i] = 0;//memset(c,0,sizeof(c));
		for (int i = 0; i < s.length(); i++) c[s[i]] = 1;
		
		
		for (int i = 0; i < 256; i++) base += c[i];
		if (base == 1) base = 2;
		int px = 0;
		vector <int> prior;
		prior.clear();
		prior.push_back(1);
		prior.push_back(0);

		for (int i = 2; i < base; i++) prior.push_back(i);

		for (int i = 0; i < s.length(); i++)
			if (c[s[i]] == 1)
			{
				c[s[i]] = 0;
				for (int j = 0; j < s.length(); j++)
					if (s[j] == s[i])
						p[j] = prior[px];
				px++;
			}
		__int64 ans = 0;
		vector<__int64> al; al.clear(); al.resize(p.size());
		al[0] = 1;
		reverse(p.begin(),p.end());
		for (int i = 1; i < p.size(); i++) al[i] = al[i - 1] * __int64(base); 
		for (int i = 0; i < p.size(); i++)
							ans += __int64(p[i]) * al[i];
		//cout << s << " "; reverse(p.begin(),p.end()); print_r(p); cout << " " << base << " = " << ans << endl;
		cout << "Case #" << ti <<": " << ans <<endl;
	}

	fclose(stdin); fclose(stdout);
	return 0;
}