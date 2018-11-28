#include<iostream>
#include<algorithm>
using namespace std;
int value[101][101];
int k;
bool value_ok(int x,int y){
	if(x+y>=k-1 && x+y<=3*(k-1) && x-y>=-(k-1) && x-y<=k-1){
		if(k%2==1){
			if(x%2 == y%2)
				return true;
		}else{
			if(x%2 != y%2)
				return true;
		}
		return false;
	}
	return false;
}
bool same(int x1,int y1,int x2,int y2){
	if(value_ok(x1,y1) && value_ok(x2,y2))
		return value[x1][y1]==value[x2][y2];
	return true;
}
bool ok(int x,int y){
//	if(x!=0 || y!=1)
//		return false;
//	cout<<"ok: x: "<<x<<"y: "<<y<<endl;
	for(int i=0;i<(k*2-1);++i){
		int jj=abs(k-i-1);
		for(int j=0;j<(k-abs(k-1-i));++j,jj+=2){
//			cout<<"  i: "<<i<<"j: "<<jj<<endl;
//			cout<<"  x: "<<x+x-i<<"y: "<<y+y-jj<<endl;
			if(same(i,jj,i,y+y-jj)==false || same(i,jj,x+x-i,jj)==false)
				return false;
		}
	}
	return true;
}
int size(int x,int y){
	int real_size=0;
	for(int i=0;i<(k*2-1);++i){
		int jj=abs(k-i-1);
		for(int j=0;j<(k-abs(k-1-i));++j,jj+=2)
			real_size=max(real_size,abs(x-i)+abs(y-jj));
	}
	real_size+=1;
	return real_size*real_size - k*k;
}
int main(){
	int t;
	cin>>t;
	for(int kk=1;kk<=t;++kk){
		cin>>k;
		for(int i=0;i<(k*2-1);++i){
			int jj=abs(k-i-1);
			for(int j=0;j<(k-abs(k-1-i));++j,jj+=2)
				cin>>value[i][jj];
		}
		int ans=0x7fffffff;
		for(int i=0;i<(k*2-1);++i)
			for(int j=0;j<(k*2-1);++j)
				if(ok(i,j)){
//					cout<<"i: "<<i<<"j: "<<j<<endl;
					ans=min(ans,size(i,j));
//					cout<<"size: "<<size(i,j)<<endl;
				}
		printf("Case #%d: %d\n",kk,ans);
	}
	return 0;
}
