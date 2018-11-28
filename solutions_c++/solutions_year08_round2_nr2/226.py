#include <cstdio>
#include <set>
#include <cmath>

using namespace std;

#define MAX 1005

int p[MAX],rank[MAX];
void make_set(int x){
    p[x] = x;
    rank[x]=0;
}

void link(int x, int y) {
    if(rank[x]>rank[y])
        p[y] = x;
    else {
        p[x] = y;
        if(rank[x]==rank[y])
        rank[y] = rank[y] + 1;
    }
}

int find_set(int x) {
    if(x != p[x])
    p[x] = find_set(p[x]);
    return p[x];
}
void union_set(int x, int y) {
    link(find_set(x),find_set(y));
}

int prime[1005];

bool isprime(int n){
    return prime[n];
}



int main(){
    int test;
    scanf("%d",&test);
    memset(prime,-1,sizeof(prime));
    for(int i=2;i<1005;i++)
        if(prime[i])
            for(int j=i+i;j<1005;j+=i)
                prime[j]=0;
    
    for(int t=0;t<test;t++){
        int a,b,p;
        scanf("%d %d %d",&a,&b,&p);
        for(int i=a;i<=b;i++)
            make_set(i);
        
        for(int i=a;i<=b;i++)
            for(int j=i+1;j<=b;j++)
                for(int k=p;k<=b;k++)
                    if(isprime(k)&&(i%k)==0&&(j%k)==0){
                        union_set(i,j);
                    }
        set<int> si;
        for(int i=a;i<=b;i++)
            si.insert(find_set(i));
        printf("Case #%d: %d\n",t+1,si.size());
    }
    return 0;
}
