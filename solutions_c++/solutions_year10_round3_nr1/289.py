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
	ifstream in("a.in");
	ofstream out("a.out");
	int T, n, w=0, a, b;
	in>>T;
	//out<<T<<endl;
	while(w<T){
		w++;
		res=0;
		in>>n;
		v.clear();
		forn(i,n){
			in>>a>>b;
			v.push_back(a);
			v.push_back(b);
			}
		for(int i=0; i<2*n; i+=2){
			for(int j=i+2; j<2*n; j+=2){
				if(v[i]>v[j] && v[i+1]<v[j+1])res++;
				if(v[i]<v[j] && v[i+1]>v[j+1])res++;
				}
			}
		out<<"Case #"<<w<<": ";
		out<<res<<endl;
		}
}

