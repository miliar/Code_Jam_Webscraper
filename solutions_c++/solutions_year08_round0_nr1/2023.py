#include <iostream>
#include <map>
#include <string>
using namespace std;
int main(){
	map<string,int> Map;
	int t,o=1,s,q,swit=0,sco;
	string str;
	cin>>t;
while(t--)
{
cin>>s;
sco=0;
getline(cin,str);
for(int i=0;i<s;i++)
{getline(cin,str);Map[str]=0;}
cin>>q;
getline(cin,str);
while(q--)
{
getline(cin,str);
if(!Map[str]) 
{Map[str]=1;sco++;}
if(sco==s) {
	swit++;
	sco=1;
	map<string,int>::iterator it = Map.begin();
		for(;it!=Map.end();it++)
			it->second=0;
	Map[str]=1;
			}
}
cout<<"Case #"<<o++<<": "<<swit<<endl;
swit=0;
Map.clear();
}
return 0;
}