#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;
int main()
{
	char sourse[31][101],a[]="abcbdefghijklmnopqrstuvwxyz";
	char dst[31][101],b[]="yhesocvxduiglbkrztnwjpfmaq";
	int t,i,j,k,flag;
	freopen("A-small-attempt3.in","r",stdin);
	freopen("A.out","w",stdout);
	cin>>t;
	getchar();
	for(i=1;i<=t;i++)
	{
		gets(sourse[i]);
		for(j=0;j<strlen(sourse[i]);j++)
		{
			for(k=0,flag=0;k<26;k++)
				if(sourse[i][j]==k+'a') 
				{
					dst[i][j]=b[k];
					flag=1;
					break;
				}
			if(flag==0) dst[i][j]=sourse[i][j];
		}
		dst[i][j]='\0';
		cout<<"Case #"<<i<<":"<<" "<<dst[i]<<endl;
	}
	return 0;
}
