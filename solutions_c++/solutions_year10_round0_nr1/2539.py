
#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
template<class T>
ostream& operator<<(ostream& out, const vector<T>& nums)
{
	out<<"[";
	for(vector<T>::const_iterator i=nums.begin(); i!=nums.end(); i++)
		out<<(*i)<<ends;
	out<<"]";
	return out;
}

int pow2(int n)
{
	int p=1;
	for (int i=0; i<n; i++)
	{
		p*=2;
	}
	return p;
}
string cj(int n, int k)
{
	if ((k+1)%pow2(n)==0)
		return "ON";
	else
		return "OFF";
}

int main()
{
	int T;
	cin>>T;
	int N, K;
	int count=1;
	for (; count<=T; count++)
	{
		cin>>N>>K;
		cout<<"Case #"<<(count)<<": "<<cj(N, K)<<endl;
	}
	return 0;
}

