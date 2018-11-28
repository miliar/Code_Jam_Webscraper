#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<cmath>
using namespace std;

const int INF=1000111222;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

int main() {
	int testow;
	scanf("%d",&testow);
	for(int z=1;z<=testow;++z) {
		int n,k;
		scanf("%d%d",&n,&k);
		bool wynik=(k%(1<<n))+1==(1<<n);
		printf("Case #%d: %s\n",z,(wynik?"ON":"OFF"));
	}
}
