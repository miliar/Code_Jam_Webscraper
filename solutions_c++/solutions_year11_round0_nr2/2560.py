#include <iostream>
#include <stdio.h>
#include <string.h>
#include <climits>
#include <map>
using namespace std;
map<char,int> ctoi;
map<int,char> itoc;
char map1[110][110];
int map2[110][110];
bool vist[150];
string str;
char ch[200],ans[150];
int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    ctoi.insert(make_pair('Q',1));
    ctoi.insert(make_pair('W',2));
    ctoi.insert(make_pair('E',3));
    ctoi.insert(make_pair('R',4));
    ctoi.insert(make_pair('S',5));
    ctoi.insert(make_pair('D',6));
    ctoi.insert(make_pair('F',7));
    itoc.insert(make_pair(2,'W'));
    itoc.insert(make_pair(1,'Q'));
    itoc.insert(make_pair(3,'E'));
    itoc.insert(make_pair(4,'R'));
    itoc.insert(make_pair(5,'S'));
    itoc.insert(make_pair(6,'D'));
    itoc.insert(make_pair(7,'F'));
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        int n;
        cin>>n;
        memset(map1,0,sizeof(map1));
        memset(map2,0,sizeof(map2));
        for(int i=1;i<=n;i++)
        {
            cin>>str;
            map1[ctoi[str[0]]][ctoi[str[1]]]=str[2];
            map1[ctoi[str[1]]][ctoi[str[0]]]=str[2];
        }
        cin>>n;
        for(int i=1;i<=n;i++)
        {
            cin>>str;
            map2[ctoi[str[0]]][ctoi[str[1]]]=-1;
            map2[ctoi[str[1]]][ctoi[str[0]]]=-1;
        }
        cin>>n;
        cin>>&ch[1];
        int cnt=0;
        memset(vist,0,sizeof(vist));
        for(int i=1;i<=n;i++)
        {
            if(cnt==0)
            {
                cnt=1;
                ans[1]=ch[i];
                continue;
            }
            if(map1[ctoi[ch[i]]][ctoi[ans[cnt]]]!=0)
            {
                if(vist[cnt]==0)
                {
                    char tmp=map1[ctoi[ch[i]]][ctoi[ch[i-1]]];
                    ans[cnt]=tmp;
                    vist[cnt]=1;
                    continue;
                }
            }
            else
            {
                for(int j=1;j<=cnt;j++)
                {
                    if(map2[ctoi[ch[i]]][ctoi[ans[j]]]==-1&&vist[j]==0)
                    {
                        cnt=0;
                        memset(vist,0,sizeof(vist));
                        break;
                    }
                }
                if(cnt==0) continue;
            }
            ans[++cnt]=ch[i];
        }
        printf("Case #%d: [",k);
        for(int i=1;i<=cnt;i++)
        {
            if(i==1)
            {
                printf("%c",ans[i]);
                continue;
            }
            printf(", %c",ans[i]);
        }
        printf("]\n");
    }
    return 0;
}
