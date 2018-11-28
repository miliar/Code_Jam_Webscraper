//{{{
#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <valarray> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <memory> 
#include <new> 
#include <iterator> 
#include <limits> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
#include <cctype> 
using namespace std;
//}}}

int A[1000010],R[1000000];
int n,s,m;
void add(int a,int delta){
	for(a++;a<=n;a+=a&-a)
		A[a]+=delta;
}
int get(int a){
	int ret=0;
	for(a++;a>0;a-=a&-a)
		ret+=A[a];
	return a;
}
int find(int a){
	int p=0;
	for(int i=s;i>0;i>>=1)
		if(p+i<=n&&A[p+i]<a)
			a-=A[p+=i];
	return p;
}
int main(){
	int tests;
	scanf("%d",&tests);
	for(int t=1;t<=tests;t++){
		scanf("%d%d",&n,&m);
		for(s=1;s+s<=n;s<<=1);
		memset(A,0,sizeof(A[0])*(n+1));
		for(int i=0;i<n;i++)
			add(i,1);
		int pos=0;
		for(int i=0;i<n;i++){
			pos=(pos+i)%(n-i);
			int now=find(pos+1);
			R[now]=i;
			add(now,-1);
		}
		printf("Case #%d:",t);
		for(int i=0;i<m;i++){
			int tmp;
			scanf("%d",&tmp);
			printf(" %d",R[tmp-1]+1);
		}
		printf("\n");
	}
scanf("%*s");
	return 0;
}
