#include<iostream>
#include<map> 
using namespace std;
int N,M;
string W[10010];
string List;

int uid[10010];//每个单词的组号 
int olduid[10010];

int cnt[100010];//每个组的单词个数 
bool NowAppear[100010];//改组是否出现了能匹配当前字符的单词

map<string,int> HASH[100010];
 
int ans[10010];
int maxuid;//最大组号

bool Appear[10010][26];//对于 每个字符是否在单词里出现过 
int Position[26];//每个字符在List里的位置 


void Solve()
{
     memset(cnt,0,sizeof(cnt));
     memset(ans,0,sizeof(ans));
     memset(uid,0,sizeof(uid));
     for (int i=0;i<N;++i)
     {
         uid[i]=W[i].size();
         cnt[W[i].size()]++;
         maxuid=max(maxuid,int(W[i].size()));
     }//初始化 
     for (int i=0;i<26;++i) Position[List[i]-'a']=i; 
     for (int c=0;c<26;++c)//枚举当前字符 
     {
         for (int i=0;i<N;++i) olduid[i]=uid[i];//备份uid 
         memset(NowAppear,0,sizeof(NowAppear));
         
         char tmp=List[c];//当前考虑的字符 
         
         for (int i=0;i<=maxuid;++i) HASH[i].clear(); 
         
         for (int i=0;i<N;++i)
         if (cnt[uid[i]]>1)
         {
            string MODE="";
            for (int j=0;j<W[i].size();++j)
            {
                if (W[i][j]==tmp) NowAppear[uid[i]]=true;
                if (Position[W[i][j]-'a']<=c) MODE+=W[i][j]; else MODE+='_';
            }
            map<string ,int >::iterator IT;
            IT=HASH[uid[i]].find(MODE);
            if (IT==HASH[uid[i]].end()) 
            {
                HASH[uid[i]][MODE]=++maxuid;
                uid[i]=maxuid;
            } else
            {
                  uid[i]=HASH[uid[i]][MODE];
            }              
         }
         for (int i=0;i<N;++i) 
         if ( (!Appear[i][tmp-'a']) &&  NowAppear[olduid[i]] ) ans[i]++;
         memset(cnt,0,sizeof(cnt));
         for (int i=0;i<N;++i) cnt[uid[i]]++;
     }
     int maxans=-1;
     for (int i=0;i<N;++i) maxans=max(maxans,ans[i]);
     for (int i=0;i<N;++i)
     if (ans[i]==maxans)
     {
         cout<<W[i];
         break;
     }
}


int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int T;
    cin>>T;
    for (int k=1;k<=T;++k)
    {
          cout<<"Case #"<<k<<":";
          cin>>N>>M;
          for (int i=0;i<N;++i) cin>>W[i];
          memset(Appear,0,sizeof(Appear));
          for (int i=0;i<N;++i)
                    for (int j=0;j<W[i].size();++j)
                        Appear[i][W[i][j]-'a']=true;
          for (int i=0;i<M;++i)
          {
              cin>>List;
              cout<<" ";
              Solve();
          }
          cout<<endl;
    }    
    return 0;
}
