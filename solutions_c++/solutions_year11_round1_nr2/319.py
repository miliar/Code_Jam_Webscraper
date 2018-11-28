/*
    ID:
    PROG:
    LANG:C++
*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <string>
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
#include <cstring>
using namespace std;

string d[10010],l;
int T,n,m;
char s[30];
//list<int> que;
int que[10010],ql;
//vector<int> a[10010][26];
bool b[30];
int best,bests,score;
int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&T);
    for(int cs=1;cs<=T;++cs){
        scanf("%d %d",&n,&m);
        for(int i=0;i<n;++i){
            scanf("%s",s);d[i]=s;
            //for(int j=0;j<26;++j)a[i][j].clear();
        }
        printf("Case #%d: ",cs);
        /*for(int i=0;i<n;++i)
            for(int j=i+1;j<n;++j)
                if(d[i].size()==d[j].size())
                for(int k=0;k<26;++k){
                    int l=0;
                    for(;l<d[i].size();++l)
                        if((d[i][l]==k+'a')!=(d[j][l]==k+'a'))break;
                    if(l==d[i].size()){
                        a[i][k].push_back(j);
                        a[j][k].push_back(i);
                    }
                }*/
        for(int cm=0;cm<m;++cm){
            if(cm!=0)printf(" ");
            scanf("%s",s);
            best=-1;bests=0;
            for(int i=0;i<n;++i){
                score=0;ql=0;
                for(int j=0;j<26;++j)b[j]=0;
                for(int j=0;j<n;++j)
                    if(d[j].size()==d[i].size()){
                        que[ql++]=j;
                        for(int k=0;k<d[j].size();++k)b[d[j][k]-'a']=true;
                    }
                for(int k=0;k<26;++k){
                    if(ql==1)break;
                    int nql=0;
                    if(b[s[k]-'a']==0) continue;
                    int p=0;
                    for(;p<d[i].size();++p)if(d[i][p]==s[k])break;
                    if(p==d[i].size()){
                        ++score;//continue;
                    }
                    for(int u=0;u<26;++u)b[u]=0;
                    for(int u=0;u<ql;++u){
                        int v=0;
                        for(;v<d[i].size();++v)
                            if((d[que[u]][v]==s[k])!=(d[i][v]==s[k]))break;
                        if(v==d[i].size()){
                            que[nql++]=que[u];
                            for(v=0;v<d[i].size();++v)
                                b[d[que[u]][v]-'a']=true;
                        }
                    }
                    ql=nql;
                }
                if(score>best){
                    best=score;bests=i;
                }
            }
            printf("%s",d[bests].c_str());
        }
        printf("\n");
    }
    return 0;
}
