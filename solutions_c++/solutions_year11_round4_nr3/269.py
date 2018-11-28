#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <iterator>
#include <bitset>
#include <sstream>
#include <cmath>
#include <cstring>

using namespace std;

#define LL long long

bool f[1111111];
LL n;
void work(){
	cin >> n;
	if (n==1) {puts("0");return ;}

	LL ret=0;
	for (LL i=1;i*i<=n;i++)
		if (!f[i]){
			LL cnt=1,cur=i;
			while (cur<=n) cur=cur*i,cnt++;
			cnt--;
			ret+=cnt-1;
		}
	cout << ret+1 <<endl;
}

void pre(){
	memset(f,0,sizeof(f));
	f[0]=f[1]=1;
	for (LL i=2;i<=1000000;i++){
		if (!f[i]){
			for (LL j=2;j*i<=1000000;j++)
				f[j*i]=1;
		}
	}
}

int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	pre();
	int t;cin >> t;
	for (int i=1;i<=t;i++){
		cout << "Case #"<< i << ":" <<" ";
		work();
	}
	//system("pause");
	return 0;
}
