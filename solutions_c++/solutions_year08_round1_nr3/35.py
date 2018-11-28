#include <iostream>
#include <vector>
#include <cmath>
#include <map>
using namespace std;
#define fu(i,m,n) for(int i=m; i<n; i++)

int iden[]={1,0,0,1};
int matt[]={6,1,-4,0};
int stt[]={28,6,6,2};
vector<int> mat(matt,matt+4);
vector<int> pows[1000];
vector<int> st(stt,stt+4);

vector<int> mult(const vector<int>& a, const vector<int>& b) {
	vector<int> ret(4);
	ret[0] = (a[0]*b[0]+a[1]*b[2]+1000000)%1000;
	ret[1] = (a[0]*b[1]+a[1]*b[3]+1000000)%1000;
	ret[2] = (a[2]*b[0]+a[3]*b[2]+1000000)%1000;
	ret[3] = (a[2]*b[1]+a[3]*b[3]+1000000)%1000;
	return ret;
}

vector<int> matpow(const vector<int>& x, long long n) {
	if(n==0) return vector<int>(iden,iden+4);
	if(n==1) return x;
	vector<int> ret(iden,iden+4);
	fu(i,0,50) if(n&(1LL<<i)) ret=mult(ret,pows[i]);
	/*fu(i,0,n) {
		ret = mult(ret, x);
	}*/
	return ret;
}

int main(void) {
	int T;
	/*fu(i,0,20) {
		double a=pow(3+sqrt(5),i), b=pow(3-sqrt(5),i);
		cout << a << " " << b << " " << a+b << endl;
	}*/
	//val[0]=2;
	//val[1]=6;
	cin >> T;
	pows[0]=mat;
	fu(i,0,200) pows[i+1]=mult(pows[i],pows[i]);
	fu(ts,1,T+1) {
		map<string,int> engines;
		cout << "Case #" << ts << ": ";
		int N;
		cin >> N;
		int ret;
		int a=2, b=6, c;
		/*fu(i,0,4) {
			fu(j,0,4) cout << mult(st,matpow(mat,i))[j] << " ";
			cout << endl;
		}*/
		//fu(i,1,N) c=(6*b-4*a+10000)%1000, a=b, b=c;
		b=mult(st,matpow(mat,N))[3];
		printf("%03d\n",b-1);
	}
}
