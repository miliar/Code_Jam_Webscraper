#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <cctype>
#include <ctime>
#include <cassert>
#include <cwchar>
#include <cstdarg>
#include <cwctype>
#include <queue>
#include <stack>
#include <algorithm>
#include <list>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <deque>
#include <complex>
#include <string>
#include <functional>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <valarray>
#include <fstream>
using namespace std;

typedef long long int lli;
typedef unsigned int uint;
typedef unsigned char uchar;
typedef unsigned long long ull;

#define REP(i,x) for(int i=0;i<(int)(x);i++)
#define FOR(i,x) for(__typeof((c).begin())i=(c).begin();i!=(c).end();i++)
#define RREP(i,x) for(int i=(x);i>=0;i--)
const double EPS=1e-8;
int dx[4]={-1,0,1,0},dy[4]={0,-1,0,1};
int MAP[10][10];
int W,H,d;
typedef complex<double> Point;
bool solve(int x,int y,int s){
	Point res(0,0);
	Point center((double)x,(double)y);
	if(s&1){
		center+=Point(s/2,s/2);
	}else{
		center+=Point(s/2-.5,s/2-.5);
	}
	int hx=x+s-1,hy=y+s-1;
	for(int xx=x;xx<x+s;xx++){
		for(int yy=y;yy<y+s;yy++){
			if(hx==xx&&yy==hy)continue;
			if(x==xx&&yy==y)continue;
			if(hx==xx&&yy==y)continue;
			if(x==xx&&yy==hy)continue;
			res+=(double)MAP[xx][yy]*(Point(xx,yy)-center);
		}
	}
	//cout<<res.real()<<","<<res.imag()<<endl;
	//if(res.real()<EPS&&res.imag()<EPS)return true;
	if(res==Point(0,0))return true;
	return false;
}
int main(){
	int T;
	cin>>T;
	for(int tcase=1;tcase<=T;tcase++){
		cin>>H>>W>>d;
		for(int i=0;i<H;i++){
			string tmp;
			cin>>tmp;
			for(int j=0;j<W;j++){
				MAP[j][i]=tmp[j]-'0'+d;
			}
		}
		int ans=0;
		for(int i=3;i<=min(W,H);i++){
			for(int x=0;x<=W-i;x++){
				for(int y=0;y<=H-i;y++){
					if(solve(x,y,i)){
						ans=i;
						//cout<<x<<","<<y<<","<<i<<endl;
					}
				}
			}
		}
		if(ans)
			cout<<"Case #"<<tcase<<": "<<ans<<endl;
		else
			cout<<"Case #"<<tcase<<": "<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
