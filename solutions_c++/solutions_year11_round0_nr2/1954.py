#include <cstdio>
#include <cstring>
#include <stack>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <map>
using namespace std;
int mp[100][100];
int  tt[10000];
char re[10000];
int vst1[100][100];
int vst2[100][100];
char s[10000];
int main()
{
    int t,n;
    int C,D;


    freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
    scanf("%d",&t);
    int cas=0;
    while(t--)
    {
        scanf("%d",&C);
        memset(vst1,0,sizeof(vst1));
        memset(vst2,0,sizeof(vst2));
        for(int i=0;i<C;i++)
        {
            scanf("%s",s);
            mp[s[0]-'A'][s[1]-'A']=s[2]-'A';
            mp[s[1]-'A'][s[0]-'A']=s[2]-'A';
            vst1[s[0]-'A'][s[1]-'A']=1;
            vst1[s[1]-'A'][s[0]-'A']=1;
        }
        scanf("%d",&D);
        for(int i=0;i<D;i++)
        {
            scanf("%s",s);
            vst2[s[0]-'A'][s[1]-'A']=1;
            vst2[s[1]-'A'][s[0]-'A']=1;
        }
        scanf("%d",&n);
        scanf("%s",s);
        stack <int> q1,q2;
        for(int i=0;i<n;i++)
        {
            int id=s[i]-'A';
            if(q1.empty())
                q1.push(id);
            else if(vst1[id][q1.top()])
            {
                int tmp=q1.top();
                q1.pop();
                q1.push(mp[id][tmp]);
            }
            else
               q1.push(id);
            q2=q1;
            int cnt=0;
            while(!q2.empty())
            {
                int tmp=q2.top();
                tt[cnt++]=tmp;
                q2.pop();
            }
            if(cnt<2)
              continue;
            bool flag=false;
            for(int j=0;j<cnt&&!flag;j++)
              for(int k=j+1;k<cnt&&!flag;k++)
              {
                  if(vst2[tt[j]][tt[k]])
                    {
                        while(!q1.empty())
                           q1.pop();
                        flag=true;
                        break;
                    }
              }


        }
        int cnt=0;
        while(!q1.empty())
          {
              int tmp=q1.top();
              q1.pop();
              re[cnt++]=tmp+'A';
          }
        printf("Case #%d: ",++cas);
        printf("[");
        for(int i=cnt-1;i>=1;i--)
          printf("%c, ",re[i]);
        if(cnt>0)
          printf("%c",re[0]);
        printf("]\n");

    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
