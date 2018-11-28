#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<iomanip>
//setprecision
using namespace std;
class W{
	public:
//W* l;
//W* r;
int l;
int d;
int y;
};
int compare(const void* a,const void* b){
	//return *((int*)a)-*((int*)b);
	return ((W*)a)->d-((W*)b)->d;
}
	//qsort(a,10,sizeof(int),compare);
int main(){
	int TT;
	cin>>TT;
	int n;
//	int d[10010];
//	int l[10010];
	int x;
	W w[10010];
	for(int T=1;T<=TT;++T){
		cin>>n;
		for(int i=0;i<n;++i){
			cin>>w[i].d>>w[i].l;
			w[i].y=0;
		}
		cin>>x;

		qsort(w,n,sizeof(W),compare);
		
		int l;
		int d;
		int g;
		d=w[0].d;
		if(w[0].d>w[0].l)
			l=w[0].l;
		else
			l=w[0].d;
		w[0].y=l;
		cerr<<d<<" "<<l<<endl;
		for(int i=0;i<n;++i){
			cerr<<"?"<<w[i].d<<" "<<w[i].y<<endl;
			for(int j=i+1;j<n;++j){
				if(w[j].d<=w[i].d+w[i].y){
					if(w[j].d-w[i].d>w[j].l)
						l=w[j].l;
					else
						l=w[j].d-w[i].d;
					if(l>w[j].y)
						w[j].y=l;
				}
			}
		}
		g=0;
		for(int i=0;i<n;++i){
			if(w[i].d+w[i].y>=x)
				g=1;
		}
		cout<<"Case #"<<T<<": ";
		if(g)
			cout<<"YES";
		else
			cout<<"NO";
		printf("");
		cout<<"\n";
	}
	return 0;
}
