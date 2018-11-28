//Done by Grey Matter
//Fet per Ferran Alet

#include<iostream>
#include<cmath>
#include<iomanip>
#include<vector>
#include<map>
#include<queue>
#include<fstream>
#include<algorithm>
#include<string>
#include<stack>
#include<numeric>
#include<set>
#include<sstream>

#define INF 2147483647
#define LINF 1000000000000000000LL
#define EPS 1e-9
#define debug(x) cerr << #x << " = " << x << endl
#define FORN(x,y) for(int x=0;x<y;x++)
#define FORU(x,y) for(int x=1;x<=y;x++)
using namespace std;


typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<string> VS;
typedef map<int,int> MII;
typedef MII::iterator iMII;
typedef long long ll;

int powers[]={1,2,4,8,16,32,64,128,256,512,1024,2048,4096};

VI T;
VB M;
int res,p;

ifstream fin("Bsmall.in");
ofstream fout("Bsmall.out");

void actualitza(int pos){
	if(pos>=p){
		while(pos){
			T[pos]--;
			pos/=2;
		}
		T[0]--;
	}
	else{
		if(T[pos*2]) actualitza(pos*2);
		if(T[pos*2+1]) actualitza(pos*2+1);
	}
}

void compra(int pos){
	if(pos>=p && T[pos]) actualitza(pos);
	else{
		if(M[pos]) {
			M[pos]=false;
//			cerr<<"Compro: "<<pos<<endl;
			actualitza(pos);
		}
		else{
			if(T[pos*2]) compra(pos*2);
			else compra(pos*2+1);
		}
	}
}

int main() {
	int cases;
	fin>>cases;
	for(int cas=1;cas<=cases;cas++){
		debug(cas);
		fin>>p;
		int pp=p;
		p=powers[p];
		T= VI(2*p);
		debug(p);
		for(int i=0;i<p;i++) {
			fin>>T[i+p];
			T[i+p]=pp-T[i+p];
		}
//		system("pause");
		int a;
		pp=p/2;
		while(pp){
			for(int i=0;i<pp;i++) fin>>a;
			pp/=2;
		}
//		system("pause");
		for(int i=0;i<T.size();i++) cerr<<T[i]<<' ';
		cerr<<endl;
		for(int j=(2*p)-1;j>0;j--) T[int(j/2)]+=T[j];
		for(int i=0;i<T.size();i++) cerr<<T[i]<<' ';
		cerr<<endl;
		M= VB(2*p,true);
		res=0;
		while(T[1]) {
//			for(int i=0;i<T.size();i++) cerr<<T[i]<<' ';
//			cerr<<endl;
			compra(1);
			res++;
		}
		fout<<"Case #"<<cas<<": "<<res<<endl;
	}
	system("pause");
}
