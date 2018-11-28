#include<ctime>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
typedef istringstream iss; typedef ostringstream oss; typedef long long lli;
const double TOLL=1e-9;


int main()
{
    int t; cin>>t; int cn=0;
    while(t--)
    {
	map<string,char> com; set<string> des;
	int c; cin>>c; char x,y,z;
	for(int i=0;i<c;i++)
	{
	    cin>>x>>y>>z;
	    string temp="";
	    temp=temp+x; temp+=y;
	    com[temp]=z;

	    temp="";
	    temp+=y; temp=temp+x; 
	    com[temp]=z;
	}
	int d; cin>>d;
	for(int i=0;i<d;i++)
	{
	    cin>>x>>y;
	    string temp="";
	    temp+=x; temp+=y;
	    des.insert(temp);
	    temp="";
	    temp+=y; temp+=x;
	    des.insert(temp);
	}
	int n; cin>>n;
	string input; cin>>input;
	string rv="[";
	for(int i=0;i<n;i++)
	{
	    string now=""; now+=rv[sz(rv)-1]; now+=input[i];
	    if(com.count(now))
	    {
		char cand=com[now];
		rv[sz(rv)-1]=cand;
	    }
	    else
	    {
		bool ok=true;
		for(int j=0;j<sz(rv);j++) 
		{
		    string temp=""; temp+=rv[j]; temp+=input[i];
		    if(des.count(temp)) ok=false;
		}
		if(!ok) rv="[";
		else rv+=input[i];
	    }
	}
	rv+="]";
	for(int i=0;i<sz(rv)-1;i++) if(isalpha(rv[i]) && rv[i+1]!=']')
	{
	    rv.insert(rv.begin()+i+1,',');
	    rv.insert(rv.begin()+i+2,' ');
	}
	printf("Case #%d: ",++cn);
	cout<<rv<<endl;
    }

}
