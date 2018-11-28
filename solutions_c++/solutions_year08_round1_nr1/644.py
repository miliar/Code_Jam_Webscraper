//minimum scalar product

#include <iostream>
#include <vector>
#include <algorithm>
typedef long long int ll;
using namespace std;


vector<ll> v1;
vector<ll> v2;

void read()
{
	int number;
	cin >> number;
	//cout << number << endl;
	//cout << "hello" ;
	v1.clear();
	
	for(int k=0; k < number; k++)
	{
		ll elements, elements1;
		cin >> elements;
		v1.push_back(elements);

		//v2.push_back(elements1);
	}
	v2.clear();
	for(int k=0; k < number; k++)
	{
		ll elements, elements1;
		cin >> elements;
		v2.push_back(elements);

		//v2.push_back(elements1);
	}
	
	
	return ;
}
ll sum;
void prod()
{
		
	return ;
}

void print()
{
	vector <ll> :: iterator it;
	for( it = v1.begin(); it != v1.end(); it++)
	cout << *it << endl;
	
	vector <ll> :: iterator t;
	for( t = v2.begin(); t != v2.end(); t++)
	cout << *t << endl;
	
	return ;
}
void process()
{
	int test;
	ll Y;
	cin >> test;
	cout << test << endl;
	for(int k=1; k <= test; k++)
	{
		//read();
		//print();
		int n;
		cout << n << endl;
		//Y = prod();
		cout << " hello " << endl;
		
	}
	
	return ;
}
int main()
{
	//process();
	int test;
	cin >> test;
	for(int k=1; k <=test; k++)
	{
		//cout << test;
		//cout << "hello " <<endl;
		read();
		//print();
		//prod();
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		reverse(v2.begin(), v2.end());
		sum = 0;
		//for(int kk=0; kk < v1.size(); kk++)
		//{
			for(int jj=0; jj < v2.size(); jj++)
			{
			sum = sum + v1[jj] * v2[jj];
			}
		//}
		cout << "Case #" << k << ": " << sum << endl;
	}
		
	return 0;
}

