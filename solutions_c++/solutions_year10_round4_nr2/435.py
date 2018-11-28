#include <fstream>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <string>
//#include <BigIntegerLibrary.hh>

#define debug(x) cout<<#x<<' '<<x<<endl;
#define INF 1000000
#define MAXN 1000000
#define forn(i,n) for(int i=0; i<(int)(n); i++)
using namespace std;
vector<int> v;
long long mej[1024][1024][11];
long long cst[1024][1024];
int P;

long long solve(int x, int y, int perd){
	if(mej[x][y][perd]!=-1)return mej[x][y][perd];
	
	if(x+1==y){
		int k=min(v[x], v[y]);
		if(k<perd)return -1;
		if(k==perd){mej[x][y][perd]=cst[x][y]; return cst[x][y];}
		if(k>perd){mej[x][y][perd]=0; return 0;}
		}
	
	long long mn=-1;
	long long p1, p2, p3, p4;
	p1= solve(x, (x+y-1)/2, perd);
	p2= solve((x+y+1)/2, y, perd);
	p3= solve(x, (x+y-1)/2, perd+1);
	p4= solve((x+y+1)/2, y, perd+1);
	
	if(p1!=-1 && p2!=-1)mn=p1+p2+cst[x][y];
	if(mn==-1){
		if(p3!=-1 && p4!=-1)mn=p3+p4;
		}
	else{
		if(p3!=-1 && p4!=-1)mn=min(mn,p3+p4);
		}
	mej[x][y][perd]=mn;
	return mn;
	}

int main(){
	ifstream in("b.in");
	ofstream out("b.out");
	int T, w=0;
	int a; 
	in>>T;

	while(w<T){
		w++;
		v.clear();
		forn(i,1024)forn(j,1024)forn(k,11)mej[i][j][k]=-1;
		//forn(i,1024)forn(j,1024)cst[i][j]=-1;
		in>>P;
		//out<<(1<<P)<<endl;
		forn(i,(1<<P)){in>>a;v.push_back(a);}
		int p=P;
		int pw=1;
		forn(i,P){
			p--;
			pw*=2;
			int nxt=0;
			forn(j, (1<<p)){
				in>>a;
				cst[nxt][nxt+pw-1]=a;
				nxt+=pw;
				}
			}
		/*
		forn(i,10){
			forn(j,10)out<<cst[i][j]<<' ';
			out<<endl;
			}
		out<<endl;
		*/
		long long res=solve(0, (1<<P)-1, 0);
		out<<"Case #"<<w<<": ";
		out<<res<<endl;
		}
}

