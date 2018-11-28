#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int n;
	cin >> n;
	for(int _case=1; _case<=n; ++_case)
	{
		int s, q, p=0, res=0;
		vector<string> eng; eng.clear();
		string buf;
		bool fl[200]; memset(fl, false, sizeof(fl));
		cin >> s; getline(cin, buf);
		for(int i=0; i<s; i++, eng.push_back(buf))
			getline(cin, buf);
		cin >> q; getline(cin, buf);
		for(int i=0; i<q; ++i)
		{
			getline(cin, buf);
			int t=find(eng.begin(), eng.end(), string(buf))-eng.begin();
			if (fl[t]) continue;
			if (p==s-1)
			{
				memset(fl, false, sizeof(fl));
				fl[t]=true;
				p=1; res++;
			}
			else fl[t]=true, p++;
		}
		cout << "Case #" << _case << ": " << res << endl;
	}
	return 0;
}