#include <fstream>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#define debug(x) cout<<#x<<' '<<x<<endl;
#define INF 1000000
#define MAXN 1000000
#define forn(i,n) for(int i=0; i<(int)(n); i++)
using namespace std;

vector <int>v;
int res=0;


int main(){
	ifstream in("b.in");
	ofstream out("b.out");
	long long T, w=0, a, b, l, c, p;
	in>>T;
	//out<<T<<endl;
	while(w<T){
		w++;
		in>>l>>p>>c;
		int cont=0;
		//out<<l<<' '<<p<<' '<<c;
		while(l*c<p ){
			a=l; b=0;
			while(a<p){
				a*=c*c; b++;
				}
			while(b>0){b--; a/=c;}
			p=a;
			cont++;
			//out<<l<<' '<<p<<endl;
			}
		out<<"Case #"<<w<<": ";
		out<<cont<<endl;
		}
}

