#include<iostream>
#include<cstdio>
#include<string>
#include<map>
using namespace std;

int main()
{
    int T,tc=0;
    scanf("%d",&T);
    getchar();
    for(;tc!=T;tc++)
    {

        int C;
        scanf("%d",&C);
        getchar();
        char compress[26][26];
        for(int i=0;i<26;i++)
            for(int j=0;j<26;j++)
                compress[i][j]='-';
        for(int i=0;i<C;i++)
        {
            string s;
            cin>>s;
            compress[s[0]-'A'][s[1]-'A']=s[2];
            compress[s[1]-'A'][s[0]-'A']=s[2];
        }
        int D;
        scanf("%d",&D);
        getchar();
        bool oppose[26][26];
        memset(oppose,0,sizeof(oppose));
        for(int i=0;i<D;i++)
        {
            string t;
            cin>>t;
            int now;
            oppose[t[0]-'A'][t[1]-'A']=true;
            oppose[t[1]-'A'][t[0]-'A']=true;
        }
        int K;
        scanf("%d",&K);
        getchar();
        string now;
        cin>>now;
        bool present[26];
        memset(present,0,sizeof(present));
        int currind=1;
        while(currind!=now.length())
        {
            bool ch=false;
            if(currind > 0 && compress[now[currind] - 'A'][now[currind-1] - 'A']!='-')
            {
                ch=true;
                now[currind-1]=compress[now[currind]-'A'][now[currind-1]-'A'];
                now.erase(currind,1);
                currind --;
            }
            else for(int k=0;k<currind;k++)
            {
                if(oppose[now[k]-'A'][now[currind]-'A'])
                {
                    now=now.substr(currind+1);
                    currind=0;
                    ch=true;
                    break;
                }
            }
            if(!ch)
                currind++;
        }
        printf("Case #%d: [", tc+1);
        for(int i=0;i<now.length();i++)
        {
            printf("%c",now[i]);
            if(i!=now.length() -1)
            {
                printf(", ");
            }
        }
        printf("]\n");
    }
}
