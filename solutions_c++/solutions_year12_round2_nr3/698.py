#include<cstdio>
#include<cstdlib>
#include<ctime>
#include<cassert>
#include<cmath>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<numeric>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<sstream>
using namespace std;
#define LOOP(x,y,z) for((x)=(y);(x)<=(z);(x)++)
#define LOOPB(x,y,z) for((x)=(y);(x)<(z);(x)++)
#define RLOOP(x,y,z) for((x)=(y);(x)>=(z);(x)--)
#define RLOOPB(x,y,z) for((x)=(y);(x)>(z);(x)--)
#define ABS(x) ((x)<0?-(x):(x))
#define PI 3.1415926535898

	vector<int> nums;
template<class T> string i2s(T x){ostringstream o; o<<x;return o.str();}

int calc(int x){
	int i,ret=0;
	LOOPB(i,0,nums.size()){
		if(x&(1<<i)){
			ret+=nums[i];
		}
	}
	return ret;
}


void out_res(int x){
	int i;
	LOOPB(i,0,nums.size()){
		if(x&(1<<i)){
			printf("%d ",nums[i]);
		}
	}
	printf("\n");
}

int main(){
	int i,j,k,a,m,n,s,t,l,tt,cas;
	const int oo=1<<29;
	char tmp,str[500],ch;
	float f1,f2;
	map<int,int> ma;
	#ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
	freopen("out","w",stdout);
	#endif
	scanf("%d\n",&tt);
	cas=0;
	while(++cas,tt--){
		nums.clear();
		ma.clear();
		printf("Case #%d: \n", cas);
		scanf("%d",&n);
		LOOPB(i,0,n){
			scanf("%d",&m);
			nums.push_back(m);
		}
		LOOPB(i,0,(1<<20)-1){
			int sum=calc(i);
			map<int,int>::iterator iter;
			iter=ma.find(sum);
			if(iter!=ma.end()){
				out_res(iter->second);
				out_res(i);
				goto next;
			}else{
				ma.insert(make_pair(sum,i));
			}
		}
		next:
			;
	}
	
	return 0;
}
