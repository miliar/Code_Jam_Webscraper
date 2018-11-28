#include<iostream>
#include<algorithm>
#include<cstdio>
#include<set>
#include<map>
#include<vector>
#include<cmath>
#include<queue>
#include<cstring>

#define mp make_pair
#define ll long long

using namespace std;

struct el
{
    string s;
    int tip;
    
    el () {}
    el ( string _s, int _tip ) { s = _s; tip = _tip;}
};

    int n, m, ans =0;
    string tmp;
   
     vector<el> all;
    
bool cmp(el p1, el p2)
{
     if(p1.s == p2.s) return p1.tip > p2.tip;
     return p1.s < p2.s;
} 

int check(string cc, int pos)
{
    int res = 0;
    for( int i = pos; i < (int)cc.size() - 1; ++i )
     if( cc[i] == '/' )res++;
    return res;
}
void solve()
{
     scanf("%d%d\n", &n, &m);
    
    ans = 0;
    all.clear();
    
    for( int i = 0; i < n; ++i )
    {
     cin>>tmp;
      tmp += '/';
     all.push_back(el(tmp,1));
    
    }
        
        for( int i = 0; i < m; ++i )
    {
     cin>>tmp;
     tmp += '/';
     all.push_back(el(tmp,0));
    }   
     
     
     sort(all.begin(),all.end(),cmp);
     
     for( int i = 0; i < (int)all.size(); ++i )
     {
     // cout<<all[i].s<<" "<<all[i].tip<<"\n";
      if( i == 0 )
      {
       if( all[i].tip == 0)
       {
           all[i].tip = 1;
           ans += check(all[i].s,0);
       }
      }
      else
      {
       if( all[i].tip == 0 )
       {
        all[i].tip = 1;
        
        int len = min((int)all[i].s.size(), (int)all[i-1].s.size());
        int xx = 0;
        
        for( int j = 0; j < len; ++j )
         if( all[i].s[j] != all[i-1].s[j] )break;
         else 
         if( all[i].s[j] == '/' ) {xx = j; }
         
        // printf("ff %d\n",xx);
         ans += check(all[i].s, xx);
       }
      }
     }
            printf("%d\n",ans);
 }
int main()
{
    int t;
    scanf("%d",&t);
    for(int i = 1; i <= t; ++i){
                printf("Case #%d: ",i);
                solve();
                }
return 0;
}
