#include<iostream>
#include<string>
#include<cstring>
using namespace std;

int digit[10];

string make(int val)
{
	string ret = "";
	int k;
	for (k = val+1; k < 10; k++)
		if (digit[k])
		{
			ret.append(1, k+'0');
			digit[k]--;
			break;
		}
	if (k == 10) return ret;
	for (int i = 0; i < 10; i++)
		while (digit[i])
		{
			digit[i]--;
			ret.append(1, i+'0');
		}
	return ret;
}

int main ()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large-out.txt", "w", stdout);
	int test_cases;
	cin >> test_cases;
	string str;
	string ans;
	for (int numb = 0; numb < test_cases; numb++)
	{
		cin >> str;
		memset(digit, 0, sizeof(digit));
		int i;
		for (i = str.size()-1; i >= 0; i--)
		{
			digit[str[i]-'0']++;
			ans = make(str[i]-'0');
			if (ans != "")
			{
				ans = str.substr(0, i) + ans;
				break;
			}
		}
		if (i < 0)
		{
			ans = make(0);
			if (ans.size()>1)
				ans = ans.substr(0, 1) + "0" + ans.substr(1, ans.size()-1);
			else ans += "0";
		}
		cout << "Case #" << numb+1 << ": " << ans << endl;
	}
	return 0;
}
