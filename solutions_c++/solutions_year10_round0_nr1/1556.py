

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <iostream>
#include <vector>
#include <utility>
#include <set>
#include <map>
#include <string>
#include <complex>
#include <functional>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <fstream>
using namespace std;

/*bool cmp(const acm &A, const acm &B)
{
	if(A.x < B.x) return true;
	if(B.x < A.x) return false;
	if(A.y < B.y) return true;
	return false;
	if(A.m>B.m)return true;
	if(A.m<B.m)return false;
	if(A.t<B.t)return true;
	if(A.t>B.t)return false;
	if(A.n<B.n)return true;
	return false;
}*/

int stage[32];
int tt[31];
void deal(int n,int k,int jj){
	/*memset(stage,0,sizeof(stage));
	int flag;//label the first position of false
	flag=0;
	//int res=0;//0:OFF;1:ON
	for(int i=0;i<k;i++){
		for(int j=0;j<=flag;j++){
			stage[j]=!stage[j];
		}
		for(int j=0;;j++)
			if(!stage[j]){
				flag=j;
				break;
			}
	}
	int res=0;
	for(int i=0;i<n;i++){
		if(!stage[i]){
			break;
		}
		if(i==n-1)res=1;
	}
	if(res)printf("Case #%d: ON\n",jj);
	else printf("Case #%d: OFF\n",jj);*/
	if(abs(k%tt[n]-tt[n])-1==0)printf("Case #%d: ON\n",jj);
	else printf("Case #%d: OFF\n",jj);
};
int main() {
	freopen("E:/A-large.in","r", stdin);
	freopen("E:/A-large.out", "w", stdout);
    //printf("hello\n");
	int t,n,k;
	//int tmp=1;
	//printf("%d",!tmp);
	tt[0]=1;
	for(int i=1;i<31;i++){
		tt[i]=2*tt[i-1];
	}
	while(scanf("%d",&t)!=EOF){
		for(int jj=1;jj<=t;jj++){
			scanf("%d%d",&n,&k);
			deal(n,k,jj);
		}
	}
    return 0;
}






