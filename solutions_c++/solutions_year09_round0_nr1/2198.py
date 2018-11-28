#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool Ketemu(string s, vector< vector<char> > VC)
{
	int Pjg = s.length(), i;
	
	for (i=0; i<Pjg; i++)
	{
		if (find(VC[i].begin(), VC[i].end(), s[i]) == VC[i].end())
			return false;
	}
	return true;
}

int main()
{
	int L, D, N, i, j;
	vector<string> Word;
	string s;
	
	cin >> L >> D >> N;
	
	for (i=0; i<D; i++)
	{
		cin >> s;
		Word.push_back(s);
	}
	sort(Word.begin(), Word.end());
	
	for (i=0; i<N; i++)
	{
		string s;
		cin >> s;
		int Ans = 0;
		
		int Pjg = s.length();
		vector< vector<char> > Name;
		
		for (j=0; j<Pjg; j++)
		{
			vector<char> Temp;
			if (s[j]=='(')
			{
				j++;
				while(s[j]!=')')
				{
					Temp.push_back(s[j]);
					j++;
				}
				sort(Temp.begin(), Temp.end());
				Name.push_back(Temp);
			}
			else
			{
				Temp.push_back(s[j]);
				sort(Temp.begin(), Temp.end());
				Name.push_back(Temp);
			}
			Temp.clear();
		}
				
		for (j=0; j<D; j++)
		{
			if (Ketemu(Word[j], Name))
				Ans++;
		}
		
		
		cout << "Case #" << i+1 << ": " << Ans << "\n";
	}
	
	return 0;
}
