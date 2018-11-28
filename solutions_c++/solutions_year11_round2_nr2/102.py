#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>

#define maxn 211
#define maxC 1000000000001LL

using namespace std;

int test,n;
double len,res;
double a[maxn];
int b[maxn];

void input(){
	int i;
	scanf("%d",&n);
	cin>>len;
	for (i=1;i<=n;i++){
		cin>>a[i];
		scanf("%d",&b[i]);
	}
}

void Quicksort(int L,int H){
	int i,j;
	double pivot;
	if (L>=H) return;
	pivot=a[rand()%(H-L+1)+L];
	i=L;
	j=H;
	while (i<=j){
		while (a[i]<pivot) i++;
		while (a[j]>pivot) j--;
		if (i<=j){
			if (i<j){
				swap(a[i],a[j]);
				swap(b[i],b[j]);
			}
			i++;
			j--;
		}
	}
	Quicksort(L,j);
	Quicksort(i,H);
}

bool search(double key){
	int i;
	double w,epsilon;
	epsilon=0.00000001;
	for (i=1;i<=n;i++){
		if (i==1){
			w=a[i]-key;
			w=w+(double)(b[i]-1)*len;
			if (abs(a[i]-w)>key+epsilon) return false;
			continue;
		}
		w=max(w+len,a[i]-key);
		if (abs(a[i]-w)>key+epsilon) return false;
		w=w+(double)(b[i]-1)*len;
		if (abs(a[i]-w)>key+epsilon) return false;
	}
	return true;
}

void process(){
	int i;
	double l,r,mid,epsilon;
	epsilon=0.00000001;
	l=0;
	r=maxC;
	res=maxC;
	for (i=1;i<=1000;i++){
		mid=(l+r)/2;
		if (search(mid)){
			res=min(res,mid);
			r=mid-epsilon;
		}else l=mid+epsilon;
	}
}

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	scanf("%d",&test);
	int i;
	for (i=1;i<=test;i++){
		input();
		Quicksort(1,n);
		process();
		printf("Case #%d: %0.6lf\n",i,res);
	}
}
