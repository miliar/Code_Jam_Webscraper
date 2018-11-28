#include<iostream>
using namespace std;

int findGCD(int a, int b)
{
	if(a < b)
	{
		int temp = a;
		a = b;
		b = temp;
	}
	
	if(a == b)
		return a;
		
	if(b == 0)
		return a;
	
	int times = a / b;
	return findGCD(a - b * times, b);
}

int main()
{
	int cases;
	cin >> cases;
	
	for(int i = 1; i <= cases; i++)
	{
		long long N = 0;
		int PD = 0;
		int PG = 0;
		
		cin >> N >> PD >> PG;
		if(((PD < 100) && (PG == 100)) || ((PD > 0) && (PG == 0)))
		{
			cout << "Case #" << i << ": Broken" << endl;
			continue;
		}
		int GCD = findGCD(PD, 100);
		//cout << GCD << endl;
		int times = 100 / GCD;
		if(N >= times)
			cout << "Case #" << i << ": Possible" << endl;
		else
			cout << "Case #" << i << ": Broken" << endl;
	}
	
	
	return 0;
}