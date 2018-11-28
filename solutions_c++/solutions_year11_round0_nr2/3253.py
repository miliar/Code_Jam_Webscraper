#include <iostream>
using namespace std;
#include <stdio.h>
int change[26][26];
bool Clr[26][26];
char op[200];
char end[200];
int last;
int main()
{
    int T,N;
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&T);
    for(int CA=1;CA<=T;CA++)
    {
        string now;
        memset(change,-1,sizeof(change));
        memset(Clr,false,sizeof(Clr));
        scanf("%d",&N);
        while(N--)
        {
            cin>>now;
            change[now[0]-'A'][now[1]-'A']=now[2]-'A';
            change[now[1]-'A'][now[0]-'A']=now[2]-'A';
        }
        scanf("%d",&N);
        while(N--)
        {
            cin>>now;
            Clr[now[0]-'A'][now[1]-'A']=true;
            Clr[now[1]-'A'][now[0]-'A']=true;
        }
        int noull;
        cin>>noull>>op;
        last=-1;
        for(int i=0;i<strlen(op);i++)
        {
            if(last==-1) { end[0]=op[i]; last=0; }
            else if(change[op[i]-'A'][end[last]-'A']!=-1)
            {
                end[last]=char(change[op[i]-'A'][end[last]-'A']+'A');
            }
            else
            {
                bool flag=true;
                for(int j=last;j>=0;j--)
                    if(Clr[end[j]-'A'][op[i]-'A']==true)
                    {
                        flag=false;
                        last=-1;
                        break;
                    }
                if(flag==true) end[++last]=op[i];
            }
        }
        end[last+1]='\0';
        printf("Case #%d: [",CA);
        for(int i=0;i<strlen(end);i++)
        {
            if(i!=0) printf(", ");
            cout<<end[i];
        }
        cout<<"]"<<endl;
    }
    return 0;
}
