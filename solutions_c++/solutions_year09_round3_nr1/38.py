#include <iostream>
#include <map>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int NN = 1; NN <= T; NN++)
	{
		map<char, int> ss;
		int cnt = 0;
		char str[100];
		cin >> str;
		int len  = strlen(str);
		ss[str[0]] = 1;
		for(int i = 1; i < len; i++)
		{
			if(ss.find(str[i]) == ss.end())
			{
				ss[str[i]] = cnt++;
				if(cnt == 1)
					cnt++;
			}
		}
		long long ret = 0;
		long long base = ss.size();
		if(base == 1)
		{
			base++;
		}
		for(int i = 0; i < len; i++)
		{
			ret = ret * base + ss[str[i]];
		}
		cout << "Case #" << NN << ": " << ret << endl;

	}
	return 0;

}
