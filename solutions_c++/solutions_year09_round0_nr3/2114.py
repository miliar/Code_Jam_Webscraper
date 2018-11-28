#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
	int kases;
	scanf("%d ",&kases);
	string S="welcome to code jam";
	for(int k=1;k<=kases;k++)
	{
		cout<<"Case #"<<k<<": ";
		char t[510];
		gets(t);
		string temp(t),str="";
		for(int i=0;i<temp.size();i++)
		{
			for(int j=0;j<S.size();j++)
				if(temp[i]==S[j])
				{
					str+=temp[i];
					break;
				}
		}
		if(str.size()<19)
		{
			cout<<"0000"<<endl;
			continue;
		}
		int arr[19][str.size()];
		for(int i=0;i<19;i++)
			for(int j=0;j<str.size();j++)
				arr[i][j]=0;
		for(int j=0;j<str.size();j++)
		{
			if(str[j]=='w')
			{
				if(j==0)
					arr[0][0]=1;
				else
					arr[0][j]=arr[0][j-1]+1;
			}
			else
				arr[0][j]=j==0?0:arr[0][j-1];
		}
		for(int i=1;i<=18;i++)
		{
			char ch=S[i];
			for(int j=0;j<str.size();j++)
			{
				if(str[j]==ch && arr[i-1][j]!=0)
				{
					arr[i][j]=arr[i-1][j]+arr[i][j-1];
					if(arr[i][j]>10000)
						arr[i][j]=(arr[i][j])%10000;
				}
				else
				{
					arr[i][j]=j==0?0:arr[i][j-1];
				}
			}
		}
		int ans=arr[18][str.size()-1];
		string answer="";
		while(ans)
		{
			answer+=(ans%10+'0');
			ans/=10;
		}
		reverse(answer.begin(),answer.end());
		for(int f=0;f<4-answer.size();f++)
			cout<<0;
		cout<<answer<<endl;
	}
}


		

