#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    for(int z = 0; z < n; z++)
    {
	int k; string s2;
	cin >> k >> s2;
	vector<int> ints;
	for(int i = 0; i < k; i++) ints.push_back(i);


	int retVal = s2.size();
	do
	{
	  string s = s2;
	    for(int i = 0; i < s.size()/k; i++)
	    {
		string cur;
		for(int j = 0; j < k; j++)
		    cur += s[i*k + ints[j]];

		for(int j = 0; j < k; j++)
		    s[i*k + j] = cur[j];
	    }

	    char c = s[0]; int cnt = 0; s += "A";
	    for(int i = 0; i < s.size(); i++)
		if(c != s[i]) { cnt++; c = s[i]; }

	    retVal = min(retVal, cnt);
	} while(next_permutation(ints.begin(), ints.end()));

	cout << "Case #" << z + 1 << ": " << retVal << endl; 
    }
}
