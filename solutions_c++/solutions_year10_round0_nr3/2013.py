#include<cstdio> 
#include<cstdlib> 
#include<cstring> 
#include<cmath> 
#include<iostream> 
#include<sstream> 
#include<string> 
#include<string.h>
#include<algorithm> 
#include<map> 
#include<set> 
#include<vector> 
#include<queue> 

#define ALL(x) (x).begin(),(x).end()
#define FOR(x,a,b) for (int x=a; x<b;++x)
#define CLR(a,b) memset(a,b,sizeof(a)) //rellenar de 0's

using namespace std;

int main(){
	int total;
	cin>>total;
	FOR(i,0,total){
		int r,k,n,p;
		cin>>r>>k>>n;
		vector <int> ar;
		FOR(j,0,n){
			cin>>p;
			ar.push_back(p);
		}
		vector<int> pai(n,0);
		vector<int> tam(n,0);
		FOR(j,0,n){
			p=j;
			int sum=0;
			while(sum+ar[p]<=k){
				sum+=ar[p];
				p = (p+1)%n;
				if (p==j)
					break;
			}
			tam[j]=sum;
			pai[j]=p;
		}
		vector<long long> acu(n,0);
		vector<int> visit(n,0);
		int vueltas = 1;
		int ind = 0;
		while(visit[ind]==0){
			visit[ind]=vueltas;
			if (vueltas>r)
				break;
			FOR(q,0,n){
				if (visit[q]!=0)
					acu[q]+=tam[ind];
			}
			ind = pai[ind];
			vueltas++;
		}
		long long res = acu[0];
		if (vueltas>r)
			printf("Case #%d: %lld\n",i+1,res);
		else{
			int vueltasFaltan = r - vueltas + 1;
			long long valorciclo = acu[ind];
			long long longciclo = vueltas - visit[ind];
			int m = vueltasFaltan/longciclo;
			int sobra = vueltasFaltan - m*longciclo;
			res += (long long)m*(long long)valorciclo;
			while(sobra!=0){
				res += tam[ind];
				ind = pai[ind];
				sobra--;
			}
			printf("Case #%d: %lld\n",i+1,res);
		}
	}
}