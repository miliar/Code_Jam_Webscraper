#include<vector>
#include<iostream>

using namespace std;

int main()
{
	long n,k;
	int noOfCases=0;
	cin>>noOfCases;
	int cnt=noOfCases;
	long num=1;
	long arr[]={0,1,3,7,15,31,63,127,255,511,1023,2047,4095,8191,16383,32767,65535,131071,262143,524287,1048575,2097151,4194303,8388607,16777215,33554431,67108863,134217727,268435455,536870911,1073741823};
	
	while(noOfCases-->0)
	{
		int flag=0;
		cin>>n>>k;
		long ans=arr[n]&k;
		if(ans==arr[n])
			flag=1;
		cout<<"Case #"<<(cnt-noOfCases)<<": ";
		if(flag==1)
			cout<<"ON"<<endl;
		else
			cout<<"OFF"<<endl;
	}
	return 0;
}
