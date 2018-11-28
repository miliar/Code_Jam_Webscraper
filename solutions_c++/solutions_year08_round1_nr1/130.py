#include <iostream>
#include <math.h>
#include <windows.h>
#include <vector>
#include<valarray>
#include<algorithm>

using namespace std;
typedef vector<int> vali;
typedef valarray<int> valli;
typedef long long vlong;

int main()
{
	int cases;
	cin >> cases;

	for(int i = 0; i < cases; i++)
	{
		int places;
		cin >> places;
		vali a(places);
		vali b(places);
		int j = 0;
		for(j = 0; j < places; j++)
		{
			cin >> a[j];
		}
		for(j = 0; j < places; j++)
		{
			cin >> b[j];
		}
		sort(a.begin(), a.end() );
		sort(b.rbegin(), b.rend() );

		vlong answer = 0;
	for(j = 0; j < places; j++)
	{
		answer += a[j]*b[j];
	}
end:
		cout<< "Case #" << i + 1 <<": ";
		cout << answer;
		cout << "\n";
	}
	//std::cout << "Hello World!";
	return 1;
}
