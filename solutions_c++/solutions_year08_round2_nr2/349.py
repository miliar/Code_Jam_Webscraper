#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<sstream>
#include<map>
#include<queue>
#include<set>
#define vvi vector<vector<int> >
#define co continue
#define pb push_back
#define vi vector<int>
#define vs vector<string>
#define br break
#define re return
#define ALL(v) v.begin(),v.end() 

#define REP(i,n) for(int i=0;i<(int) n;i++)
#define LL long long
#define SZ size()
#define INF (2<<29)

#define pii pair<int ,int>
#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin() ; it!=(c).end() ;it++)
template <class T> inline int BITCNT(T x) { int ret=0; while (x) { ret++; x&=x-1; } return ret; }

using namespace std;
#define MN 1001
bool prime[MN];
vector<int > primes;
void sieve(int MAX)
{
 	 memset(prime , true , sizeof(prime));
 	 prime[0]=prime[1]=false;

 	 for(int i=2;i<=MAX ;i++)
 	 {
	  	  		 
	     if(prime[i])
		 {
		  			 primes.push_back(i);
		  			 for(LL j =(LL) i*i ;j<=MAX ;j+=i)
		  			 {
					  		prime[j]=false;
 					 }
		 }		 
     }
     return ;
}

int p[1001],rank[1001];// max_size 
void make_set(int n){
    for(int i=1;i<=n;i++){
        p[i]=i;
        rank[i]=0;
    }
}
int find_set(int x){
    if(x!=p[x])
       p[x]=find_set(p[x]);
    return p[x];
}
void link(int x,int y){
    if(rank[x]>rank[y]){
        p[y]=x;
    }
    else{
        p[x]=y;
        if(rank[x]==rank[y])
           rank[y]++;
    }
}                    
void unite(int x,int y){
    link(find_set(x),find_set(y));
}
int main()
{
	sieve(1000);
//	cout<<primes.size()<<endl;
    int kases;
    cin>>kases;
    for(int kase = 1 ; kase<=kases; kase++)
    {
		int A , B;
		cin>>A>>B;
		int P;
		cin>>P;
		make_set(B);
		for(int i=0;i<primes.size();i++)
		{
			if(primes[i]>=P)
			{
				for(int j=A;j<=B;j++)
				{
					if(j%primes[i]) continue;
					for(int k=j+1;k<=B;k++)
					{
						if(k%primes[i]) continue;
						unite(j,k);
					}
				}
			}
		}
		int res=0;
		for(int i=A;i<=B;i++) if(find_set(i)==i) res++;
	cout<<"Case #"<<kase<<": "<<res<<endl;;		
	}

}
