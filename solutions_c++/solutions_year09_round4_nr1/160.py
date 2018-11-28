#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <cassert>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for(int z = 1; z <= T; z++)
    {
	int N;
	cin >> N;
	vector<int> cur;

	int ret = 0;
	for(int i = 0; i < N; i++)
	{
	    string s;
	    cin >> s; int maxi = -1;
	    
	    for(int k = 0; k < s.size(); k++) 
		if(s[k] == '1') 
		    maxi = k;
	    
	    cur.push_back(maxi);
	}	    

	for(int i = 0; i < N; i++)
	    if(cur[i] > i)
	    {
		int j;
		for(j = i + 1; j < N; j++)
		    if(cur[j] <= i)
		    {
			for(int k = j; k >= i + 1; k--)
			{
			    swap(cur[k], cur[k - 1]);
			    ret++;
			}
			
			break;
		    }
		assert(j != N);
	    }

	cout << "Case #" << z << ": " << ret << endl;
    }
}
