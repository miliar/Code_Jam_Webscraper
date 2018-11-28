#include <iostream>
#include<cmath>
#include<set>
#include<vector>
#include<map>
#include<algorithm>
#include<string>

using namespace std;

int main()
{
	if(freopen("C:\\SANDBOX\\chocolates\\Debug\\input.txt", "r", stdin)&&freopen("C:\\SANDBOX\\chocolates\\Debug\\output.txt", "w", stdout))
	{
		//cout<<"Sucess!!";
	}
	else
	{
		cout<<"Fail!!";
		return 0;
	}

int num, inp;

vector<int> val;

int i, tmp, sum, min, xrsum;
int cs = 1;

cin>>num;
while(num--)
{
	cin>>inp;
	val.clear();
	for( i = 0; i < inp; i++)
	{
		cin>>tmp;
		val.push_back(tmp);
	}

	sum = 0; min = val[0]; xrsum = 0;
	for( i = 0; i < inp; i++)
	{
		sum += val[i];
		if(val[i] < min)
		{
			min = val[i];
		}
		xrsum ^= val[i];
	}
	
	if(xrsum == 0)
		cout<<"Case #"<<cs<<": "<<(sum-min)<<endl;
	else
		cout<<"Case #"<<cs<<": NO"<<endl;
	cs++;
}
}