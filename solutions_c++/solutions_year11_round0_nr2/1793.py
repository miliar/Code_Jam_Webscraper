/*
TASK: Problem B. Magicka
LANG: C++
*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<list>
using namespace std;
int N,M,T;
char str[127];
bool ch[40][127],er[40][127];
char chx[40][2],cht[40],err[40][2];
int coin[127];
list<char> s;
list<char>::iterator it;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf("%d",&N);
        for(i=1;i<=N;i++)
        {
            scanf("%s",str);
            ch[i][str[0]]=true;
            ch[i][str[1]]=true;
            cht[i]=str[2];
            chx[i][0]=str[0];
            chx[i][1]=str[1];
        }
        scanf("%d",&M);
        for(i=1;i<=M;i++)
        {
            scanf("%s",str);
            er[i][str[0]]=true;
            er[i][str[1]]=true;
            err[i][0]=str[0];
            err[i][1]=str[1];
        }
        scanf("%d",&k);
        scanf("%s",str);
        bool re=false,ou=false;
        for(i=0;i<k;i++)
        {
            re=false;
            ou=false;
/*/
            printf("(%c/%d)",str[i],k);
            printf("%d [",i);
            for(it=s.begin();it!=s.end();it++)
            {
                printf("%c ",(*it));
            }
            printf("]\n");  
//*/
            for(j=1;j<=N;j++)
            {
                if((str[i]==chx[j][0] && s.back()==chx[j][1]) || 
                    (str[i]==chx[j][1] && s.back()==chx[j][0]))
                {
                    coin[str[i]]--;
                    coin[s.back()]--;
                    s.pop_back();
                    s.push_back(cht[j]);
                    coin[cht[j]]++;
//                    re=true;
                    ou=true;
                    break;
                }
            }
//            if(re)  continue;
            coin[str[i]]++;
            for(j=1;j<=M;j++)
            {
                if(coin[err[j][0]]>0 && coin[err[j][1]]>0)
                {
                    if(err[j][0]==err[j][1] && coin[err[j][0]]<2)
                        continue;
                    s.clear();
                    for(j='A';j<='Z';j++)
                        coin[j]=0;
                    re=true;
                    break;
                }
            }
            if(re||ou)  continue;
            s.push_back(str[i]);
//            coin[str[i]]++;
/*
            printf("%d ((",i);
            for(it=s.begin();it!=s.end();it++)
            {
                printf("%c ",(*it));
            }
            printf("))\n");
//*/
        }
        k=0;
        for(it=s.begin();it!=s.end();it++)
        {
            k++;
        }
        printf("Case #%d: [",tt);
        bool sp=false;
        
        for(it=s.begin();it!=s.end();it++)
        {
            if(sp)  printf(" ");
            sp=true;
            printf("%c",(*it));
            k--;
            if(k!=0)    printf(",");
        }
        printf("]\n");        
        s.clear();
        for(i=1;i<40;i++)
        {
            for(j='A';j<='Z';j++)
            {
                ch[i][j]=false;
                er[i][j]=false;
            }
        }
        for(i='A';i<='Z';i++)
            coin[i]=0;
    }
}
