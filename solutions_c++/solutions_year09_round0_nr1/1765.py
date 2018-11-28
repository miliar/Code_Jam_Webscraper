#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int l,d,n;
	cin >> l >> d >> n;
	vector <string> arr;
	arr.resize(d);
	for (int i =0 ;i < d; i ++)
		 cin >> arr[i];
	for (int test = 1; test <= n; test ++)
	{
		vector <string> word(l);
		
		char c;
		for (int i = 0; i < l ; i ++)
		{
			cin >> c;
			if (c == '(')
			{
				cin >> c;
				while (c != ')')
				{
					word[i] += c;
					cin >> c;
				}
			}
			else
				word[i] = c;
		}
		int ans = 0;
		for (int i = 0; i < d; i ++)
		{
			bool ok = true;
			for (int j = 0; j < l; j ++)
			{
				int tmp = word[j].find(arr[i][j]) ;
				if (!(tmp >= 0 && tmp < word[j].length()))
				{
					ok = false;
					break;
				}
			}

			if (ok)
				ans ++;
		}
		cout << "Case #"<<test<<": "<<ans<<endl;
	}
	return 0;
}