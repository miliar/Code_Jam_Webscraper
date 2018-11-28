#include<iostream>
#include<string>
#include<vector>
using namespace std;

#define MAX_WORD_LEN 15
#define ALPH 26

int main ()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large-out.txt", "w", stdout);
	int l, d, n;
	cin >> l >> d >> n;
	vector <string> word(d);
	for (int i = 0; i < d; i++)
		cin >> word[i];
	vector <string> test(n);
	for (int i = 0; i < n; i++)
		cin >> test[i];
	for (int i = 0; i < n; i++)
	{
		bool arr[MAX_WORD_LEN][ALPH];
		memset(arr, 0, sizeof(arr));
		bool val = false;
		int index = 0;
		for (int j = 0; j < test[i].size(); j++)
		{
			if (test[i][j]=='(') val = true;
			else if (test[i][j] == ')') { val = false; index++; }
			else if (val) arr[index][test[i][j]-'a'] = true;
			else { arr[index][test[i][j]-'a'] = true; index++; }
		}
		int answer = 0;
		for (int j = 0; j < d; j++)
		{
			int k;
			for (k = 0; k < l; k++)
				if (!arr[k][word[j][k]-'a'])
					break;
			if (k == l) answer++;
		}
		cout << "Case #" << i+1 << ": " << answer << endl;
	}
	return 0;
}
