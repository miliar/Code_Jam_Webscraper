#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

long long n,A,B,C,D,x0,y0,M;
long long a[3][3],b[3][3];

void push(const long long& X,const long long& Y){
	a[X%3][Y%3]++;
}

void gen(){
	memset(a,0,sizeof(a));
	long long X=x0,Y=y0;
	push(X,Y);
	for (int i=1;i<n;i++){
		X=(A*X+B)%M;
		Y=(C*Y+D)%M;
		push(X,Y);
	}
}

long long ans;

bool notsame(int x,int y,int xx,int yy){
	return (x!=xx||y!=yy);
}

void work(){
	ans=0;
	memset(b,0,sizeof(b));
	for (int i=0;i<3;i++)
	for (int j=0;j<3;j++)
	for (int x=0;x<3;x++)
	for (int y=0;y<3;y++)
	for (int n=0;n<3;n++)
	for (int m=0;m<3;m++){
		int temp=b[0][0];
		if (notsame(i,j,x,y)&&notsame(i,j,n,m)&&notsame(x,y,n,m))
			b[(i+x+n)%3][(j+y+m)%3]+=a[i][j]*a[x][y]*a[n][m];
		else if (!notsame(i,j,x,y)&&!notsame(i,j,n,m)&&!notsame(x,y,n,m))
			b[(i+x+n)%3][(j+y+m)%3]+=a[i][j]*(a[x][y]-1)*(a[n][m]-2);
		else{
			if (!notsame(i,j,x,y))
				b[(i+x+n)%3][(j+y+m)%3]+=a[i][j]*(a[x][y]-1)*a[n][m];
			else
				b[(i+x+n)%3][(j+y+m)%3]+=a[i][j]*a[x][y]*(a[n][m]-1);
		}
	}
	ans=b[0][0]/6;
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int Q,Num=0;
	cin >> Q;
	while (Q--){
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		gen();
		work();
		Num++;
		cout << "Case #" << Num << ": " << ans << endl;
	}
	return 0;
}