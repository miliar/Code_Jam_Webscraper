#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
using namespace std;
vector<char> ans;
char combine[200][200];
char s[200];
char destroy[150];
int present[150];
int main()
{
    int i,j,k,t,T,n,c,d;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d",&c);
        memset(combine,0,sizeof(combine));
        for(i=0;i<c;i++)
        {
            scanf("%s",s);
            //printf("%s\n",s);
            combine[s[0]][s[1]]=s[2];
            combine[s[1]][s[0]]=s[2];
        }
        scanf("%d",&d);
        memset(destroy,0,sizeof(destroy));
        memset(present,0,sizeof(present));
        for(i=0;i<d;i++)
        {
            scanf("%s",s);
            //printf("%s\n",s);
            destroy[s[0]]=s[1];
            destroy[s[1]]=s[0];
        }
        scanf("%d",&n);
        scanf("%s",s);
        //printf("%s\n",s);
        ans.clear();
        ans.push_back(s[0]);
        present[s[0]]=1;
        int len=0;
        for(i=1;i<n;i++)
        {
            if(combine[s[i]][ans[ans.size()-1]] && ans.size())
            {
                //printf("here1");
                len=ans.size()-1;
                present[ans[len]]--;
                ans[len]=combine[s[i]][ans[len]];
                present[ans[len]]++;

            }
            else
            {
                ans.push_back(s[i]);
                present[s[i]]++;
            }
            if(ans.size()>1)
                if(present[destroy[ans[ans.size()-1]]])
                {
                    ans.clear();
                    //printf("here2");
                    memset(present,0,sizeof(present));
                }
            //printf("%d\n",ans.size());
        }
        printf("Case #%d: [",t);
        if(ans.size())
        for(i=0;i<(ans.size()-1);i++)
            printf("%c, ",ans[i]);
        if(ans.size())
            printf("%c",ans[i]);
        printf("]\n");
    }
    return 0;
}
