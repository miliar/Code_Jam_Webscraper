
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set> 
#include<queue>
#include<string>
#include<stack>
#include<sstream>
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it) 
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) cerr << #x << " = "; FOREACH(it,(x)) cerr << *it << ","; cerr << "\n"; 
#define fup(i,a,b) for(int i=a;i<=b;i++)
#define fdo(i,a,b) for(int i=a;i>=b;i--)
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) (int)a.size()
#define inf 1000000000
#define SQR(a) ((a)*(a))
using namespace std;
typedef long long int64;
#define maxn 200 
char co[maxn][maxn];


//PRZETESTOWANE NA MIPT
///////////////////////////////////////////
#define maxA 10000
#define maxB 10000

vector<int> T[maxA];
int ktoA[maxA];
int ktoB[maxB];
bool bylo[maxA];

struct max_skoj{

	int A,B;
	max_skoj(int a,int b){
		A=a;B=b;fup(i,0,A)T[i].clear();fup(i,0,A)ktoA[i]=-1;fup(i,0,B)ktoB[i]=-1;
	}
	void add_edge(int a,int b){

		//cout<<"ADD "<<a<<" "<<b<<endl;
		T[a].PB(b);
	}

	bool dfs(int act){
		bylo[act]=1;
		fup(i,0,siz(T[act])-1){
			int k=T[act][i];
			if(ktoB[k]==-1||(!bylo[ktoB[k]]&&dfs(ktoB[k]))){
				ktoA[act]=k;
				ktoB[k]=act;
				return 1;	
			}
		}
		return 0;
	}

	int get_skoj(){
		int skoj=0;
		while(1){
			bool ok=0;
			memset(bylo,0,sizeof(bylo));
			fup(i,0,A){
				if(bylo[i]||(ktoA[i]!=-1))continue;
				if(dfs(i)){ok=1;skoj++;}
			}
			if(!ok)break;
		}	


		return skoj;
	}
};

////////////////////////////////////////////
int numer[100][100];
int h,w;
int main(){
	int cas;
	cin>>cas;
	fup(c,1,cas){
		cin>>h>>w;
		memset(numer,0,sizeof(numer));
		fup(i,1,h)fup(j,1,w){
			cin>>co[i][j];
		}
		int a,b;
		a=0;b=0;	
		fup(i,1,h){
			fup(j,1,w){
				if(co[i][j]=='x')continue;
				if(j%2==1){
					a++;numer[i][j]=a;	
				}else{
					b++;numer[i][j]=b;
				}
			}
		}
		max_skoj skoj(a+4,b+4);
		fup(i,1,h){
			fup(j,1,w){
				if(co[i][j]=='x')continue;
				bool colo=j%2;
				if(colo==1){
						if(numer[i-1][j-1])skoj.add_edge(numer[i][j],numer[i-1][j-1]);
						if(numer[i][j-1])skoj.add_edge(numer[i][j],numer[i][j-1]);
						if(numer[i][j+1])skoj.add_edge(numer[i][j],numer[i][j+1]);
						if(numer[i-1][j+1])skoj.add_edge(numer[i][j],numer[i-1][j+1]);
						if(numer[i+1][j+1])skoj.add_edge(numer[i][j],numer[i+1][j+1]);
						if(numer[i+1][j-1])skoj.add_edge(numer[i][j],numer[i+1][j-1]);
				}

			}
		}	
		int wie=a+b;
		int sk=skoj.get_skoj();

//	cout<<"a "<<a<<" b "<<b<<" sk "<<sk<<endl;
		int maxi=wie-sk;
		printf("Case #%d: %d\n",c,maxi);
	}
	return 0;	
}
