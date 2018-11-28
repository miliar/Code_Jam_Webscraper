#include <iostream>
#include <math.h>
#include <windows.h>
#include <vector>
#include<valarray>
#include<algorithm>
#include <iomanip>
#include<map>


using namespace std;
typedef vector<int> vali;
typedef valarray<int> valli;
typedef long long vlong;

//Mathwise, this is equivalent to fibo with f(x) = 6f(x-1) - 4f(x-2)
//starting with 2 and 6
//and subtracting one from the result

//high order implementation

//t(0) = 0
//t(1) = 1
//t(2n-1) = t(n)^2 - 4*t(n-1)^2
//t(2n) = 6*t(n)^2 - 8*t(n)*t(n-1)

//Use a similar formula to combine fibo and t
map<int, vlong> fibod;
map<int, vlong> td;

vlong t(int n)
{
	if(n == 0) return 0;
	if(n == 1) return 1;
	if(td[n] != 0) return td[n];

	vlong result;
	if(n%2 == 1)
	{
		int m = (n+1)/2;
		result = t(m)*t(m) - 4*t(m-1)*t(m-1);
	}
	else
	{
		int m = n/2;
		result = 6*t(m)*t(m) - 8*t(m)*t(m-1);
	}
	result %= 1000;
	td[n] = result;
	return result;
}

vlong fibo(int n)
{
	if(n == 0) return 2;
	if(n == 1) return 6;
	if(fibod[n] != 0) return fibod[n];

	vlong result;
	if(n%2 == 1)
	{
		int m = (n+1)/2;
		result = t(m)*fibo(m) - 4*t(m-1)*fibo(m-1);
	}
	else
	{
		int m = n/2;
		result = t(m)*( 6*fibo(m)-4*fibo(m-1) ) - 4*t(m-1)*fibo(m);
	}
	result %= 1000;
	fibod[n] = result;
	return result;
}

int main()
{
	cout << setfill('0');

	int cases;
	cin >> cases;

	for(int i = 0; i < cases; i++)
	{
		int num;
		cin >> num;

end:
		cout<< "Case #" << i + 1 <<": ";
		cout <<setw( 3 ) << (fibo(num) - 1 + 2000) % 1000;
		cout << "\n";
	}
	//std::cout << "Hello World!";
	return 1;
}
