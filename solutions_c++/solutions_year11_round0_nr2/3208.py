#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
using namespace std;

char in[1000];
char frnd[30][30];
bool foe[30][30];
vector<char>out;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("outl.txt","w",stdout);
    int i,j,k,cs;
    int T,C,D,N;
    scanf("%d",&T);
    for(cs=1;cs<=T;cs++)
    {
        memset(frnd,0,sizeof(frnd));
        memset(foe,0,sizeof(foe));
        out.clear();
        scanf("%d",&C);
        for(j=1;j<=C;j++)
        {
            scanf("%s",&in);
            frnd[in[0]-'A'][in[1]-'A']=in[2];
            frnd[in[1]-'A'][in[0]-'A']=in[2];
        }
        scanf("%d",&D);
        for(j=1;j<=D;j++)
        {
            scanf("%s",&in);
            foe[in[0]-'A'][in[1]-'A']=true;
            foe[in[1]-'A'][in[0]-'A']=true;
        }
        scanf("%d",&N);
        scanf("%s",&in);
        int sz;
        out.push_back('A'+28);
        for(j=0;j<N;j++)
        {

            sz=out.size();
            if(frnd[out[sz-1]-'A'][in[j]-'A'])
            {
                out[sz-1]=frnd[out[sz-1]-'A'][in[j]-'A'];
            }
            else
            {
                for(k=1;k<sz;k++)
                {
                    if(foe[out[k]-'A'][in[j]-'A'])
                    {
                        out.clear();
                        out.push_back('A'+28);
                        break;
                    }
                }
                if(k==sz)out.push_back(in[j]);
            }
        }
		sz=out.size();
        printf("Case #%d: ",cs);
        printf("[");
        for(i=1;i<sz;i++)
        {
            if(i==sz-1)printf("%c",out[i]);
            else printf("%c, ",out[i]);
        }
        printf("]\n");
    }
    return 0;
}
