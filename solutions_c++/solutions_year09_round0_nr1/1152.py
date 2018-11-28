#include <iostream>
using namespace std;

int l,d,n;
const int maxcharvalue = 256;


struct bor
{
    bor *next[256];
        
    bor()
    {
        memset(next,0,sizeof(next));
    }
};

bor start;
char word[4096];

struct findres
{
    bor *nowb[2][8096];
    int knowu[2];
    int nowt;
    bool cango[256];
    
    int wcg[256];
    int wcgcount;
    
    void init()
    {        
        knowu[0] = 1;
        nowb[0][0] = &start;
        memset(cango, 0, sizeof(cango));
        nowt = 0;
    }
    
    void addletter(char a)
    {
        cango[(int)a] = true;
    }
    
    void refresh()
    {
        wcgcount = 0;
        for(int i=0;i<maxcharvalue;i++)
            if (cango[i]) 
            {   
                wcg[wcgcount++]=i;
                cango[i] = false;
            }
        knowu[1-nowt] = 0;
        for(int i=0;i<knowu[nowt];i++)
            for(int j=0;j<wcgcount;j++)
                if (nowb[nowt][i]->next[wcg[j]] != 0)
                    nowb[1-nowt][knowu[1-nowt]++] = nowb[nowt][i]->next[wcg[j]];
        nowt = 1-nowt;        
    }
    
    int getanswer()
    {        
        return knowu[nowt];
    }
};


int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d%d%d",&l,&d,&n);
    for(int i=0;i<d;i++)
    {
        scanf("%s",word);
        bor *np = &start;
        for(char *nw = word; *nw != 0; nw++)
        {
            int ch = (int)(*nw);
            if (np->next[ch] == 0)
                np->next[ch] = new bor();        
            np = np->next[ch];
        }
    }
    findres algor;    
    for(int i=0;i<n;i++)
    {
        scanf("%s",word);        
        algor.init();
        int status = 0;
        for(int j=0;word[j]!=0;j++)
        {
            if (word[j]=='(')
                status = 1;
            else
            if (word[j]==')')
            {
                status = 0;   
                algor.refresh();
            }
            else
            {
                algor.addletter(word[j]);                    
                if (status == 0)
                    algor.refresh();                    
            }
        }
        printf("Case #%d: %d\n", i+1, algor.getanswer());
    }
    return 0;
}
