/*from the given input, spaces between names of search engine were replaced by '_', manually.
Ex 'Dont Ask' was replaced by 'Dont_Ask'. */

/* Gcc compiler is used*/
#include<string>
#include<algorithm>
#include<iostream>
#include<limits>
using namespace std;
char searc[100][100],query[1000][100];
int pos[100];
int s,q;

int func(int n)
{
	int i,j,k=-1,l=INT_MAX;
	for(j=0;j<s;j++)
	{
	l=INT_MAX;
	for(i=n;i<q;i++)
	{
		if(strcmp(searc[j],query[i])==0)
		{l=i;
		break;}
	}
	k=max(k,l);
	}
return k;
}	

main()
{
int cnt,n;
int no,j,k;
cin>>no;
for(j=0;j<no;j++)
{
cnt=0;
 cin>>s;
 for(k=0;k<s;k++)
  {cin>>(searc[k]);}
  cin>>q;
 for(k=0;k<q;k++)
cin>>(query[k]);
n=func(0);

while(n!=INT_MAX)
{
cnt++;
n=func(n);
}
cout<<"Case #"<<j+1<<": "<<cnt<<endl;
}
}
