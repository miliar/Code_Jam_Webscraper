#include <iostream>
#include <string>
using std::cout;
using std::cin;
using std::endl;
int lowbit(int x)
{
	return (x ^ (x+1)) >> 1;
}
std::string work(int n, int k)
{
	if(lowbit(k) >= (1 << (n-1))) return "ON";
	else return "OFF";
}
int main()
{
	int t;
	cin >> t;
	for(int i=1; i<=t; i++)
	{
		int n, k;
		cin >> n >> k;
		cout << "Case #" <<  i << ": " << work(n, k) << endl;
	}
	return 0;
}
