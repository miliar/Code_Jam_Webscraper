#include<iostream>
#include<vector>
#include<string.h>
#include<stdio.h>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<math.h>
#include<limits.h>
using namespace std;
#define rp(i,a,b) for(int i = (a); i < (b); i++)
#define rrp(i,a,b) for(int i = (b); i >= (a); i--)
#define ri(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define C(x,with) memset(x,with,sizeof(x))
#define S(v) (v).size()
#define ll long long int
#define ii pair<int,int>

void op(int t){
	cout << "Case #" << t << ": ";
}

int main()

{

	char a[200][200];
	int test;
	cin >>	test;
	rp(t,1,test+1){
	
	int n;
	cin >> n;
	rp(i,0,n)
		rp(j,0,n)
			cin >> a[i][j];	
	double w[n];
	double l[n];
	rp(i,0,n) w[i]=0.0,l[i]=0.0;
	rp(i,0,n){
		double x =0 , y=0;
			rp(j,0,n){
				if(a[i][j]=='0') y += 1.0;
				if(a[i][j]=='1') x += 1.0;	
			}	
		w[i]=x;l[i]=y;	
	}
//	rp(i,0,n)
//		w[i] /= 2.0 , l[i] /= 2.0;	
	
	double f[n];
	
	rp(i,0,n){
		double res = 0.0;
		double cnt = 0.0;
		rp(j,0,n){
			if(a[i][j]=='1')	res += (w[j])/(w[j] + l[j] - 1);
			if(a[i][j]=='0')	res += (w[j]-1)/(w[j] + l[j] - 1);
			if(a[i][j]!='.') cnt += 1.0;
		}
		f[i] = res / cnt ;
	}
	//rp(i,0,n)
	//	cout << f[i] << "\n";
	double ans[n];
	rp(i,0,n) ans[i] = 0.0;
	rp(i,0,n){
		double res = 0.0;
		res += (w[i] / (w[i] + l[i])) * 0.25;
		res += f[i] * 0.50;
		double res1 = 0.0;
		double cnt = 0.0;
		rp(j,0,n){
			if(a[i][j] != '.') {res1 += f[j]; cnt += 1.0 ; }	
		}
		res += (res1 / cnt) * 0.25;
		ans[i] = res;
	}	
	op(t);cout << "\n";
	rp(i,0,n)
		cout << ans[i] << "\n";
	//cout << "\n\n";
	}
	return 0;
}
