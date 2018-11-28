#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 

int n,m;
set<string> memo;

int oku(){
    memo.clear();
    scanf("%d%d",&n,&m);
     //cout<<n<<" "<<m<<endl;
    string ss;
    string s;
    int ans=0;
    memo.insert("/");
    
    for(int i=0;i<n;i++)
    {
     cin>>ss;
     //cout<<ss<<endl;
     ss+='/';
     string s="";
     for(int i=0;i<ss.size();i++)
     if(ss[i]!='/') s+=ss[i]; 
     else { s+=ss[i];
     	    memo.insert(s); //cout<<s<<endl;
      	  }
     
    }
    for(int i=0;i<m;i++)
    {
     cin>>ss;
     //cout<<ss<<endl;
     ss+='/';
     string s="";
     for(int i=0;i<ss.size();i++)
     if(ss[i]!='/') s+=ss[i]; 
     else { s+=ss[i];
            if(!present(memo,s)) {ans++; memo.insert(s);}
      	  }
     
    }
    return ans;
}


int main(){
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);

int t; scanf("%d",&t);
for(int i=1;i<=t;i++)
{
printf("Case #%d: ",i);
cout<<oku();
cout<<endl;
}


return 0;}