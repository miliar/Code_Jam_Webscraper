#include <map> 
#include <set> 
#include <queue> 
#include <bitset> 
#include <valarray> 
#include <complex> 
#include <iostream> 
#include <sstream> 
#include <cmath> 
#include <algorithm> 
#include <string> 
#include <cassert> 

using namespace std;

// prewritten code

#define Size(x) (int)(x).size()
#define For(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define Ford(i,a,b) for(int i=(int)(a);i>=(int)(b);--i) 
#define RepV(i,v) for (int i=0;i<Size(v);++i)
#define All(c) (c).begin(),(c).end()
#define Fill(a,b) memset(&a,b,sizeof(a))
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
#define Abs(a) ((a)<0?-(a):(a))
#define VVI vector<vector<int> >
#define VI vector<int>
#define VVS vector<vector<string> >
#define VS vector<string>
#define ForEach(it,a) for (typeof((a).begin()) it=(a).begin(); it!=(a).end(); ++it)
#define DBG(x) cout << #x <<" = "<< x << endl;
#define DBGA(x) {cout << #x <<": "; for (int i=0; i<(int)sizeof(x)/(int)sizeof(x[0]); ++i) cout<<x[i]<<' '; cout<<endl;}
#define DBGV(x) {cout << #x <<": "; for (int i=0; i<(int)Size(x); ++i) cout<<x[i]<<' '; cout<<endl;}

const string problem_name = "B-large";

struct state {
	state(int H, int M, int Type){h=H;m=M;type=Type;}
	int h, m, type;
	bool operator < (const state other) const{
		if (h!=other.h) return h<other.h;
		if (m!=other.m) return m<other.m;
		return type < other.type;
	}
};

int main(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
	
	int t;
	scanf("%d",&t);
	
	For(z,1,t){
		printf("Case #%d: ",z);
		vector<state> A, B;
		int t, na, nb;
		scanf("%d%d%d",&t,&na,&nb);
		For(i,1,na) {
			int h1, m1, h2, m2;
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			A.push_back(state(h1,m1,1));
			B.push_back(state(h2,m2,0));
		}
		For(i,1,nb) {
			int h1, m1, h2, m2;
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			B.push_back(state(h1,m1,1));
			A.push_back(state(h2,m2,0));
		}
		int rA = 0, rB = 0;
		sort(All(A));
		sort(All(B));

		vector <state> buf;
		RepV(i,A) {
			if (A[i].type == 0) {
				int hh = A[i].h, mm=A[i].m+t;
				if (mm>=60) {
					++hh;
					mm%=60;
				}
				if (hh<=23) buf.push_back(state(hh,mm,0));
			} else {
				int k=-1;
				RepV(j,buf) if (buf[j].h<A[i].h || (buf[j].h==A[i].h && buf[j].m <= A[i].m)) {k=j; break;}
				if (k==-1) ++rA;
				else buf.erase(buf.begin()+k);
			}
		}
		buf.clear();
		RepV(i,B) {
			if (B[i].type == 0) {
				int hh = B[i].h, mm=B[i].m+t;
				if (mm>=60) {
					++hh;
					mm%=60;
				}
				if (hh<=23) buf.push_back(state(hh,mm,0));
			} else {
				int k=-1;
				RepV(j,buf) if (buf[j].h<B[i].h || (buf[j].h==B[i].h && buf[j].m <= B[i].m)) {k=j; break;}
				if (k==-1) ++rB;
				else buf.erase(buf.begin()+k);
			}
		}
		printf("%d %d\n",rA,rB);
	}

	return 0;
}
