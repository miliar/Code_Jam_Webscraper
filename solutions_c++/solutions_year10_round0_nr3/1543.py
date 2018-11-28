

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

int stage[1024];

struct group{
	int up,v;//down;
};

group gg[100000];

void deal(int r,int k,int n,int jj){
	long long res,tmp;
	tmp=0;
	if(n==1){
		//printf("%d\n",stage[0]);
		if(stage[0]<=k)printf("Case #%d: %I64d\n",jj,long long(stage[0]*r));
		else printf("Case #%d: %I64d\n",jj,tmp);
		return ;
	}
	for(int i=0;i<n;i++){
		tmp+=stage[i];
		if(tmp>k){break;}
	}
	if(tmp<=k){
		printf("Case #%d: %I64d\n",jj,long long(tmp*r));
		return ;
	}
	tmp=0;
	int j=0;
	int label=0;
	int m;
	for(int i=0;;i++){
		if(i==n)i=0;
		//printf("%d",label);
		if(label!=0)break;
		tmp+=stage[i];
		//printf("%I64d",tmp);
		int st;
		if(i+1==n)st=0;
		else st=i+1;
		if(tmp+stage[st]>k){
			gg[j].up=i;
			gg[j++].v=tmp;
			for(m=0;m<j-1;m++){
				if(gg[m].up==i&&gg[m].v==tmp){label=j-1;break;}
			}
			//if(j==1)label=0;
			tmp=0;
		}
		else continue;
	}
	res=0;
	for(int i=0,j=0;i<r;i++,j++){
		if(j==label){j=m;}
		res+=gg[j].v;
	}
	printf("Case #%d: %I64d\n",jj,res);
};

int main() {
	freopen("E:/C-large.in","r", stdin);
	freopen("E:/C-large.out", "w", stdout);
    //int i=10;
	//int j=1000000000;
	//printf("%d",i*j);
	int t,r,k,n;
	while(scanf("%d",&t)!=EOF){
		for(int jj=1;jj<=t;jj++){
			scanf("%d%d%d",&r,&k,&n);
			for(int i=0;i<n;i++)
				scanf("%d",&stage[i]);
			deal(r,k,n,jj);
		}
	}
    return 0;
}






