#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
int gcd(int a,int b){
	return b?gcd(b,a%b):a;
}

using namespace std;
char str[10010][20];
int len[10010];
char order[300][30],word[20];
int se[30][10010];
int main(){
    int tt,i,j,o,k,choose,num[300],c,cost;
    freopen("B-small-attempt3.in","r",stdin);
    freopen("B-small-attempt3.out","w",stdout);
    scanf("%d",&tt);
    for (int tcas = 1;tcas<=tt;tcas++){
        int N,M;
        scanf("%d%d",&N,&M);
        for (i=0;i<N;i++)
        scanf("%s",str[i]),len[i] = strlen(str[i]);
        for (i=0;i<M;i++)
        scanf("%s",order[i]);
        printf("Case #%d:",tcas);
        for (o = 0;o<M;o++){
            int Max = -1,Maxc = -1;
            for (choose = 0;choose<N;choose++){
                memset(word,-1,sizeof(word));
                memset(num,0,sizeof(num));
                se[0][0] = 0;
                for (i=0;i<N;i++)
                if (len[choose]==len[i])
                 {
                     se[0][++se[0][0]] = i;
                     for (j=0;j<len[i];j++)
                         num[str[i][j]]++;
                 }
                int now = 0,then = 1;
                cost = 0;
                for (int cc=0;cc<26;cc++)
                if (num[order[o][cc]]>0){
                   /* for (set<int>::iterator p = se.begin(),q;p!=se.end();p++)                  
                    */
                   /* for (i=1;i<=se[now][0];i++)
                    printf("%d ",se[now][i]);
                    printf(" %c\n",order[o][cc]);*/
                   bool lose = true;
                   c = order[o][cc];
                   for (j=0;j<len[choose];j++)
                   if (str[choose][j]==c)
                      word[j] = c,lose = false;

                   if (lose) cost++;
                   se[then][0] = 0;
                   for (i=1;i<=se[now][0];i++){
                       int p = se[now][i];
                       for (j=0;j<len[choose];j++)
                           if ((word[j]!=-1&&word[j]!=str[p][j])||(word[j]==-1&&str[p][j]==c)){
                              for (k=0;k<len[choose];k++)
                                  num[str[p][k]]--;
                              break;
                           }
                           
                       //printf("%d %d---\n",p,j);
                       if (j==len[choose]) se[then][++se[then][0]] = p;
                   }
                   if (se[then][0]==1) break;
                   now^=1,then^=1;
                }
               // printf("%s %d\n",str[choose],cost);
                if (cost>Max){
                   Max = cost;
                   Maxc = choose;
                }
            }
            printf(" %s",str[Maxc]);
        }
        printf("\n");
    }
}
            
        
