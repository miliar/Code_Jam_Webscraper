#include<iostream>
#include<cstdlib>
#include<cstdio>

using namespace std;

int T;
int N,M;
char word[10010][15];
char list[30];
int ca[15];
int lose[10010];
int co;
int len;
bool val[10010];
bool ff;
int anj,anr,ans,ank;
bool fk;

int main()
{
    freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
    cin>>T;
    while(T--)
    {
        cin >> N >> M;co++;
        cout<< "Case #"<<co<<":";
        memset(ca,0,sizeof(ca));
        for(int i = 1;i<=N;i++)
            cin>>word[i];
        for(int i=1;i<=N;i++)
            for(int j=1;j<=N;j++)
            {
                ca[strlen(word[i])]++;
            }
        for(int i=1;i<=M;i++)
        {
            cin >> list;
            memset(lose,0,sizeof(lose));
            for(int j=1;j<=N;j++)
            {
                len=strlen(word[j]);
                if(ca[len]==1)
                {
                    lose[j]=0;
                    continue;
                }
                memset(val,0,sizeof(val));
                for(int r=1;r<=N;r++)
                {
                    if(r==j || strlen(word[r])!=strlen(word[j])) continue;
                    val[r]=1;
                }
                for(int k=0;k<26;k++)
                {
                    fk=0;
                    for(int r=1;r<=N;r++)
                    {
                        if(!val[r]) continue;
                        ff=1;
                        for(int t=0;t<len;t++)
                        {
                            if(list[k]==word[j][t] && list[k]!=word[r][t])
                            {
                                ff=0;break;
                            }
                            if(list[k]!=word[j][t] && list[k]==word[r][t])
                            {
                                ff=0;break;
                            }
                        }
                        anj=anr=0;
                        for(int t=0;t<len;t++)
                        {
                            if(list[k]==word[j][t]) anj++;
                            if(list[k]==word[r][t]) anr++;
                        }
                        if(anj!=anr) ff=0;
                        if(anj==0 && anr>0)
                        {
                                fk=1;
                        }
                        //cout << list[k] << " " << anj << " "<< anr<<" "<<fk<<endl;

                        if(!ff) val[r] = 0;
                    }
                    if(fk) lose[j]++;
                    ff=0;
                    for(int r=1;r<=N;r++)
                    if(val[r]==1) {ff=1;break;}
                    if(!ff) break;
                }
            }
            ans=lose[1];ank=1;//cout<<1<<" "<<lose[1]<<endl;
            for(int k=2;k<=N;k++)
            {
            //    cout<<k<< " "<<lose[k]<<endl;
                if(lose[k]>ans)
                {
                    ans=lose[k];
                    ank=k;
                }
            }
            cout<< " "<<word[ank];
        }
        cout << endl;
    }
    return 0;
}
