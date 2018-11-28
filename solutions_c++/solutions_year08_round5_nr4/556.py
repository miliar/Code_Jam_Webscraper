/*
ID: imranka1
PROG: test
LANG: C++
*/
#include<iostream>
#include<vector>
#include<algorithm>
#include <fstream>
using namespace std;
#define all(x) (x).begin(),(x).end()

#define vs vector <string>
#define vi vector <int>
#define vvi vector < vi >
#define p(X) push_back((X))

#define fir(i,j,n) for(int (i)=(j);(i)<(n);(i)++)
#define fire(i,j,n) for(int (i)=(j);(i)<=(n);(i)++)
#define firr(i,j,n) for(int (i)=(j);(i)>(n);(i)--)
#define firre(i,j,n) for(int (i)=(j);(i)>=(n);(i)--)
#define tr(v,it) for(typeof(v.begin()) it=v.begin();it!=v.end();it++)

#define srt(v) sort((v).begin(),(v).end())
#define srtc(v) sort(v.begin(),v.end(),cmp)

#define _bc(i) __builtin_popcount(i)
#define INF 0x3f3f3f3f
#define ipow(a,b) (int)pow((double)a,(double)b)
#define fill(a,b) memset(a,b,sizeof(a))
#define maxr(num,a,b) max_element(num.begin()+a,num.begin()+b);
#define minr(num,a,b) min_element(num.begin()+a,num.begin()++b)
#define maxi(v) max_element(all(v))
#define mini(v) min_element(all(v))
#define mod(n)	((n+10007)%10007)
#define cin fin
#define cout fout
int main(){
	ofstream fout("test.out");
    ifstream fin("test.in");
	int cs,n,r,w,h,c,i,j,k,l;
	cin>>n;
	for(cs=1;cs<=n;cs++){
		cin>>h>>w>>r;
		vvi v(r);
		vvi a(h+1, vi (w+1,0));
		fir(i,0,r){
			cin>>k>>l;
			a[k][l]=-1;
			v.resize(v.size()+1);
			v[i].p(k);
			v[i].p(l);
		}
		a[1][1]=1;
		fir(i,1,h+1){
			fir(j,1,w+1){
				if(a[i][j]!=-1&&j>2&&a[i-1][j-2]!=-1)	a[i][j]+=a[i-1][j-2];
				if(a[i][j]!=-1&&i>2&&a[i-2][j-1]!=-1)	a[i][j]+=a[i-2][j-1];
				if(a[i][j]!=-1)				a[i][j]=mod(a[i][j]);
			}
		}
		if(a[h][w]==-1||a[1][1]==-1)	a[h][w]=0;
		cout<<"Case #"<<cs<<": "<<a[h][w]<<endl;
	}
	return 0;
}

