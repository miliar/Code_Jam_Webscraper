#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;

long long nums[1000];
long long gcd(long long a, long long b)
{
	if(a == 0)
		return b;
	return gcd(b%a,a);
}
int main()
{
	ifstream cin("B-small.in");
	ofstream cout("B-small.out");
	int C;
	cin >> C;
	for(int i = 1; i <= C; i++)
	{
		
		int N;
		cin >> N;
		for(int x = 0; x < N; x++)
			cin >> nums[x];
		sort(nums,nums+N);
		
		int gc = 0;
		for(int i = 1; i < N; i++)
			gc = gcd(gc,nums[i]-nums[i-1]);

		int y = 0;
		
		int m = 1;
		while(m*gc < nums[0])
			m++;
		y = m*gc - nums[0];
		
		cout << "Case #" << i << ": " << y << endl;
	}
}