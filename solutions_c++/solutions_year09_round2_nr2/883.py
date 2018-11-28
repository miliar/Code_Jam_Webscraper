#include<iostream>
#include<sstream>
#include<vector>
#include<string.h>
#include<set>
#include<stack>
#include<algorithm>
#include<map>
#include<cmath>
#include<climits>
#include<queue>
#include<cstdio>
#include<cstdlib>

using namespace std;

#define I (int)
#define D (double)
#define PB push_back
#define FF first
#define SS second
#define MK make_pair
#define GI ({int temp; scanf("%d",&temp); temp;})
#define all(x) x.begin(),x.end()
#define out(x) printf("Case #%d: %d\n", cnum, x);
#define LL long long
#define VI vector <int>

string getLine() {
  string s;
  while(!feof(stdin)) {
    char c = fgetc(stdin);
    if(c == 13) continue;
    if(c == 10) return s;
    s += c;
    }
  return s;
}

bool same(int a,int b)
{
        int cnt[10];
        memset(cnt,0,sizeof cnt);        
        
        while(a)
        {
                cnt[a%10]++;
                a/=10;
        }
        
        while(b)
        {
                cnt[b%10]--;
                b/=10;
        }
        
        for(int i=1;i<10;i++)
        if(cnt[i])
        return false;
        
        return true;
        
        
        
}

bool largest(string str)
{
        if(next_permutation(str.begin(),str.end()))
        return false;
        
        return true;
}

void solve(int cnum)
{
        int i;
        string num;
        cin>>num;
        string ans;
        
        if(largest(num))
        {
               //sort(num.begin(),num.end());
               int cnt[10];
               memset(cnt,0,sizeof cnt);
               
               for(i=0;i<num.size();i++)
               cnt[num[i]-'0']++;
               
               cnt[0]++;
               for(i=1;i<10;i++)
               {
                        while(cnt[i]--)
                        {
                                ans+=(char)(i+'0');
                        }
               }
               
              
              ans.insert(ans.begin()+1,cnt[0],'0');
              
              //goto end;
              
        }
        
        
        else
        {
                /*mn='9'+1;
                for(i=0;i<num.size()-1;i++)
                if(num[i]<=mn)
                mn=num[i],ind=i;
                
                for(i=ind+1;i<num.size();i++)
                {
                        if(num[i]>mn && mn1>num[i])
                        mn1=num[i],ind1=i;
                
                }
                
                swap(num[ind],num[ind1]);
                
                for(i=0;i<)*/
                
                next_permutation(num.begin(),num.end());
                ans=num;
        }
        
        cout<<"Case #"<<cnum<<": "<<ans<<endl;
}

int main()
{

        int N=GI;
        
        for(int cnum=1;cnum<=N;cnum++)
        {
                solve(cnum);
        }
        return 0;
}
