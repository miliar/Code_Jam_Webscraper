#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <climits>
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
#include <iomanip>
#include <sstream>
#include <bitset>
#include <valarray>
#include <iterator>
using namespace std;

typedef long long int lli;
typedef unsigned int uint;
typedef unsigned char uchar;
typedef unsigned long long ull;

#define REP(i,x) for(int i=0;i<(int)(x);i++)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();i++)
#define RREP(i,x) for(int i=(x);i>=0;i--)
#define RFOR(i,c) for(__typeof((c).rbegin())i=(c).rbegin();i!=(c).rend();i++)

int dx[4]={-1,0,1,0},dy[4]={0,-1,0,1}; //ç∂ è„ âE â∫

const int INF=0x20000000;
const double EPS=1e-8;

int W,H;
int N;
int r[10000];
double resx[10000],resy[10000];
int resc;
typedef pair<int,int> P;
P in[10000];
bool check(double x,double y,double R){
	REP(i,resc){
		if((x-resx[i])*(x-resx[i])+(y-resy[i])*(y-resy[i])>=(R+r[i]+1)*(R+r[i]+1)+EPS){
		}else{

			return false;
		}
	}
	return true;
}
uint32_t xor128(void) {
	static uint32_t x = 123456789;
	static uint32_t y = 362436069;
	static uint32_t z = 521288629;
	static uint32_t w = 88675123;
	uint32_t t;

	t = x ^ (x << 11);
	x = y; y = z; z = w;
	return w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));
}
void solve(){
	//
	do{
		bool ok=true;

		for(resc=0;resc<N;resc++){
			bool tok=false;
			for(int i=0;i<10;i++){
	//			cout<<resc<<endl;
				double x=xor128()/4294967296.0*W;
				double y=xor128()/4294967296.0*H;
	//			cout<<x<<","<<y<<endl;
				if(resc==0){
					x=0;y=0;
				}
				if(resc==1){
					x=W;y=H;
				}
				if(!check(x,y,r[resc])){
					continue;
				}
				resx[resc]=x;
				resy[resc]=y;
				tok=true;
				break;
			}
			if(!tok){
				ok=false;
				break;
			}
		}
		if(ok){
			vector<double> rx(N),ry(N);
			REP(i,N){
				rx[in[i].second]=resx[i];
				ry[in[i].second]=resy[i];
			}
			for(int i=0;i<N;i++){
				cout<<setprecision(8);
				cout<<setiosflags(ios::fixed);
				cout<<" "<<rx[i]<<" "<<ry[i];
			}
			cout<<endl;
			return;
		}
	}while(true);
}
int main(){
	int TestCaseCount;
	cin>>TestCaseCount;
	for(int tc=1;tc<=TestCaseCount;tc++){
		cin>>N>>W>>H;
		for(int i=0;i<N;i++){
			cin>>r[i];
			in[i].first=r[i];
			in[i].second=i;
		}
		sort(in,in+N);
		reverse(in,in+N);

		sort(r,r+N);
		reverse(r,r+N);


		cout<<"Case "<<"#"<<tc<<":";
		solve();
	}
}
