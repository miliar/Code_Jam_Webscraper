#include<iostream>
using namespace std;
int main()
{
	int t,templen;
	cin>>t;
	for(int ttt=1;ttt<=t;ttt++)
	{
		cout<<"Case #"<<ttt<<": ";
		int len,n;
		char C[26][26];
		char O[26][26];
		for(int i=0;i<26;i++)
			for(int j=0;j<26;j++)
			{	
C[i][j]=0;

				O[i][j]=0;
			}

		cin>>n;
		char temp[3];
		for(int i=0;i<n;i++)
		{
			cin>>temp;
			C[temp[0]-'A'][temp[1]-'A']=temp[2];
			C[temp[1]-'A'][temp[0]-'A']=temp[2];
		}
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>temp;
			O[temp[0]-'A'][temp[1]-'A']=1;
			O[temp[1]-'A'][temp[0]-'A']=1;
		}

		cin>>len;
//cout<<len;		
char arr[150];
		cin>>arr;
		templen=0;
		for(int i=0;i<len;i++)
		{
			if(i>0 && C[arr[i]-'A'][arr[i-1]-'A']!=0)
			{
				arr[i-1]=C[arr[i]-'A'][arr[i-1]-'A'];
				for(int j=i+1;j<len;j++)
					arr[j-1]=arr[j];
				len--;
				i--;
			}
			else
			{
				int pos=-1;
				for(int j=i-1;j>=0;j--)
				{
					if(O[arr[i]-'A'][arr[j]-'A']==1)
					{
						pos=j;
					break;
					}
				}
				if(pos!=-1)
				{
					pos=0;
					for(int j=i+1;j<len;j++)
					{
						arr[pos++]=arr[j];
					}
					i=-1;
					len=pos;
				}}}
//cout<<endl<<len<<endl;				
cout<<"[";
				for(int i=0;i<len-1;i++)
					cout<<arr[i]<<", ";
				if(len-1>=0)
					cout<<arr[len-1];
				cout<<"]\n";
}
}
