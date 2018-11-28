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
int r;
int num;
int x;
int y;
};
int compare(const void* a,const void* b){
	//return *((int*)a)-*((int*)b);
	return ((W*)b)->r-((W*)a)->r;
}
int compare2(const void* a,const void* b){
	//return *((int*)a)-*((int*)b);
	return ((W*)a)->num-((W*)b)->num;
}
	//qsort(a,10,sizeof(int),compare);
int main(){
	int TT;
	cin>>TT;
	int n;
	int w;
	int l;
	W c[2000];
	int d;
	int dd;
	int x;
	for(int T=1;T<=TT;++T){
		cin>>n>>w>>l;
		for(int i=0;i<n;++i){
			cin>>c[i].r;
			c[i].num=i;
			c[i].x=-1;
		}
		qsort(c,n,sizeof(W),compare);
		dd=0;
		d=0;
		x=0;
		{
			int i;

			for(i=0;i<n;++i){
				if(x+c[i].r<=w||x==0){
					if(x==0)
						c[i].x=0;
					else
						c[i].x=x+c[i].r;
					c[i].y=0;
					if(c[i].r>dd){
						dd=c[i].r;
					}
					if(x==0)
						x=c[i].r;
					else
						x+=2*c[i].r;
				}
				else{
					break;
				}
			}
			cerr<<"!"<<dd<<endl;
			x=0;
			d=0;
			for(;i<n;++i){
				if(x+c[i].r<=w||x==0){
					if(x==0)
						c[i].x=0;
					else
						c[i].x=x+c[i].r;
					c[i].y=dd+c[i].r;
					if(2*c[i].r+dd>d){
						d=2*c[i].r+dd;
					}
					if(x==0)
						x=c[i].r;
					else
					x+=2*c[i].r;
				}
				else{
					dd=d;
					x=0;
					--i;
				}
			}
		}
		qsort(c,n,sizeof(W),compare2);
		cout<<"Case #"<<T<<":";
		for(int i=0;i<n;++i){
			cout<<" "<<c[i].x<<" "<<c[i].y;
			if(c[i].y>l)
				cerr<<"?????";
			if(c[i].x>w){
				cerr<<"$$$$";
			}
		}
		cout<<"\n";
	}
	return 0;
}
