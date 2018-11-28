#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <map>
#include <cmath>
#include <cstring>
#include <string>
using namespace std;

int TC,A,B,b[2000005],pw[20],AC,x,cnt,p,y,pre,last;

int main(){
	scanf("%d",&TC);
	pw[0] = 1;
	for (int i=1;i<10;i++) pw[i] = pw[i-1] * 10;
	
	for (int C=1;C<=TC;C++){
		scanf("%d%d",&A,&B);
		for (int i=A;i<=B;i++) b[i] = 0;
		AC = 0;
		
		for (int i=A;i<=B;i++){
			x = i;
			cnt = 1;
			b[x] = 1;
			p = 0;
			while (x>=10) p++,x/=10;
			x = i;
			for (int j=1;j<=p;j++){
				last = x % pw[j];
				pre = x - last;
				y = pre / pw[j] + last * pw[p+1-j];
				if (A <= y && y <= B && !b[y]){
					cnt++;
					b[y] = 1;
				}
			}
			AC += ((cnt) * (cnt-1)) / 2;
		}
		printf("Case #%d: %d\n",C,AC);
	}
	return 0;
}
