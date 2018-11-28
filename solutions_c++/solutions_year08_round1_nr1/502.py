#include <iostream>
#include <vector>
using namespace std; 

int cmp(int a, int b)
{
	return a > b;    
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out.txt", "w", stdout);
    int t, n, kase;
    vector<int> x, y;
    cin >> kase;
    for(t = 1; t <= kase; t++)
    {
		cin >> n;
		
		int i, j;
		x.clear();
		y.clear();
		for(i = 0; i < n; i ++)
		{
			cin >> j;
			x.push_back(j); 	
		}
		for(i = 0; i < n; i ++)
		{
			cin >> j;
			y.push_back(j); 	
		}
		sort(x.begin(), x.end());
		sort(y.begin(), y.end(), cmp);
		int res = 0;
		for(i = 0; i < n; i ++)
			res += x[i] * y[i];
			
		cout << "Case #" << t << ": "<< res << endl;
	}
    
    return 0;    
}
