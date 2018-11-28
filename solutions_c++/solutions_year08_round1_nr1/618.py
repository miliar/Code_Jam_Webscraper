#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int tc;
    cin >> tc;
    for(int z = 0; z < tc; z++)
    {
	int num, t;
	cin >> num;
	vector<int> va, vb;

	for(int i = 0; i < num; i++)
	{
	    cin >> t;
	    va.push_back(t);
	}

	for(int i = 0; i < num; i++)
	{
	    cin >> t;
	    vb.push_back(t);
	}

	sort(va.begin(), va.end());
	sort(vb.begin(), vb.end());
	reverse(vb.begin(), vb.end());

	long long retVal =0;
	for(int i = 0; i < va.size(); i++)
	    retVal += va[i] * vb[i];

	cout << "Case #" << z + 1 << ": " << retVal << endl;
    }
}
