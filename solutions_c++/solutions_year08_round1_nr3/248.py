#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;
int  f[61];
int ans[31];
int main()
{
	int T, n;
	ifstream cin("3.txt");
	ofstream cout("output.txt");
	f[0] = 0;
	f[1] = 1;
	for(int i = 2; i < 61; i++)
		f[i] = (f[i-1] + f[i-2]) % 1000;
	for(int i = 2, k = 4; i < 31; i++, k = (2 * k) % 1000)
	{
		ans[i] = (k * 2 * f[2 * i - 1] + k * f[2 * i] - 1) % 1000;
		//cout<<ans[i]<<endl;
	}
	cin>>T;
	for(int Case = 1; Case <= T; Case++)
	{
		cin>>n;		
		cout<<"Case #"<<Case<<": ";
		if(ans[n] < 100)
			cout<<0;
		cout<<ans[n]<<"\n";
	}
}