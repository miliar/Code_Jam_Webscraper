#include<iostream>
#include<string>
using namespace std;
string words[5000];
string pattern;
bool map[15][26];
int L, D, N;
int main()
{
	cin >> L >> D >> N;
	for(int i=0; i<D; ++i)
		cin >> words[i];
	for(int k=1; k<=N; ++k)
	{
		cin >> pattern;
		int p=0;
		for(int i=0; i<L; ++i) {
			for(int j=0; j<26; ++j)
			    map[i][j] = false;
			if(pattern[p] == '(')
				for(++p; pattern[p]!=')'; ++p)
				    map[i][pattern[p]-'a'] = true;
			else
				map[i][pattern[p]-'a'] = true;
			++p;
		}
		p=0;
		for(int i=0; i<D; ++i)
		{
			bool flag = true;
			for(int j=0; j<L; ++j)
				if(!map[j][words[i][j]-'a'])
				{
					flag = false;
					break;
				}
			if(flag)
			    ++p;
		}
		cout << "Case #" << k << ": " << p << endl;
	}
	return 0;
}
