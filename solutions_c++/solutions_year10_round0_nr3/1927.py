#include<cstdio>
#include<map>
using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i = a;i < b;++i)

typedef long long LL;

LL mem[10000001];

LL proc(int g[],int r,int k,int n){

	map< pair<int,int> , int> rev;rev.clear();
	
	int index = 0,sum,ng,s = 0,e,mpindex = 0;
	LL ans = 0;
	while(r--){
		sum = 0;
		ng = 0;
		s = index;
		
		while(sum + g[index] <= k && ng < n){
			sum += g[index];
			index = (index + 1) % n;
			ng ++;
		}
		
		e = (n + index - 1) % n;
			
		if( !rev.count( make_pair( s,e ) ) ){		
			mem[mpindex] = 0;
			if(mpindex)	
			mem[mpindex] = mem[ mpindex - 1 ];
			mem[mpindex] += sum;
			ans += sum;			
			rev[ make_pair( s,e ) ] = mpindex ++;
		}
		else
			break;
	

	}
	

	int start = rev[  make_pair( s,e ) ];
	int end = mpindex - 1;
	int size = end - start + 1;
	
	
	return ans + (r/size) * (mem[end] - mem[start - 1]) + mem[start + r % size] - mem[start - 1] ;
}


int main(){
	int test = GI;

	FOR(tt,1,test+1){
		int r = GI,k = GI,n = GI;
		int g[n];

		FOR(i,0,n) g[i] = GI;
		
		printf("Case #%d: %lld\n",tt,proc(g,r,k,n));
	}

	return 0;
}
