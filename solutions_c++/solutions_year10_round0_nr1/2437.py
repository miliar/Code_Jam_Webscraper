#include <iostream>
#include<algorithm>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include <cstdio>
#include<map>
#include<stack>
#include<set>
#include<queue>
#include<cctype>
#include<assert.h>
#include<numeric>
#include<ctime>
#include<iterator>
//#include<sstream>
using namespace std;



int main() {
	freopen("A.in.txt", "r", stdin);
	freopen("A.out.txt", "w", stdout);
	int t,ca=1;cin>>t;
	while(t--){
		int n,k;
		scanf("%d%d",&n,&k);
		int des = (1<<n) - 1,div = 1<<n;
		int ans = k%div;
		//cout<<"ans: "<<ans<<" des:"<<des<<endl;
		if(ans==des){
			printf("Case #%d: ON\n",ca++);
		}
		else{
			printf("Case #%d: OFF\n",ca++);
		}
	}
    return 0;
}

