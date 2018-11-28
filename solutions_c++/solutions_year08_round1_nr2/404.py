#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int tc;
    cin >> tc;
    for(int z = 0; z < tc; z++)
    {
	int fl, cust;
	cin >> fl >> cust;
        vector<vector<int> > customers(cust, vector<int>(fl, -1));

	for(int i = 0; i < cust; i++)
	{
	    int T;
	    cin >> T;
	    for(int j = 0; j < T; j++)
	    {
		int x, y;
		cin >> x >> y;
		customers[i][x - 1] = y;
	    }
	}

	int retVal = 999999999, corresp = 0;
	for(int i = 0; i < (1<<fl); i++)
	{
	    bool br = false;
	    for(int j = 0; j < cust; j++)
	    {
		bool sat = false;
		for(int k = 0; k < fl; k++)
		{
		    if((customers[j][k] == 0 && ((i & (1<<k)) == 0))
		       || (customers[j][k] == 1 && (i & (1<<k)))) { sat = true; break; }
		}

		if(!sat) { br = true; break; }
	    }

	    if(!br && retVal > __builtin_popcount(i))
	    {
		retVal = __builtin_popcount(i);
		corresp = i;
	    }
	}

	string ret;
	if(retVal == 999999999) ret = "IMPOSSIBLE";
	else
	{
	    for(int i = 0; i < fl; i++)
	    {
		if(i > 0) ret += " ";

		if(corresp & (1<<i)) ret += "1";
		else ret += "0";
	    }
	}

	cout << "Case #" << z + 1 << ": " << ret << endl;
    }
}
