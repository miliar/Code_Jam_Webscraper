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

int c[16];
bool flag[2000001];

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	int Case,a,b,res;
	scanf("%d",&Case);
	for(int cas = 1; cas <= Case; cas ++){

		memset(flag,false,sizeof(flag));

		scanf("%d %d",&a,&b);
		res = 0;

		for(int kk = a; kk <= b; kk ++){

			if(flag[kk]) continue;
			int tmp = kk;
			int index = 0;
			while(tmp){
				c[index ++] = tmp % 10;
				tmp /= 10;
			}
			tmp = kk;
			int cnt = 1;
			for(int i = 0;i < index; i ++){
				c[index + i] = c[i];
				cnt *= 10;
			}
			cnt /= 10;
			int now = 1;
		//	d[now ++] = tmp;
			flag[tmp] = true;
			for(int i = index - 1; i >=1; i --){
				tmp = (tmp % cnt ) * 10 +  c[i];
				//printf("cnt = %d %d kk tmp = %d\n",cnt,kk,tmp);
				if(tmp > a && tmp <= b && !flag[tmp]){
					//d[now ++] = tmp;
					now ++;
					flag[tmp] = true;
				}
			}
			//sort(d,d + now);
			
			if(now >= 2) res += now * (now - 1) / 2;
		}
		
		printf("Case #%d: %d\n",cas,res);
	}
	return 0;
}