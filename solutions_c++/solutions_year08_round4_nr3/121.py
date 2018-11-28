
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set> 
#include<queue>
#include<string>
#include<stack>
#include<sstream>
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it) 
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) cerr << #x << " = "; FOREACH(it,(x)) cerr << *it << ","; cerr << "\n"; 
#define fup(i,a,b) for(int i=a;i<=b;i++)
#define fdo(i,a,b) for(int i=a;i>=b;i--)
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) (int)a.size()
#define inf 1000000000
#define SQR(a) ((a)*(a))
using namespace std;
typedef long long int64;
#define maxn 5555
int pos[maxn][3];
int p[maxn];
double bok[maxn];

int n,cas;
bool moge(double x){
	fup(z,0,1000000){
		fup(i,1,n)bok[i]=p[i]*x;	
		double lx,rx,ly,ry;
		lx=-inf;rx=inf;
		ly=-inf;ry=inf;
		fup(i,1,n){
			double st=bok[i]-abso(z-pos[i][2]);
			double lxx,rxx;
			double x,y;
		//	cout<<i<<" "<<st<<endl;
			x=pos[i][0]-pos[i][1];
			y=pos[i][0]+pos[i][1];
			lxx=x-st;rxx=x+st;
			double lyy,ryy;
			lyy=y-st;ryy=y+st;
			lx=maxi(lx,lxx);
			rx=mini(rx,rxx);
			ly=maxi(ly,lyy);
			ry=mini(ry,ryy);
		}
	if(lx<=rx&&ly<=ry)return 1;	
		
	}	
	return 0;
}
int main(){
	cin>>cas;
	fup(c,1,cas){
		cin>>n;
		fup(i,1,n)cin>>pos[i][0]>>pos[i][1]>>pos[i][2]>>p[i];
		//cout<<moge(3.5)<<endl;
//		return 0;
		double s,e;
		s=0;
		e=1000000;
		fup(i,1,50){
			double q=(s+e)/2;
			if(moge(q)){
				e=q;
			}else{
				s=q;	
			}
		}
		printf("Case #%d: ",c);
		printf("%.6lf\n",s);
	}
	return 0;	
}
