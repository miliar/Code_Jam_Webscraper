#include <iostream>
#include <vector>
#include <cctype>
using namespace std;
void split(string pattern,vector<string>& V)
{
	int i=0;
	while (i<pattern.length())
	{
		if (isalpha(pattern[i]))
			V.push_back(string("")+pattern[i++]);
		else //(
		{
			string s="";
			i++;
			while (pattern[i]!=')')
				s+=pattern[i++];
			V.push_back(s);
			i++;
		}
	}
}
int main()
{
	int L,D,N,i,j,k;
	string words[5000];
	string pattern;
	cin >> L >> D >> N;
	for (i=0; i<D; i++)
		cin >> words[i];
	for (j=1; j<=N; j++)
	{
		vector<string> V;
		cin >> pattern;
		split(pattern,V);
		int cnt=0;
		for (i=0; i<D; i++)
		{
			bool ok=true;
			for (k=0; k<L; k++)
				if (V[k].find(words[i][k])==-1)
				{
					ok=false;
					break;
				}
			if (ok) cnt++;
		}
		cout << "Case #" << j << ": " << cnt << endl;
	}
	return 0;
}