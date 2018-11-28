#include <stdlib.h>
#include <algorithm>
#include <stdio.h>
#include <cstring>
#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <functional>
#include <stack>
#include <cmath>
#define MMset(a,b) memset(a,b,sizeof(a))
#define max(a,b)   ((a)>(b)?(a):(b))
#define min(a,b)   ((a)<(b)?(a):(b))
#define eps 1e-8
using namespace std;
int T,C,D,N;
int com[26][26];
bool rev[26][26];
int ins[26];
int main()
{
    
    //freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        scanf("%d",&C);
        MMset(com,-1);
        MMset(rev,0);
        MMset(ins,0);
        stack<int>S;
        char str[101],in[3];
        for (int i=0;i<C;i++)
        {
            scanf("%s",in);
            com[in[0]-'A'][in[1]-'A']=com[in[1]-'A'][in[0]-'A']=in[2]-'A';
        }
        scanf("%d",&D);
        for (int i=0;i<D;i++)
        {
            scanf("%s",in);
            rev[in[0]-'A'][in[1]-'A']=rev[in[1]-'A'][in[0]-'A']=1;
            
        }
        scanf("%d",&N);
        scanf("%s",&str);
        for (int i=0;i<N;i++)
        {
            int s = str[i]-'A';
            if (S.empty()) S.push(str[i]-'A'),ins[s]++;
            else
            {
                int t = S.top();
                while (com[t][s]!=-1)
                {
                      s=com[t][s];
                      ins[t]--;
                      S.pop();
                      if (S.empty()) break;
                      t=S.top();
                }
                int cnt=0;
                for (int j=0;j<26;j++)
                {
                    if (ins[j] && rev[s][j]) cnt+=ins[j];
                }
                if (cnt==0) 
                {
                   S.push(s);
                   ins[s]++;
                   continue;
                }
                if (cnt!=0)
                {
                   MMset(ins,0);
                   while (!S.empty()) S.pop();
                }
            }    
        }
        char res[123],pi=0;
        while (!S.empty())
        {
              res[pi++]=S.top()+'A';
              S.pop();
        }
        reverse(res,res+pi);
        res[pi]='\0';
        printf("Case #%d: [",cas);
        for (int i=0;i<pi;i++)
        {
            printf("%c",res[i]);
            if (i+1<pi) printf(", ");
        }
        printf("]\n");
    }
}
