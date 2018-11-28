#include<iostream>
#include<cstring>
#include<string>
#include<cmath>
#include<vector>
#include<map>
#include<algorithm>
#include<set>
using namespace std;

int a[10230];
int main(){
	//freopen("A-small.in","r",stdin);freopen("A-small.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int ncases=0;
	scanf("%d",&ncases);
	for(int cc=1;cc<=ncases;cc++){
		cerr<<cc<<endl;
		int N;
		for(int i=0;i<10230;i++){a[i]=0;}
		scanf("%d",&N);
		for(int i=0;i<N;i++){
			int A,B;
			scanf("%d %d",&A,&B);
			a[A]=B;
		}
		int t=0;
		for(int i=0;i<10230;i++){
			if(a[i]==0)continue;
			int w=a[i];
			for(int j=0;j<i;j++){
				if(a[j]>w)t++;
			}
		}
		printf("Case #%d: ",cc);
		printf("%d\n",t);
	}
}