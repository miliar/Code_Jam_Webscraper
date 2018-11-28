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
const int SIZE = 1000;
const int mmd = 10000;
char gg[]="welcome to code jam";
char buff[SIZE];
int miaomiao[400];
void mywork(){
	memset(miaomiao,0,sizeof(miaomiao));
	int n = strlen(gg);
	int m = strlen(buff);
	int i,j;
	for (i=m-1;i>=0;i--){
		for (j=0;j<n;j++){
			if (gg[j]==buff[i]){
				if (j==n-1){
					miaomiao[n-1]=(miaomiao[n-1]+1)%mmd;
				}else{
					if (miaomiao[j+1]>0){
						miaomiao[j]=(miaomiao[j]+miaomiao[j+1])%mmd;
					}
				}
			}
		}
	}
}
int main(){
	int cas;
	scanf("%d",&cas);
	int i;
	gets(buff);
	for (i=1;i<=cas;i++){
		gets(buff);
		mywork();
		int ans = miaomiao[0]%mmd;
		printf("Case #%d: %04d\n",i,ans);
	}
	return 0;
}
