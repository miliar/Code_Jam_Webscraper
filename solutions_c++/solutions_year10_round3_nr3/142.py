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



void convert(string &s,VI &v){
	int num;
	for(int i=0;i<s.size();i++){
		if(s[i]<='9') num=s[i]-'0';
		else num=s[i]-'A'+10;
//		cerr<<num<<' ';
		for(int j=3;j>=0;j--){
			v[i*4+j]=num%2;
			num/=2;
		}
	}
}

int main() {
	ifstream fin("C-small.in");
	ofstream fout("C-small.out");
	long long tests,N,M;
	fin>>tests;
	for(int t=1;t<=tests;t++){
		fin>>N>>M;
		VVI v(N, VI(M));
		for(int i=0;i<N;i++){
			string s;
			fin>>s;
			convert(s,v[i]);
		}
/*		for(int i=0;i<N;i++){
			for(int j=0;j<M;j++) cerr<<v[i][j];
			cerr<<endl;
		}
*/		VVI w(N, VI(M));
		int cont=N*M;
		vector<int> TAU(min(N,M)+1);
		while(cont){
			for(int i=0;i<N;i++) for(int j=0;j<M;j++) w[i][j]=0;
			for(int i=N-1;i>=0;i--) if(v[i][M-1]!=-1) w[i][M-1]=1;
			for(int j=M-1;j>=0;j--) if(v[N-1][j]!=-1) w[N-1][j]=1;
			for(int i=N-2;i>=0;i--){
				for(int j=M-2;j>=0;j--){
					if(v[i][j]==-1) continue;
					if(v[i][j]!=v[i+1][j] && v[i][j]!=v[i][j+1]){
						w[i][j]=min(w[i+1][j],w[i][j+1]);
						if(w[i+1][j]!=w[i][j] || (i+w[i][j]<N && j+w[i][j]<M && v[i][j]==v[i+w[i][j]][j+w[i][j]])) w[i][j]++;
					}
					else w[i][j]=1;
				}
			}
			int maxim=w[0][0],x=0,y=0;
			for(int i=0;i<N;i++){
				for(int j=0;j<M;j++){
					if(w[i][j]>maxim){
						maxim=w[i][j];
						x=i;
						y=j;
					}
				}
			}
			TAU[maxim]++;
			cont-=(maxim*maxim);
			for(int i=x;i<x+maxim;i++)	for(int j=y;j<y+maxim;j++) v[i][j]=-1;
/*			cerr<<cont<<' '<<x<<' '<<y<<endl;
			for(int i=0;i<N;i++){
				for(int j=0;j<M;j++) cerr<<v[i][j]<<' ';
				cerr<<endl;
			}
			system("pause");
*/		}
		int res=0;
		for(int i=1;i<TAU.size();i++) if(TAU[i]) res++;
		fout<<"Case #"<<t<<": "<<res<<endl;
		for(int i=TAU.size()-1;i>0;i--) if(TAU[i]) fout<<i<<' '<<TAU[i]<<endl;
	}
	system("pause");
}
