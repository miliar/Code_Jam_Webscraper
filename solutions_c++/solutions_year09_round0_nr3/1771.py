#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	string str="zwelcome to code jam";
	char input[10000];
	int no;
	scanf("%d",&no);
	char c;
	scanf("%c",&c);
	for(int my=1;my<=no;my++)
	{
		gets(input);
		if( strlen(input) < 19 )
		{
			cout<<"Case #"<<my<<": ";
			cout<<"0000\n";
			continue;
		}
			
		int arr[100];
		for(int i=1;i<=19;i++)
			arr[i]=0;
		
		arr[0]=1;
		for(int i=0;i<strlen(input);i++)
		{
			char temp=input[i];
			for(int j=1;j<=19;j++)
			{
				if( temp==str[j] )
				{
					arr[j]=(arr[j]+arr[j-1])%1000000;
				}
			}
		}
		int ans=arr[19]%10000;
		cout<<"Case #"<<my<<": ";
		if(ans/10 == 0)
			cout<<"000"<<ans<<endl;
		else if( ans/100 == 0)
			cout<<"00"<<ans<<endl;
		else if( ans/1000 == 0)
			cout<<"0"<<ans<<endl;
		else
			cout<<ans<<endl;
	}
	return 0;
}
