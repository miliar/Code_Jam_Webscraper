#include <iostream>
#include <cstdlib>
#include <climits>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int runs(string& s)
{
	char c = '\0';
	int r = 0;
	for (int i=0; i<s.length(); ++i)
	{
		if (c != s[i])
		{
			++r;
			c = s[i];
		}
	}
	return r;
}

int main() 
{
	
	int C;
	
	cin >> C;
	for (int cas=1; cas<=C;++cas)
	{
		
		int k;
		string S;
		
		cin >> k >> S;
		
		vector<int> perm;
		for (int i=0; i<k; ++i)
		{
			perm.push_back(i);
		}
		
		int m=S.length();
		do	{
			string t(S);
			
			for (int i=0; i < S.length() / k; ++i)
			{
				for (int j=0; j<k; ++j)
				{
					t[i*k+j] = S[i*k+perm[j]];
				}
			}
			
			m = min(m, runs(t));
			
		} while (next_permutation(perm.begin(),perm.end()));
		
		cout << "Case #" << cas << ": " << m << endl;
		
	}
	return 0;
}