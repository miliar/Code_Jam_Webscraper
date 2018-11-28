#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<deque>
#include<complex>
#include<numeric>
using namespace std;

int main() {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	int test;
	scanf("%d",&test);
	for(int no=1;no<=test;++no){
		printf("Case #%d: ", no);
		int n;
		int c=0;
		int val=0x7fffffff;
		int x,s=0;
		scanf("%d",&n);
		for(int i=0;i<n;++i){
			scanf("%d",&x);
			s+=x;
			c^=x;
		//	cout << "--> xor = "<<c<<"  after "<<x<<endl;
			val=min(val,x);
		}
		
		
		
		if(c) {
			puts("NO");
			continue;
		}
		printf("%d\n", s-val);
	}
}
