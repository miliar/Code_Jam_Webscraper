#include <iostream>
#include <string>

using namespace std;

int main()
{
	string sample_in = "aoz ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv",
		sample_out = "yeq our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

	static char m[127];
	for (int i = 0; i < sample_in.size(); i++)
		m[sample_in[i]] = sample_out[i];


	m['q'] = 'z';

	int n;
	cin >> n;
	string s; getline(cin, s);
	for (int i = 1; i <= n; i++)
	{
		getline(cin, s);
		cout << "Case #" << i << ": ";
		for (int j = 0; j < s.size(); j++)
		{
			if (m[s[j]] == 0)
				cerr << "fail" << s[j] << endl;
			cout << m[s[j]];
		}
		cout << endl;
	}
}
