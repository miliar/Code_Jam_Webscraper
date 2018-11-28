#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include<cstdlib>
#include<cstring>
#include<string>


using namespace std;

#define pb push_back
#define sz size
#define all(a)  a.begin(),a.end()
#define SZ(v) ((int)(v).size())
#define gcj_print(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}


typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef vector<string> vs;
typedef long long  ll;

int main()
{
   int t,test=0;
   scanf("%d",&t);
   while(t--)
   {
      char st[22];
      scanf("%s",st);
      string s=st;
      //cout<<next_permutation( all(s) )<<endl;
      //cout<<s<<endl;
      int len=SZ(s);
      string s1=s;
      sort(all(s1));
      reverse(all(s1));
      if(s!=s1)
      {
         //vi d;
         //for(int i=0;i<len;i++)d.pb(s[i]-'0');
         next_permutation( all(s) );
         cout << "Case #" << ((test)+1) << ": " << s << endl;
      }
      else
      {
         string s2=s,s3;
         //s2.pb(s[0]);
         sort(all(s2));
         int i=0;
         for(i=0;i<len && s2[i]=='0';i++);
         s3.pb(s2[i]);
         s3.pb('0');
         int ind=i;
         for(i=0;i<len;i++){if(i!=ind)s3.pb(s2[i]);}  
         cout << "Case #" << ((test)+1) << ": " << s3 << endl;
      }
      test++;
   }      
   return 0;
}   
