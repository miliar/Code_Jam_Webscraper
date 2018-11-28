#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int i, j, k, L, D, N;
	vector<string> words;
	cin >> L >> D >> N;
	for(i=0; i<D; i++)
	{
		string word;
		cin >> word;
		words.push_back(word);
	}
	for(i=0; i<N; i++)
	{
		string language;
		cin >> language;
		int pos=0, start=0;
		vector< vector<bool> > exist(30, vector<bool>(16, false));
		for(j=0; j<(int)language.size(); j++)
		{
			if(language[j] == '(')
				start=1, pos++;
			else if(language[j] == ')')
				start=0;
			else
			{
				if(start == 0) pos++;
				exist[language[j]-'a'][pos]=true;
//				cout << language[j] << " " << pos << endl;
			}
		}

		int ans = 0;
		bool flag = false;
		for(j=0; j<D; j++)
		{
			flag = false;
			for(k=0; k<(int)words[j].size(); k++)
			{
				if(!exist[words[j][k] - 'a'][k+1])
				{
					flag = true;
					break;
				}
			}
			if(!flag) ans++;
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}
