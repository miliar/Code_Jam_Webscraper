#include<iostream>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
struct wire{
	int left;
	int right;
	void init(int l,int r){left = l;right = r;}
} w[1005];
bool cmp(wire& a,wire& b){
	if(a.left<b.left)
		return true;
	else 
		return false;
}
bool isTr(wire& a,wire& b){
	if(a.right>b.right)
		return true;
	else 
		return false;
}
int main(){
	
	freopen("A-large.in","r",stdin);
	freopen("data.out","w",stdout);
	int k=1;
	int T;
	int l,r;
	int N;
	scanf("%d",&T);
	while(T--){
		int sum = 0;
		scanf("%d",&N);
		for(int i = 0;i < N;i++){
			scanf("%d%d",&l,&r);
			w[i].init(l,r);
		}
		sort(w,w+N,cmp);//ÉýÐòÅÅ
		for(int i = 0 ; i < N-1 ; i ++){
			for(int j = i +1;j< N;j ++)
				if(isTr(w[i],w[j]))
					sum++;
		}
		printf("Case #%d: %d\n",k++,sum);

	}
	return 0;
}