/*	SURENDRA KUMAR MEENA	*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <queue>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
#define FF(i,m,n)	for(int i=m;i<n;i++)
#define F(i,n)	FF(i,0,n)

int main(){
	int t;
	cin>>t;
	FF(i,1,t+1){
		int n,k;
		cin>>n>>k;
		printf("Case #%d: ",i);
		if((((1<<n)-1) & k)==((1<<n)-1))	puts("ON");
		else							puts("OFF");
	}
	return 0;
}
