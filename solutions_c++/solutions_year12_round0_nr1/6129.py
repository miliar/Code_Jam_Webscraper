#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <stack>
#include <bitset>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> pii; 

#define				pb	push_back
#define	 present(x, c)	((c).find(x) != (c).end()) 			// used for map and set. //
#define		forn(i, n)	for(int i = 0; i < n; i++)
#define             S   scanf
#define             P   printf

int main()
{
    int t,i,j,cs=1;
    string str;
    vi map(26,0);
    string s="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string m="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    
    for(i=0;i<s.size();i++)
    {
                           map[s[i]-'a'] = m[i]-'a';
                           
    }
    map['q'-'a'] = 'z'-'a';
    map['z'-'a'] = 'q'-'a';
    //for(i=0;i<map.size();i++) 
   // cout<<char(i+'a')<<" "<<char(map[i]+'a') << endl ;

    cin>>t;
    getline(cin,str);
    while(t>0)
    {
              str.clear();
              getline(cin,str);
              
              
          
              for(i=0;i<str.size();i++) str[i]= map[str[i]-'a'] + 'a';
              
              
              printf("Case #%d: ",cs++);
              cout<<str<<endl;
              
              t--; 
              
    }
    
  return 0;
}
