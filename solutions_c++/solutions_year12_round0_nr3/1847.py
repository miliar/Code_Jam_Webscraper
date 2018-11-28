#include <map>
#include <string>
#include <iostream>
#include <cmath>
#include <sstream>
#include <set>

using namespace std;

set<pair<int, int> > iset;

int rotate(int i)
{
    ostringstream oss;
    oss << i;
    string istr = oss.str();
    
    for (int n = 1; n < istr.size(); n++)
    {
        string rotated = istr.substr(istr.size() - n, n) + istr.substr(0, istr.size() - n);
        if (rotated[0] == '0' || rotated == istr)
            continue;
        istringstream iss(rotated);
        int irotated;
        iss >> irotated;
        
        pair<int, int> p(i < irotated ? i : irotated, i < irotated ? irotated : i);
        iset.insert(p);
    }
}
    
int main()
{
	int n;
	cin >> n;

	for (int i = 1; i <= 2000000; i++)
	{
	    rotate(i);
//	    if (i % 1000 == 0)
//	        cerr << i << endl;
	}
	    
	for (int i = 0; i < n; i++)
	{
	    int a, b, count = 0;
	    cin >> a >> b;
	    
	    for (set<pair<int, int> >::iterator iter = iset.begin(); iter != iset.end(); iter++)
	        if (iter->second >= a && iter->second <= b && iter->first >= a && iter->first <= b)
	            count++;
	            
	    cout << "Case #" << i + 1 << ": " << count << endl;
	}
}
