#include <iostream>
#include <vector>
#include <cstdlib>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <set>
#include <string>
#define mp make_pair
#define pii pair(int,int)
#define all(v) v.begin(),v.end()
#define ll long long
//#define abs((x),()y)) ((x)>(y)?(x)-(y):(y)-(x))
using namespace std;

string func(int number)
{
    if (number == 0)
        return "0";
    string temp="";
    string returnvalue="";
    while (number>0)
    {
        temp+=number%10+48;
        number/=10;
    }
    for (int i=0;i<temp.length();i++)
        returnvalue+=temp[temp.length()-i-1];
    return returnvalue;
}

string res(string s,int k)
{string temp="";
 int i,len=s.size();
 for(i=k;i<len;i++) temp+=s[i];
 s=temp+s;
 //string ans="";
 //for(i=0;i<len;i++)
 //ans+=s[i];
 //return ans;
 s.erase(len,s.size()-len);
 return s;
}

bool comp(string s,string t)
{sort(all(s));
 sort(all(t));
 return(s==t);
}

bool  are(int n,int m)
{int i;
 for(i=0;i<n;i++)
 if((res(func(n),i))==func(m))
 return true;
 return false;
}

int main()
{int n,m,t;
 freopen("C-small-attempt3.in","rt",stdin);
 freopen("Out.txt","wt",stdout);
 cin >> t;cin.get();
 for(int tc=1;tc<=t;tc++)
{cin >> n >> m;cin.get();
 int i,k,j,ans=0;
 for(i=n;i<m;i++)
 for(j=i+1;j<=m;j++)
 if(comp(func(i),func(j)))
 ans+=are(i,j);
 cout << "Case #" << tc << ": " << ans << endl;}
}
