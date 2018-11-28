#include<iostream>
#include<string>
using namespace std;
int fa[102][102][2];
int a[102][102];
char r[102][102];
int min(int a,int b)
{
	if(a<b)return a;else return b;
}
void getfa(int x,int y)
{
	if(fa[x][y][0]!=0)return;
	int px,py;
	int m=min(min(a[x-1][y],a[x+1][y]),min(a[x][y-1],a[x][y+1]));
	if(m>=a[x][y]){
		fa[x][y][0]=x;
		fa[x][y][1]=y;
		return;
	}
	if(a[x-1][y]==m){
		px=x-1;py=y;
	}else if(a[x][y-1]==m){
		px=x;py=y-1;
	}else if(a[x][y+1]==m){
		px=x;py=y+1;
	}else if(a[x+1][y]==m){
		px=x+1;py=y;
	}
	getfa(px,py);
	fa[x][y][0]=fa[px][py][0];
	fa[x][y][1]=fa[px][py][1];
}
int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	const int max=10001;
	int t,h,w,x,y;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>h>>w;
		for(x=0;x<=h+1;x++)
			a[x][0]=a[x][w+1]=max;
		for(y=0;y<=w+1;y++)
			a[0][y]=a[h+1][y]=max;
		for(x=1;x<=h;x++)
			for(y=1;y<=w;y++)
				cin>>a[x][y];
		memset(fa,0,sizeof(fa));
		for(x=1;x<=h;x++)
			for(y=1;y<=w;y++)
				getfa(x,y);
		memset(r,0,sizeof(r));
		char ch='a';
		for(x=1;x<=h;x++)
			for(y=1;y<=w;y++){
				int px=fa[x][y][0];
				int py=fa[x][y][1];
				if(r[px][py]==0){
					r[px][py]=ch;
					ch++;
				}
				r[x][y]=r[px][py];
			}
		
		cout<<"Case #"<<i+1<<":"<<endl;
		for(x=1;x<=h;x++){
			for(y=1;y<w;y++)cout<<r[x][y]<<" ";
			cout<<r[x][w]<<endl;
		}

	}

	return 0;
}