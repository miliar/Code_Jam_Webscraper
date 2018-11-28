#include<iostream>
#include<map>
#include<string>
using namespace std;
main()
{
int t,n,q,flag[201],count,ans,c=1;
string str;
map < string,int > kadli;
cin>>t;
while(t--)
{
	cin>>n;
	int i;
	kadli.clear();
	for(i=0;i<=n;i++)
	{
	getline(cin,str,'\n');
 	if(i!=0)
	kadli.insert(pair<string,int> (str,i)); 
	}
	memset(&flag,0,sizeof(flag));
	cin>>q;
	count=0;ans=0;
	for(i=0;i<=q;i++)
	{
   	getline(cin,str,'\n');
   	if(i==0)
   	continue;
	int num=kadli.find(str)->second;
	if(flag[num]==0)
	{
	flag[num]=1;
count++;
}
if(count==n)
{
 ans++;
memset(&flag,0,sizeof(flag));
flag[num]=1;
count=1;
}
}

cout<<"Case #"<<c<<": "<<ans<<endl;
c++ ;
}



}
