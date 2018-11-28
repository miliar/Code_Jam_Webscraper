#include<iostream>
using namespace std;

int xx1,xx2,xx3,yy1,yy2,yy3;

double xmult(int x1,int y1,int x2,int y2,int x0,int y0){
	return (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);
}

double area_triangle(int x1,int y1,int x2,int y2,int x3,int y3){
	return xmult(x1,y1,x2,y2,x3,y3);
}



void get(int n,int m,int a){
	xx1=xx2=xx3=yy1=yy2=yy3=-1;

	for(int i1=0;i1<=0;i1++){
		for(int i2=0;i2<=n;i2++){
			for(int i3=i2;i3<=n;i3++){
				if(i3==0)continue;

				for(int j1=0;j1<=m;j1++){
					for(int j2=0;j2<=m;j2++){
						if(j2<j1 && j2!=0)continue;

						for(int j3=j2;j3<=m;j3++){
							if(area_triangle(i1,j1,i2,j2,i3,j3)==a){
								xx1=i1;
								xx2=i2;
								xx3=i3;

								yy1=j1;
								yy2=j2;
								yy3=j3;

								return;
							}
						}
					}
				}
			}
		}
	}
}

void solve(int c){
	int n,m,a;
	cin>>n>>m>>a;

	cout<<"Case #"<<c<<":";
	get(n,m,a);

	if(xx1==-1)cout<<" IMPOSSIBLE\n";
	else cout<<" "<<xx1<<" "<<yy1<<" "<<xx2<<" "<<yy2<<" "<<xx3<<" "<<yy3<<endl;
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);


	int C;
	cin>>C;


	for(int c=1;c<=C;c++)
		solve(c);
}