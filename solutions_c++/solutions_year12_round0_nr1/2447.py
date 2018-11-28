#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
int main() 
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
    int T,i,len;

	scanf("%d\n", &T);
	for(i=1; i<=T; i++)
	{
		char str[102],res[102];


		gets(str);
		len = strlen(str);
		int j=0;
		while(len--)
		{
			if(str[j]=='a') 
				res[j]='y';
				
			else if(str[j]=='b') 
				res[j]='h';
			
			else if(str[j]=='c') 
				res[j]='e';
				
			else if(str[j]=='d') 
				res[j]='s';
				
			else if(str[j]=='e') 
				res[j]='o';
				
			else if(str[j]=='f') 
				res[j]='c';
				
			else if(str[j]=='g')
				res[j]='v';
				
			else if(str[j]=='h') 
				res[j]='x';
				
			else if(str[j]=='i') 
				res[j]='d';
				
			else if(str[j]=='j') 
				res[j]='u';
				
			else if(str[j]=='k') 
				res[j]='i';
				
			else if(str[j]=='l') 
			{
				res[j]='g';
				
			}
			else if(str[j]=='m') 
			{
				res[j]='l';
				
			}
			else if(str[j]=='n') 
			{
				res[j]='b';
				
			}
			else if(str[j]=='o') 
			{
				res[j]='k';
				
			}
			else if(str[j]=='p') 
			{
				res[j]='r';
				
			}
			else if(str[j]=='q') 
			{
				res[j]='z';
				
			}
			else if(str[j]=='r') 
			{
				res[j]='t';
				
			}
			else if(str[j]=='s') 
			{
				res[j]='n';
				
			}
			else if(str[j]=='t') 
			{
				res[j]='w';
				
			}
			else if(str[j]=='u') 
			{
				res[j]='j';
				
			}
			else if(str[j]=='v') 
			{
				res[j]='p';
				
			}
			else if(str[j]=='w') 
			{
				res[j]='f';
				
			}
			else if(str[j]=='x') 
			{
				res[j]='m';
				
			}
			else if(str[j]=='y') 
			{
				res[j]='a';
				
			}
			else if(str[j]=='z') 
			{
				res[j]='q';
				
			}
			else res[j]=str[j];
			//cout<<str[j]<<" "<<res[j];
			j++;

		}
		res[j]='\0';
		string s = res;
		printf("Case #%d: %s\n",i,res);
		//cout<<"Case #"<<i<<": "<<s<<endl;
	}
	//char c;
	//cin>>c;
    return 0;
}