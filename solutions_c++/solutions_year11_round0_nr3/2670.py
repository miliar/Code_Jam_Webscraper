#include<iostream>
using namespace std;

int main()
{
int xorsum=0;
int sean_val;
long int total;
int testcases,candiesnum;

	cin>>testcases;
	int i=1;
	while(i<=testcases)
	{
		xorsum=0;
		total=0;
		sean_val = 1000000;
		cin>>candiesnum;
		int candy_val[candiesnum];
		for(int j=0;j<candiesnum;j++)
		{
			cin>>candy_val[j];
			xorsum = xorsum^candy_val[j];
			if(candy_val[j]<sean_val)
			sean_val=candy_val[j];
			total += candy_val[j];
		}
	
	if(!xorsum)
	cout<<"Case #"<<i<<": "<<total-sean_val<<"\n";
	else
	cout<<"Case #"<<i<<": "<<"NO\n";
	i++;
	
	}
}

