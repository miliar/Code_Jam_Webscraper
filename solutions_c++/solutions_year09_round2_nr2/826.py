#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;
bool fun(int a,int b)
{
	if(a>b)
		return true;
	else return false;
}
int main()
{
int t,c=0;
cin>>t;
while(c++<t)
	{
		
		string num;
		cin>>num;
		string myNum="0";
		myNum+=num;
		char arr[myNum.size()];
		for(int i=0;i<myNum.size();i++)
		{
		arr[i]=myNum[i];
		}
		next_permutation(arr,arr+myNum.size());
		
		int start=(arr[0] == '0')?1:0;
		cout<<"Case #"<<c<<": ";
		for(int i=start;i<myNum.size();i++)
		{
			cout<<arr[i];
		}
		cout<<"\n";
	}
}
