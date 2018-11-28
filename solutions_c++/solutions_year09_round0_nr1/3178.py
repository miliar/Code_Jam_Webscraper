#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;

int main()
{
	int l,d,n;
	int i,j,k;
	vector<string> dict;
	int count;
	
	string dword, word;
	cin >> l >> d >> n;
	vector<set<int> > lsets(l);
	set<int>::iterator it;
	set<char>::iterator itc;
	
	while (d--)
	{
		cin >> dword;
		dict.push_back(dword);
	}
	for (i=1; i<=n ;++i)
	{
		lsets.clear();
		//lsets.resize(l);
		count = 0;
		
		cin >> word;
		vector<set<char> > letters(l);

		bool startb = false, endb = false;
		int curl = 0;
		for (j=0; j<word.size(); ++j)
		{
			if (word[j] == '(') {
				startb = true;
			}			
			else if (startb && word[j] != ')') 
			{
				letters[curl].insert(word[j]);
			}			
			else if (word[j] == ')') 
			{
				startb = false;
				++curl;
			}
			else if (word[j] != '(')
			{
				letters[curl++].insert(word[j]);
			}
		}

		for (j=0; j<l; ++j)
		{
			lsets[j].clear();
			for (k=0; k<dict.size(); ++k)
			{
				
				if (letters[j].find(dict[k][j]) != letters[j].end())
				{
					lsets[j].insert(k);
				}
			}			
		}
		
		set<int> curset = lsets[0];
		set<int> intset;
		
		for (j=0; j<l-1; ++j)
		{
			for (it=curset.begin(); it!=curset.end();++it)
				if (lsets[j+1].find(*it) != lsets[j+1].end())
					intset.insert(*it);
			curset = intset;
			intset.clear();
		}
		
		cout << "Case #" << i << ": "<< curset.size() << endl;
		
	}
}