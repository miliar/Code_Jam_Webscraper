#include<stdio.h>
#include<string.h>
#include<string>
#include<cstdlib>
#include<vector>
using namespace std;


char line[200];
int N,c,d;

int mp[300][300];
vector<int>op[300];
int exi[300],True;

char fao[20];
char str1[100000];

int main()
{
    freopen("B.in","rt",stdin);
    freopen("B.out","wt",stdout);
    int tst,cas;
    scanf("%d",&tst);
    for(cas=1;cas<=tst;cas++)
    {
        True++;
        scanf("%d",&c);
        memset(mp,0,sizeof(mp));
        for(int i=0;i<300;i++) op[i].clear();
        for(int i=0;i<c;i++)
        {
            scanf("%s",&fao);
            mp[fao[0]][fao[1]]=fao[2];
            mp[fao[1]][fao[0]]=fao[2];
        }

        scanf("%d",&d);
        for(int i=0;i<d;i++)
        {
            scanf("%s",&fao);
            op[fao[0]].push_back(fao[1]);
            op[fao[1]].push_back(fao[0]);
        }
        scanf("%d",&N);
        scanf("%s",&line);

        int sz=0;
        for(int i=0;i<N;i++)
        {
            if(i==0) {
                str1[sz]=line[i];

                sz++;
                str1[sz]=0;
            }
            else
            {
                str1[sz]=line[i];
                exi[line[i]]=True;
                sz++;
                if(sz-2>=0)
                {
                    if(mp[str1[sz-1]][str1[sz-2]]!=0)
                    {
                        //exi[str1[sz-1]]=True-1;
                        //exi[str1[sz-2]]=True-1;
                        char ff=mp[str1[sz-1]][str1[sz-2]];
                        //exi[ff]=True;
                        str1[sz-2]=ff;
                        str1[sz-1]=0;sz=sz-1;
                    }
                    else
                    {
                        bool fn=false;
                        for(int j=0;j<op[line[i]].size();j++)
                        {
                            for(int l=0;l<sz-1;l++)
                            {
                                if(op[line[i]][j]==str1[l])
                                {
                                    fn=true;
                                    break;
                                }
                            }
                            if(fn) break;

                        }
                        if(fn)
                        {

                            sz=0;
                            str1[sz]=0;
                        }
                    }
                }
            }
        }

        printf("Case #%d: [",cas);
        for(int i=0;i<sz;i++)
        {
            if(i) printf(", ");
            printf("%c",str1[i]);
        }
        printf("]\n");


    }
    return 0;
}
