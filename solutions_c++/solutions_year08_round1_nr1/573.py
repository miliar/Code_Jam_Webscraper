#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <memory>
#include  <map>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cmath>
using namespace std;

#define cin in
#define cout out
ifstream in("A-large.in");
ofstream out("A_large.out");

int t;
int n;
int a[1000];
int b[1000];

int main()
{
	cin >> t;
	for(int i = 0;i < t;i ++)
	{
		cin >> n;
		for(int j = 0;j < n;j ++)
			cin >> a[j];
		for(int j = 0;j < n;j ++)
			cin >> b[j];
		sort(a,a + n);
		sort(b,b + n);

		long long  sum = 0;
		for(int j = 0 ;j < n;j ++)
		{
			sum += ((long long)a[n - 1 - j]) * b[j];
		}
		cout << "Case #"<<i + 1<<": ";
		cout << sum << endl;
	}



	return 0;
}