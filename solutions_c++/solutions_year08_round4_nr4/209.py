
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set> 
#include<queue>
#include<string>
#include<stack>
#include<sstream>
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it) 
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) cerr << #x << " = "; FOREACH(it,(x)) cerr << *it << ","; cerr << "\n"; 
#define fup(i,a,b) for(int i=a;i<=b;i++)
#define fdo(i,a,b) for(int i=a;i>=b;i--)
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) (int)a.size()
#define inf 1000000000
#define SQR(a) ((a)*(a))
using namespace std;
typedef long long int64;

char t[1006];
char t2[1006];
int main(){
	int cas;
	scanf("%d",&cas);
	fup(c,1,cas){
		int k;
		scanf("%d",&k);
		scanf("%s",t+1);
		int n=strlen(t+1);
		vector<int> per;
		fup(i,1,k)per.PB(i);
		int mini=inf;
		do{
			int x=n/k;
			fup(part,0,x-1){
				fup(j,1,k){
					t2[part*k+j]=t[part*k+per[j-1]];
				}
			}	
			int zm=0;
			fup(i,1,n)if(t2[i]!=t2[i-1])zm++;
		if(zm<mini)mini=zm;			
		}while(next_permutation(per.begin(),per.end()));
		printf("Case #%d: %d\n",c,mini);
	}
	return 0;	
}
