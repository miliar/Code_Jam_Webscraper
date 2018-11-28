#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cmath>
#include <vector>

#define maxn 2000

using namespace std;

int test,n;
long long res;
int a[maxn];
int b[maxn];

void input(){
	int i;
	cin>>n;
	for (i=1;i<=n;i++) cin>>a[i]>>b[i];
}

void Quicksort(int L,int H){
	int i,j,pivot;
	if (L>=H) return;
	i=L;
	j=H;
	pivot=a[rand()%(H-L+1)+L];
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

void process(){
	int i,j;
	res=0;
	if (n==1) return;
	for (i=1;i<n;i++)
		for (j=i+1;j<=n;j++)
			if (b[j]<b[i]) res++;
}

int main(){
	//freopen("A-large.in","r",stdin);
	//freopen("output.txt","w",stdout);
	cin>>test;
	int i;
	for (i=1;i<=test;i++){
		input();
		Quicksort(1,n);
		process();
		cout<<"Case #"<<i<<": " <<res<<"\n";
	}
}
