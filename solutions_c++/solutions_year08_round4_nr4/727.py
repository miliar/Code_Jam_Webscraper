#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cstring>
#include <sstream>
#include <string>

using namespace std;

#define go(i,v) for(typeof(v.begin()) i=v.begin();i!=v.end();i++)
#define fo(i,n) for(int i=0;i<n;i++)
#define fi fo(i,n)
#define fj fo(j,n)
#define all(v) v.begin(),v.end()

inline int get(void) { int x; scanf("%d",&x); return x; }

char S[1001];
char S2[1001];
int soln(){
	int k = get();
	scanf("%s",S);
	int n = strlen(S);
	memset(S2,0,sizeof(S2));

	int perm[5];
	fo(i,k) perm[i]=i;
	int ans=(1<<30);
	do{
		for(int i=0;i<n;i+=k)fo(j,k)S2[i+j]=S[i+perm[j]];
		int temp=0;
		for(int i=1;i<n;i++)if(S2[i]!=S2[i-1])temp++;
		ans=min(ans,temp);
	} while(next_permutation(perm,perm+k));
	return ans+1;
}

int main(void){
	int n = get();
	fi printf("Case #%d: %d\n",i+1,soln());
}
