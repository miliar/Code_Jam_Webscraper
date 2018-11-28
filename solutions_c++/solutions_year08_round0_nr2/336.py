#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n; cin >> n;
    for (int x = 1; x <= n; ++x)
    {
	// depart=true, arrive=false
	std::vector<pair<int, pair<bool, int> > > v;
	int t;
	cin >> t;
	int n[2];
	cin >> n[0] >> n[1];
	for (int i = 0; i < 2; ++i)
	    while (n[i]--)
	    {
		int dh, dm, ah, am;
		char z;
		cin >> dh >> z >> dm >> ah >> z >> am;
		v.push_back(make_pair(dh*60 + dm, make_pair(true, i)));
		v.push_back(make_pair(ah*60 + am + t, make_pair(false, 1 - i)));
	    }
	sort(v.begin(), v.end());
	int a[2] = { 0, 0 }, r[2] = { 0, 0 };
	for (typeof(v.begin()) p = v.begin(); p != v.end(); ++p)
	{
	    int i = p->second.second;
	    if (p->second.first)
	    {
		if (r[i] == 0) a[i]++; else r[i]--;
	    }
	    else
		r[i]++;
	}
	cout << "Case #" << x << ": " << a[0] << " " << a[1] << endl;
    }
    return 0;
}
