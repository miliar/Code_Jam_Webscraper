#include<iostream>
#include<cstring>
using namespace std;
char arr[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
void fun(int cas,char *str,int n)
{
	int j=0,pos;
	cout<<"Case #"<<cas<<": ";
	for(j=0;j<n;j++)
	{
		if(str[j]!=' ')
		{
			if(str[j]>='a'&&str[j]<='z')
				{
					pos = str[j] -97;
				}
			else if(str[j]>='A'&&str[j]<='Z')
				{
					pos = str[j]-65;
				}
			str[j]=arr[pos];
		}	
		cout<<str[j];
	}
	cout<<"\n";
	
}

int main()
{
	char str[101];
	int n,i,len,j;
	cin>>n;
	cin.ignore();
//	cin.getline(str,100);
	for(i=0;i<n;i++)
	{
		cin.getline(str,101);
		//cin.ignore();
		len=strlen(str);
		fun(i+1,str,len);		
	}
		
}
