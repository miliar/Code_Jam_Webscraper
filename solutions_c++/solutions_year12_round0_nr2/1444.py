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
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int t[105];
bool flag[105];
int main(){

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int Case,n,s,p,res;
	scanf("%d",&Case);
	
	for(int cas = 1; cas <= Case; cas ++){
		
		scanf("%d %d %d",&n,&s,&p);
		for(int i = 0; i < n; i ++){
			scanf("%d",&t[i]);
		}
		res = 0;
		sort(t,t + n);
		for(int i = 0; i < n; i ++){
			if(s && t[i] > 1){
				int tmp;
				if(t[i] % 3 == 1) tmp = t[i] / 3 + 1;
				if(t[i] % 3 == 2) tmp = t[i] / 3 + 2;
				if(t[i] % 3 == 0) tmp = t[i] / 3 + 1;
				if(tmp >= p) {
					res ++;
					s --;
				}
			}else {
				int tmp;
				if(t[i] % 3 == 1) tmp = t[i] / 3 + 1;
				if(t[i] % 3 == 2) tmp = t[i] / 3 + 1;
				if(t[i] % 3 == 0) tmp = t[i] / 3;
				if(tmp >= p){
					res ++;
				}
			}

		}
		printf("Case #%d: %d\n",cas,res);
	}

	return 0;
}