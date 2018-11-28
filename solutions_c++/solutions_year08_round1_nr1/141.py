#include <iostream>
#include <queue>

using namespace std;

int main()
{
	int cases;
	cin >> cases;
	
	for (int cNum = 1; cNum <= cases; cNum++)
	{
		int dim;
		cin >> dim;
		
		priority_queue<int> v1;
		priority_queue<int, vector<int>, greater<int> > v2;
		
		for (int i = 0; i < dim; i++)
		{
			int t;
			cin >> t;
			v1.push(t);
		}
			
		for (int i = 0; i < dim; i++)
		{
			int t;
			cin >> t;
			v2.push(t);
		}
			
			
		/* while (!v1.empty())
		{
			int f = v1.top();
			v1.pop();
			cout << "V1: " << f << endl;
		}
		while (!v2.empty())
		{
			int f = v2.top();
			v2.pop();
			cout << "V2: " << f << endl;
		} */
		
		long long product = 0;
		while (!v1.empty())
		{
			int i1, i2;
			i1 = v1.top(); v1.pop();
			i2 = v2.top(); v2.pop();
			
			long long prod = i1 * i2;
			product += prod;
		}
		
		cout << "Case #" << cNum << ": " << product << endl;
	}
	
	return 0;
}