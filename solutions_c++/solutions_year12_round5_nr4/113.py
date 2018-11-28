#include<cmath>
#include<cstdio>
#include<cctype>
#include<vector>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;

#define sqr(a) (a)*(a)
#define cub(a) (a)*(a)*(a)
#define for1(i,a,b) for(i=(a);i<(b);i++)
#define for2(i,a,b) for(i=(a);i>(b);i--)
#define same(a) memset((a),0,sizeof(a));
#define ll long long

int cmpint(const void*a,const void *b)
{
    if(((int*)a)[0]==((int*)b)[0])
      return ((int*)a)[1]-((int*)b)[1];
    return ((int*)a)[0]-((int*)b)[0];
}

char s[1000005];
int a[1000005];
int flag[205][205];
int n,m;
int ch[1005];
int t[1005],b[1005];
void check(int i){
    int k=s[i],j=s[i+1];
    if(flag[s[i]][s[i+1]]==0){
        t[s[i]]++;
        b[s[i+1]]++;
        flag[s[i]][s[i+1]]=1;
        m++;
    }
    if(ch[k]>=0){
        if(flag[ch[k]+48][s[i+1]]==0){
            t[ch[k]+48]++;
            b[s[i+1]]++;
            flag[ch[k]+48][s[i+1]]=1;
            m++;
        }
    }
    if(ch[j]>=0){
        if(flag[s[i]][ch[j]+48]==0){
            b[ch[j]+48]++;
            t[s[i]]++;
            flag[s[i]][ch[j]+48]=1;
            m++;
        }
    }
    if(ch[j]>=0&&ch[k]>=0){
        if(flag[ch[k]+48][ch[j]+48]==0){
            b[ch[j]+48]++;
            t[ch[k]+48]++;
            flag[ch[k]+48][ch[j]+48]=1;
            m++;
        }
    }
    return;
}

int main()
{
    int i,j,k,l,o,p;
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    scanf("%d",&p);
    for1(i,0,200) ch[i]=-48;
    ch['o']=0;
    ch['i']=1;
    ch['e']=3;
    ch['a']=4;
    ch['s']=5;
    ch['t']=7;
    ch['b']=8;
    ch['g']=9;
    for1(o,0,p){
        same(flag);
        same(b);
        same(t);
        scanf("%d",&k);
        scanf("%s",s);
        l=strlen(s);
        m=n=0;
        for1(i,0,l-1){
            check(i);
        }
        n=m*2;
        for1(i,0,200)
          if(b[i]>0&&t[i]>0){
                n-=min(b[i],t[i]);
        }
        if(n==m) n+=1;
        printf("Case #%d: %d\n",o+1,n);
    }
    return 0;
}
