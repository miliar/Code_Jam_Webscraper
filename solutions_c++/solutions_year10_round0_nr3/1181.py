/*  File: main.cpp  Author: Administrator Created on 2010年5月8日, 上午8:47 */

#include <stdlib.h>
#include<iostream>
#include<vector>
#include<algorithm>
#include<stdio.h>
#include<set>
using namespace std;
#define maxn 10005
#define len 1001
#define out(x) (cout<<#x<<"="<<x<<endl)
int R,K,N;
int v1[len],v2[len];
long long b[maxn],sum[maxn];

struct node{
    int a[len],id;
    node (){}
    node (int *t,int Id){
        for(int i=1;i<=N;i++) a[i]=t[i];
        id=Id;
    }
    void  set(int *t,int Id){
        for(int i=1;i<=N;i++) a[i]=t[i];
        id=Id;
    }
    bool operator <(const node & B)const{
        int i;
        for(i=1;i<=N;i++) {
            if(a[i]<B.a[i]) return true;
        }
        return false;
    }
};

void pr(int *a){
    for(int i=1;i<=N;i++) printf("%d ",a[i]);
    printf("\n");
}
void pr(long long *a){
    for(int i=0;i<=N;i++) printf("%lld ",a[i]);
    printf("\n");
}
long long sloved(){
    int i,j,k; node tmp;
    set<node> st; set<node>::iterator it;
    int *f=v1,*g=v2; f[N+1]=(long long)1<<60;
    sum[0]=0;
    tmp.set(f,0);
    st.insert(tmp);
    for(i=1;i<=R;i++){
        int p=0;
        int idx=0;
        for(j=1;j<=N;j++){
            if(p+f[j]<=K) idx=j,p+=f[j];
            else break;
        }
        k=1;
        for(j=idx+1;j<=N;j++) g[k++]=f[j];
        for(j=1;j<=idx;j++) g[k++]=f[j];
     //   out(i);
    //    pr(g);
        b[i-1]=p;
        if(i==1) sum[0]=b[0];
        else sum[i-1]=sum[i-2]+b[i-1];
        tmp.set(g,i);
        it=st.find(tmp);
        if(it==st.end()){
            st.insert(tmp);
            if(i==R) return sum[R-1];
        }else{
            break;
        }
        
   
        swap(f,g);
    }
    int I=i;
    int Id=it->id;
    int T=(i-Id);
 //   out(I);out(Id);out(T);
  //  pr(b);
 //   pr(sum);
    long long Tsum=sum[I-1]-sum[Id-1];
   // out(Tsum);
    R--;
    int idx=(R-Id)%T+Id;
  //  out(idx);
    return sum[Id-1]+((R-Id)/T)*Tsum + ( sum[idx] - sum[Id-1]);

}
int main(int argc, char** argv) {
    int ca=8,i,j,t,cas=0;
    freopen("C-large.in","r",stdin);
    freopen("out.out","w",stdout);
    cin>>ca;
    while(ca--){
        scanf("%d%d%d",&R,&K,&N);
        for(i=1;i<=N;i++){
            scanf("%d",v1+i);
            if(v1[i]>K) i--,N--;
        }
        printf("Case #%d: %lld\n",++cas,sloved());
    }
    return (EXIT_SUCCESS);
}
/*Input

Output

3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3
 Case #1: 21
Case #2: 100
Case #3: 20
10 1
2
*/
