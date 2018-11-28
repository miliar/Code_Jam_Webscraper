#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<utility>
#include<set>
#include<sstream>
#define fr(a,b,c) for (a=b;a<=c;a++)
#define frr(a,b,c) for (a=b;a>=c;a--)
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
using namespace std;

char d[256][256],o[256];
int st[111],last;

int main()
{
   int test,it,n,i,j,cc,dd;
   string s;
   cin >> test;
   fr(it,1,test)
   {
      memset(d,0,sizeof(d));
      memset(o,0,sizeof(o));
      cin >> cc;
      while (cc--)
      {
         cin >> s; 
         d[int(s[1])][int(s[0])]=int(s[2]);
         d[int(s[0])][int(s[1])]=int(s[2]);
      }
      cin >> dd;
      while (dd--)
      {
         cin >> s;
         o[int(s[1])]=int(s[0]);
         o[int(s[0])]=int(s[1]);
      }
      cin >> n;
      cin >> s;
      last=0;
      fr(i,0,n-1)
      {
         if (!last)
         {
            st[++last]=int(s[i]);
            continue;
         }
         if (d[st[last]][int(s[i])])
            st[last]=d[st[last]][int(s[i])];  
         else
         {
           st[++last]=int(s[i]); 
           fr(j,1,last)
             if (st[j]==o[int(s[i])])
             {
                last=0; break;
             }
         }
       //  fr(j,1,last) cout << st[j] << " "; cout << endl;
      }
      cout << "Case #" << it << ":  [";
      if (last) cout << char(st[1]);
      fr(i,2,last) cout << ", " << char(st[i]);
      cout << "]" << endl;
   }
   return 0;
}
