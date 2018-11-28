// problem 1 

#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;
typedef long long int ll;

vector <ll> numbers;
vector <ll> store;

void process()
{
	vector <ll> :: iterator it;
	int test;
	cin >> test;
	int N, P , K , L;
	ll no;
	ll ret;
	
	for(int k=1; k <= test; k++)
	{
		numbers.clear();
		store.clear();
		
		cin >> P >> K >> L;
		for(int n = 0; n < K; n++)
		numbers.push_back(0);
		for(int l = 0; l < L; l++)
		{
			cin >> no;
			numbers.push_back(no);
		}
		int value = -1;
		
		sort(numbers.begin(), numbers.end());
		reverse(numbers.begin(), numbers.end());
		
		for(int kk = 1; kk <= L/K + 1; kk++)
		{
		 	for(int m = 1; m <= K; m++)
		 	{
		 		value += 1;
		 		
		 		store.push_back(numbers[value] * kk);
		 	}
		 }
		ll ret = 0;
		//for(it = store.begin(); it != store.end(); it++)
		//cout << *it;
		for(it = store.begin(); it != store.end(); it++)
			ret += *it;
		cout << "Case #" << k << ": " << ret << endl;
		
	}
	
	return ;
}
int main()
{
		process();
		return 0;
}

