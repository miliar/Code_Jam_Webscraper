#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>

#define maxn 2222

using namespace std;

int test,n,x,y,sumx,sumy,res,gt,sum;
int a[maxn];

void input(){
	int i;
	scanf("%d",&n);
	gt=0;
	sum=0;
	for (i=1;i<=n;i++){
		scanf("%d",&a[i]);
		sum=sum+a[i];
		gt=gt^a[i];
		if (i==1) res=a[i]; else res=min(res,a[i]);
	}
}

void visit(int i){
	int j;
	for (j=0;j<=1;j++){
		if (j==0){
			x=x^a[i];
			sumx=sumx+a[i];
		}else{
			y=y^a[i];
			sumy=sumy+a[i];
		}
		if (i<n) visit(i+1); else 
			if ((x==y)&&(sumx>0)&&(sumy>0)){
				res=max(res,sumx);
				res=max(res,sumy);
			}
		if (j==0){
			x=x^a[i];
			sumx=sumx-a[i];
		}else{
			y=y^a[i];
			sumy=sumy-a[i];
		}
	}
}

void process_1(){
	res=0;
	x=0;
	sumx=0;
	y=0;
	sumy=0;
	visit(1);
}

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	scanf("%d",&test);
	int i;
	for (i=1;i<=test;i++){
		input();
		//process_1();
		cout<<"Case #"<<i<<": ";
		if (gt!=0) cout<<"NO\n"; else cout<<sum-res<<"\n";
	}
}
