#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int getsize(const string &str, const vector<int> &vperm)
{
	int block = vperm.size();
	string newstr = str;
	for(int i=0; i < str.size(); i+=block)
		for(int j=i; j < i+block; j++)
			newstr[j] = str[i+vperm[j-i]];
	char prev = newstr[0];
	int complen = 1;
	for(int i=1; i < newstr.size(); i++)	
	{
		if (newstr[i] == prev) continue;
		complen++; prev = newstr[i];
	}
	return complen;
}
int main()
{
	int ncase; cin >> ncase;
	for(int icase=0; icase < ncase; icase++)
	{
		cout << "Case #" << icase+1 << ": ";
		int k;
		string str;
		cin >> k >> str;
//cout << k << " " << str << endl;
		vector<int> vperm;
		for(int i=0; i < k; i++)
			vperm.push_back(i);


		int minsize = 50000;
		do
		{
			int curr = getsize(str, vperm);
			minsize = min(curr, minsize);
//			for(int i=0; i < vperm.size(); i++)
//				cout << vperm[i] << " ";
//			cout << endl;
		}while(next_permutation(vperm.begin(), vperm.end()));
		cout << minsize << endl;
	}
}

