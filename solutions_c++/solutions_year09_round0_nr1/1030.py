#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stdio.h>

using namespace std;

#define CLEAR(x,with) memset(x,with,sizeof(x))  
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define sz(a) int((a).size())

typedef pair<int,int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

int main()
{
	bool contains[20][30];
	int L, D, N;
	vector<string> list_of_words;

	cin >> L >> D >> N;
	for(int i=0; i<D; i++)
	{
		string word;
		cin >> word;
		list_of_words.push_back(word);
	}
	for(int i=1; i<=N; i++)
	{
		for(int j=0; j<20; j++) for(int k=0; k<30; k++) contains[j][k] = false;
		string pattern;
		cin >> pattern;
		int position = -1;
		bool parenthesis_open = false;
		for(int j=0; j<(int)pattern.size(); j++)
		{
			if( pattern[j] == '(')
			{
				parenthesis_open = true;
				position++;
			}
			else if(pattern[j] == ')')
			{
				parenthesis_open = false;
			}
			else
			{
				if( parenthesis_open == false ) position++;
				contains[ position ][ pattern[j] - 'a' ] = true;
			}
		}

		int ans = 0;
		for(int j=0; j<D; j++)
		{
			for(int k=0; k<(int)list_of_words[j].size(); k++)
			{
				if(!contains[k][list_of_words[j][k] - 'a'])
					goto endend;
			}
			ans++;
endend:;
		}
		cout << "Case #" << i << ": " << ans << endl;
	}

	return 0;
}
