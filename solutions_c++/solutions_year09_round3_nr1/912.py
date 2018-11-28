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
#define left Left
#define right Right


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




void solve(int cnum)
{
        string s;
        
        
        getline(cin,s);
        
        map <int,int> dig;
        map <int,int> found;
        
        int i,mx=-1;
        
        /*for(i=0;i<s.size();i++)
        {
                if(s[i]>='0' && s[i]<='9' && dig.find(s[i])==dig.end())
                {
                        dig[s[i]]=s[i]-'0';
                        found[s[i]-'0']=s[i];
                        mx=max(s[i]-'0',mx);
                        
                        //cout<<s[i]<<" :: "<<s[i]-'0'<<endl;
                }
        }*/
        
        for(i=0;i<s.size();i++)
        {
                if(dig.find(s[i])!=dig.end())
                continue;
                
                for(int j=0;j<1000;j++)
                {
                        if(!i && !j)
                        continue;
                        
                        if(!found[j])
                        {
                                found[j]=s[i];
                                dig[s[i]]=j;
                                mx=max(mx,j);
                                
                                //cout<<s[i]<<"->"<<j<<endl;
                                break;
                        }
                }
        }
        
        LL j=1,ans=0;
        
        
        for(i=s.size()-1;i>=0;i--,j*=(LL)(mx+1))
                ans+=(dig[s[i]]*j);
        
        
        cout<<"Case #"<<cnum<<": "<<ans<<endl;
        
          
        
}

int main()
{

        int N;
        scanf("%d\n",&N);
        
        for(int cnum=1;cnum<=N;cnum++)
        {
                solve(cnum);
        }
        return 0;
}
