#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string.h>
#include <map>

using namespace std;

int T;
int C,D,N;
int top;

char Mer[4],Con[3],Str[110],ans[110];

int Mertab[9][9];
bool Contab[9][9];
bool temp[9];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    map<char,int> m;
    cin>>T;
    char s[9]={'a','Q','W','E','R','A','S','D','F'};
    for(int i=1;i<9;i++)
    {
        m.insert(make_pair(s[i],i));
    }
//    cout<<m['a']<<endl;
//    return 0;
    for(int t=1;t<=T;t++)
    {
        memset(Contab,0,sizeof(Contab));
        memset(Mertab,0,sizeof(Mertab));
        memset(temp,0,sizeof(temp));
        top=0;
        scanf("%d",&C);
        for(int i=0;i<C;i++)
        {
            cin>>Mer;
            Mertab[m[Mer[0]]][m[Mer[1]]]=Mer[2];
            Mertab[m[Mer[1]]][m[Mer[0]]]=Mer[2];
        }
        scanf("%d",&D);
        for(int i=0;i<D;i++)
        {
            cin>>Con;
            Contab[m[Con[0]]][m[Con[1]]]=1;
            Contab[m[Con[1]]][m[Con[0]]]=1;
        }
        scanf("%d",&N);
        cin>>Str;
        bool bo;
        for(int i=0;i<N;i++)
        {
            if(i==0) {ans[top++]=Str[i]; continue;}
            if(top&&m[ans[top-1]]&&Mertab[m[ans[top-1]]][m[Str[i]]])
            {
                ans[top-1]=Mertab[m[ans[top-1]]][m[Str[i]]];
//                cout<<ans[top-1]<<" "<<top<<endl;
                continue;
            }
            else
            {
                if(top&&m[ans[top-1]]) temp[m[ans[top-1]]]=1;
                ans[top++]=Str[i];
            }
            for(int j=1;j<9;j++)
            {
                if(temp[j])
                {
                    if(Contab[m[Str[i]]][j])
                    {
                        top=0;
                        memset(temp,0,sizeof(temp));
                    }
                }
            }
        }
        printf("Case #%d: [",t);
        for(int i=0;i<top-1;i++)
        {
            printf("%c, ",ans[i]);
        }
        if(top) printf("%c]\n",ans[top-1]);
        else printf("]\n");
    }
    return 0;
}
