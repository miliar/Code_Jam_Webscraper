#include<iostream>
#include<cstring>
#include<map>
#include<sstream>
#include<cstdio>
#include<cstdlib>
using namespace std;
map<pair<string,string>,int > ans;
void recycled(string one,int a,int b)
{
	for(int i=1;i<one.size();i++)
	{
	       string fhalf,shalf;
	       fhalf=one.substr(0,i);
	       shalf=one.substr(i,one.size()-i);
	       string::iterator iter=shalf.begin();
	       while((*iter)=='0')
	       {
		       shalf.erase(iter);
		       iter=shalf.begin();
	       }
	       string newstr=shalf+fhalf;
	       int no1=atoi(newstr.c_str());
	       if(no1>=a&&no1<=b)
	         {
			 pair<string,string> tmp,revpair;
			 tmp.first=one;
			 tmp.second=newstr;
			 revpair.first=newstr;
			 revpair.second=one;
			 if(ans.count(revpair)<=0&&newstr.compare(one)!=0)
			 {ans[tmp]=1;}
			 
		 }

	}
}
int main()
{
	int n=1;
	cin>>n;
	for(int caseno=1;caseno<=n;caseno++)
	{
		int a,b;
		cin>>a>>b;
		ans.clear();
		for(int i=a;i<=b;i++)
                 {
	            stringstream temp;
		    temp<<i;
		    string inp=temp.str();
                    recycled(inp,a,b);
		 }
		cout<<"Case #"<<caseno<<": "<<ans.size()<<endl;
	}
}
