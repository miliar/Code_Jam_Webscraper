#include <cstdio>
#include <string>
#include <vector>
#include<map>
#include <iostream>

using namespace std;

int main()
{
int t;
scanf("%d",&t);

for(int count=0;count<t;count++)
{
int N,M;
scanf("%d %d",&N, &M);


map<string,bool> mp;
	for(int i=0;i<N;i++)
	{
	string temp;
	cin>>temp;
	mp[temp]=true;
	}

int mkdir=0;
mp[""]=true;
for(int i=0;i<M;i++)
{
string temp;
cin>>temp;
if(temp=="/") continue;
int dir=0;
for(int i=temp.length();i>=0;i--)
{

if(i==temp.length())
{
if(mp.find(temp)!=mp.end()) break;
else
mp[temp]=true;
}
else if(temp[i]=='/')
{
dir++;
if( mp.find(temp.substr(0,i))!=mp.end() )
{mkdir+=dir; break; }
else
mp[temp.substr(0,i)]=true;
}
	
}
}

printf("Case #%d: %d\n",count+1,mkdir);

}

return 0;
}
