#include<iostream>
#include<cstdio>
#include<cstring>
#include<set>
using namespace std;
int f(int s){
	int c = 0;
	while(s){
		c++;
		s/=10;
	}
	return c;
}

int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int t;
	scanf("%d",&t);
	int a[7];
	a[0] = 1;
	for(int i = 1;i<7;i++)a[i] = 10*a[i-1];
	int casenum = 0;
	while(t--){
		
		int ans = 0;
		int A,B;
		scanf("%d%d",&A,&B);
		int num = f(A);
		printf("Case #%d: ",++casenum);
		if(num==1){
			printf("0\n");
			continue;
		}
	//	memset(visit,false,sizeof(visit));
		for(int i = A;i<B;i++){
			set<int>  s;
			for(int j = num-1;j>=1;j--){
				int ret1 = i%a[j];
				int ret2 = i/a[j];
				int k = ret1*a[num-j]+ret2;
				if(k >i && k<=B && s.find(k)==s.end()){
					s.insert(k);
					///visit[k] = true;
					///printf("%d %d\n",i,k);
					ans++;
				}
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}