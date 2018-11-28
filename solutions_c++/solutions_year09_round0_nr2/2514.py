#include<iostream>
#include<vector>
#include<cassert>
using namespace std;
typedef vector<vector<int> > array2d;
array2d init2d(int w,int h,int v=0){
	return vector<vector<int> >(h,vector<int>(w,v));
}

void boundary(array2d& a){
	const int w = a[0].size()-2;
	const int h = a.size()-2;
	for(int x=1;x<=w;x++){
		a[0][x]=a[1][x];
		a[h+1][x]=a[h][x];
	}
	for(int y=1;y<=h;y++){
		a[y][0]=a[y][1];
		a[y][w+1]=a[y][w];
	}
}
void boundary(array2d& a,int v){
	const int w = a[0].size()-2;
	const int h = a.size()-2;
	for(int x=1;x<=w;x++){
		a[0][x]=v;
		a[h+1][x]=v;
	}
	for(int y=1;y<=h;y++){
		a[y][0]=v;
		a[y][w+1]=v;
	}
}

int pset(int x,int y,int ch,array2d& alt,array2d& ret){
	// 確定済みか
	if(ret[y][x]>0){
//		assert(!"error");
		return ch;
	}

	// 4方向のうち最も低いcellとその方向を求める
	int minvecy=-1,minvecx=0,mincell=alt[y-1][x];
	if(mincell>alt[y][x-1]){ minvecy= 0;minvecx=-1;mincell=alt[y][x-1]; }
	if(mincell>alt[y][x+1]){ minvecy= 0;minvecx=+1;mincell=alt[y][x+1]; }
	if(mincell>alt[y+1][x]){ minvecy= 1;minvecx= 0;mincell=alt[y+1][x]; }

	// となりが自分より高い場合
	if(alt[y][x]<=alt[y+minvecy][x+minvecx]){
		//自分を塗って帰る
		return ret[y][x]=ch;
	}

	// となりが確定していないとき
	if(ret[y+minvecy][x+minvecx]<=0){
		// となりを塗って返る
		int c=pset(x+minvecx,y+minvecy,ch,alt,ret);
		ret[y][x]=c;
		return c;
	}

	// となりが確定しているとき、隣の色で自分を塗り帰る
	else {
		ret[y][x]=ret[y+minvecy][x+minvecx];
		return ret[y][x];
	}

	return ch;
}

void print(const array2d& a){
	const int w = a[0].size()-2;
	const int h = a.size()-2;
	for(int y=1;y<=h;y++){
		cout<<(y==1?"":"\n");
		for(int x=1;x<=w;x++){
			cout<<(x==1?"":" ")<<char(a[y][x]);
		}
	}
}

array2d paint(array2d alt){
	const int w = alt[0].size()-2;
	const int h = alt.size()-2;
	array2d ret=init2d(w+2,h+2,0);
	boundary(ret,1);

	int c='a';
	for(int y=1;y<=h;y++){
		for(int x=1;x<=w;x++){
			if(ret[y][x]<=0){
				c=pset(x,y,c,alt,ret)+1;
			}
		}
	}
	return ret;
}


int main() {
	int T;cin>>T;
	for(int t=1;t<=T;t++){
		int W,H;cin>>H>>W;
		array2d alt=init2d(W+2,H+2);
		for(int y=1;y<=H;y++){
			for(int x=1;x<=W;x++){
				cin>>alt[y][x];
			}
		}
		boundary(alt);
		array2d ret=paint(alt);

		cout<<"Case #"<<t<<":\n";
		print(ret);
		cout<<endl;
	}
	return 0;
}
