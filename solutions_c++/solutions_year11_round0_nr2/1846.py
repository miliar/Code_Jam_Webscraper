#include <iostream>
#include <vector>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cstdlib>
#include <string.h>
#include <memory.h>
using namespace std;
template <class T> void OUT(T x, int n){  for(int i = 1; i <= n; ++i)  cout << x[i] << ' ';    cout << endl;    }
template <class T> void OUT(T x, int n, int m){  for(int i = 1; i <= n; ++i)    OUT(x[i], m);    cout << endl;    }
template <class T> void checkmod(T& a,T m){ a=(a%m+m)%m;}
#define  eps 1e-8
#define  LL long long
inline LL mod(LL x, LL y) { return x - floor(1.0 * x / y+eps) * y; }
#define  out(x) (cout << #x << " = " << x << endl)
#define  Set(a,b)  memset(a,b,sizeof(a))
#define  Sqr(x) ((x) * (x))
#define  pi  acos(-1.0)
const int maxn = 1005,INF = (1<<29);
int n,m;

map<string,int> combine;
map<string,int> oppose;
char com[10],opp[10],in[105];
char Stack[105];
int main()
{
//    freopen("in.txt","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,k,t,T,x,y,sum,index;
    cin>>T;
    for(t=1;t<=T;t++){
        combine.clear();
        oppose.clear();
        int c,d;
        string a="",b="";
        scanf("%d",&c);
        for(i=0;i<c;i++){
            a="";
            scanf("%s",com);
            a+=com[0];
            a+=com[1];
            combine[a]=com[2]-'A'+1;
            a="";
            a+=com[1];
            a+=com[0];
            combine[a]=com[2]-'A'+1;
        }
        scanf("%d",&d);
        for(i=0;i<d;i++){
            a="";
            scanf("%s",opp);
            a+=opp[0];
            a+=opp[1];
            oppose[a]=1;
            a="";
            a+=opp[1];
            a+=opp[0];
            oppose[a]=1;
        }
        scanf("%d%s",&n,in);
        int head=0;
        for(i=0;i<n;i++){
            if(head==0) Stack[head++]=in[i];
            else{
                a="";
                a+=Stack[head-1];
                a+=in[i];
                x=combine[a];
                if(x){
                    Stack[head-1]=x+'A'-1;
                }
                else{
                    for(j=0;j<head;j++){
                        a="";
                        a+=Stack[j];
                        a+=in[i];
                        y=oppose[a];
                        if(y){
                            head=0;
                            break;
                        }
                    }
                    if(!y) Stack[head++]=in[i];
                }
            }
//            out(head);
//            for(j=0;j<head;j++) cout<<Stack[j]<<" ";
//            puts("");
        }
        printf("Case #%d: [",t);
        for(i=0;i<head;i++){
            if(i==head-1) printf("%c",Stack[i]);
            else printf("%c, ",Stack[i]);
        }
        printf("]\n");
    }
    return 0;
}
