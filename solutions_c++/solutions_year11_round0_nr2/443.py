/*
5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW
*/
#include<iostream>
#include<cstdio>

using namespace std;

int T;
int C;
int N;
int D;

int inv[30][30];
bool cmp[30][30];
char a,b,c;
int list;
int q[110];

int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    cin >> T;
    for(int num=1;num<=T;num++)
    {
        memset(inv,0,sizeof(inv));
        memset(cmp,0,sizeof(cmp));
        cin >> C;
        for(int i=1;i<=C;i++)
        {
            cin >> a;
            while (a<'A'|| a>'Z') cin >>a;
            cin >> b;
            while (b<'A'|| b>'Z') cin >>b;
            cin >> c;
            while (c<'A'|| c>'Z') cin >>c;
            inv[a-'A'][b-'A']=c-'A';
            inv[b-'A'][a-'A']=c-'A';
        }
        cin >> D;
        for(int i=1;i<=D;i++)
        {
            cin >> a;
            while (a<'A'|| a>'Z') cin >>a;
            cin >> b;
            while (b<'A'|| b>'Z') cin >>b;
            cmp[a-'A'][b-'A']=1;
            cmp[b-'A'][a-'A']=1;
        }
        cin >> N;list = 0;
        for(int i=1;i<=N;i++)
        {
            cin >> a;
            while (a<'A'|| a>'Z') cin >>a;
            if(list == 0)
            {
                list ++;
                q[list]=a-'A';
            }
            else
            {
                if(inv[q[list]][a-'A']>0)
                {
                    q[list]=inv[q[list]][a-'A'];
                    continue;
                }
                for(int j=1;j<=list;j++)
                {
                    if(cmp[q[j]][a-'A']>0 || cmp[a-'A'][q[j]]>0)
                    {
                        list=0;
                        break;
                    }
                }
                if(list!=0)
                {
                    list++;
                    q[list]=a-'A';
                }
            }
            //cout<<list<<" "<<q[list]<<endl;

        }
        cout<<"Case #"<<num<<": [";
        if(list>0) cout<<char(q[1]+'A');
        for(int i=2;i<=list;i++)
            cout<<", "<<char(q[i]+'A');
        cout<<"]"<<endl;
    }
}
