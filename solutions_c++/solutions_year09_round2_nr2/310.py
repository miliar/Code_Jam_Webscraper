#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <cstdio>

using namespace std;

int main()
{
	int t,T;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		string str;
		cin>>str;
		int orig[10]={0};
		int i;
		for( i=str.size()-1;i>=0;--i)
		{
			int cur=str[i]-'0';
			orig[cur]++;
			int j=cur+1;
			while((j<10)&&(orig[j]==0))
				j++;
			if(j<10)
			{
				cout<<"Case #"<<t<<": ";
				for(int l=0;l<i;l++)cout<<str[l];
				cout<<j;
				orig[j]--;
				for(j=0;j<10;j++)
					for(int k=0;k<orig[j];k++)cout<<j;
				cout<<endl;
				break;
			}
		}
		if(i<0)
		{
			int j=1;
			while((j<10)&&(orig[j]==0))
				j++;
			orig[j]--;
			cout<<"Case #"<<t<<": ";
			cout<<j;
			cout<<0;
			for(j=0;j<10;j++)
				for(int k=0;k<orig[j];k++)cout<<j;
			cout<<endl;
		}
	}
	return 0;
}