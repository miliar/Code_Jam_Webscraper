#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;

int main()
{
	int t;
	cin>>t;
	int count =0;
	int arr[25],duparr[25];
	char str[25];
	char *num;
	while(count<t)
	{
		cin>>str;
		char *p, *beg;
		p = &str[0];
		beg = &str[0];
		int length = 0;
		arr[0] =0;
		length++;
		for(int i=0;*p!='\0';i++)
		{
			arr[i+1] = *p - 48;
			duparr[i] = *p - 48;
			p++;
			length++;
		}
		
		next_permutation(arr,arr+length);
		
		
		cout<<"Case #"<<count+1<<": ";
			
			if(arr[0]!=0)
			cout<<arr[0];	
		
			for(int i=1;i<length;i++)
			{
				cout<<arr[i];
			}
				cout<<"\n";
		count++;
	}


}