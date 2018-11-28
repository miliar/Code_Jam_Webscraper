#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;

int main()
{
	char str[102];
	int n,i,j=0;
	int arr[26]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};
	cin>>n;
	cin.get();
	while(j++<n)
	{
		cin.getline(str,102);
		for(i=0;i<strlen(str);i++)
		{
			if(str[i]!=' ')
			{
				str[i]='a'+arr[str[i]-97];
			}
		}
		cout<<"Case #"<<j<<": "<<str;
		if(j<n)
			cout<<"\n";
	}
	return 0;
}