#include <iostream>

using namespace std;

int main()
{
	string google = "ynficwlbkuomxsevzpdrjgthaq";
	string english = "abcdefghijklmnopqrstuvwxyz";
	int n;
	cin >> n;
	string tmp;
	getline(cin,tmp);
	for(int i = 0; i < n; i++)
	{
		string word;
		string ans;
		getline(cin, word);
		for(int j = 0; j < word.length(); j++)
		{
			if(word[j] != ' ')
			{
				unsigned int loc = google.find_first_of(word[j]);
				ans.append(1,english[loc]);
			}
			else
			{
				ans.append(" ");
			}
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
}