#include <iostream>
using std::cout;
using std::cin;
#include <algorithm>
using std::sort;
using namespace std;

int arr[2000010],temp[2000010],c,d,num,cases,a,b;
long long y,counter;
int main()
{
	for(int i=0;i<=11;i++)
	{
		arr[i]=i;
	}
	c=2;
	d=10;
	for(int i=12;i<=2000000;i++)
	{
		if(i==100){c=3;d=100;}
		if(i==1000){c=4;d=1000;}
		if(i==10000){c=5;d=10000;}
		if(i==100000){c=6;d=100000;}
		if(i==1000000){c=7;d=1000000;}
		num=i;
		arr[i]=11000000;
		for(int j=1;j<=c;j++)
		{
			num=((num%10)*d)+(num/10);
			if(num<arr[i] && num>=d)
			{
				arr[i]=num;
			}
		}
	}
	cin>>cases;
	for(int kase=1;kase<=cases;kase++)
	{
		cin>>a>>b;
		for(int i=a;i<=b;i++)
		{
			temp[i]=arr[i];
		}
		sort(temp+a,temp+b+1);
		counter=1;
		y=0;
		for(int i=a+1;i<=b;i++)
		{
			if(temp[i]==temp[i-1])
			{
				counter++;
				//continue;
			}
			else
			{
				y+=(counter*(counter-1))/2;
				counter=1;
			}
		}
		y+=(counter*(counter-1))/2;
		cout<<"Case #"<<kase<<": "<<y<<"\n";
	}
	return 0;
}