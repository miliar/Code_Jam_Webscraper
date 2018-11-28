#pragma comment(linker,"/STACK:1024000000")
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <memory.h>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <iomanip>
#include <sstream>
#include <stack>
#include <ctime>
#include <cstdlib>
using namespace std;
#define forn(i,n) for(int i=0;i<(n);++i)
#define forv(i,v) forn(i,(int)(v).size())
#define iinf 1000000000
#define linf 1000000000000000000LL
#define dinf 1e200
#define all(v) (v).begin(),(v).end()
#define pb push_back
#define mp make_pair
#define lng long long
#define eps 1e-5
#define EQ(a,b) (fabs((a)-(b))<eps)
#define SQ(a) ((a)*(a))
#define PI 3.14159265359
#define index asdindex
#define FI first
#define SE second
#define prev asdprev
#define PII pair<int,int> 
#define PLL pair<lng,lng> 
#define PDD pair<double,double> 
#define X first
#define Y second
#define unlink asdunlink
#define div asddiv
#define divides asddivides
typedef unsigned char uchar;
typedef unsigned int uint;
inline int mymax(int a,int b){return a<b?b:a;}
inline int mymin(int a,int b){return a>b?b:a;}
inline lng mymax(lng a,lng b){return a<b?b:a;}
inline lng mymin(lng a,lng b){return a>b?b:a;}
inline lng abs(lng a){return a<0?-a:a;}
#ifdef __ASD__
#define LOG(x) cerr<<x<<endl
#else
#define LOG(x)
#endif

bool wall[6100][6100];
bool was[6100][6100];
PII src[11000];
int M;
int n;
int s;
bool bridge,fork;

bool edg[7];
bool corn[7];

const int da[6]={0,0,-1,1,-1,1};
const int db[6]={-1,1,0,0,-1,1};

bool inside(int i,int j){
	return i>0&&j>0&&i<n-1&&j<n-1&&abs(i-j)<s;
}

void dfs2(int a,int b){
	if(!inside(a,b)||was[a][b]||!wall[a][b])
		return;
	was[a][b]=true;
	if(a==1&&b==1)
		corn[0]=true;
	else if(a==1&&b==s)
		corn[1]=true;
	else if(a==s&&b==1)
		corn[2]=true;
	else if(a==n-2&&b==n-2)
		corn[3]=true;
	else if(a==n-2&&b==s)
		corn[4]=true;
	else if(a==s&&b==n-2)
		corn[5]=true;
	else{
		if(a==1)
			edg[0]=true;
		if(b==1)
			edg[1]=true;
		if(a-b==s-1)
			edg[2]=true;
		if(b-a==s-1)
			edg[3]=true;
		if(a==n-2)
			edg[4]=true;
		if(b==n-2)
			edg[5]=true;
	}
	forn(i,6){
		dfs2(a+da[i],b+db[i]);
	}
}

void detect2(){
	memset(was,0,sizeof(was));
	forn(i,n){
		forn(j,n){
			if(!inside(i,j)||was[i][j]||!wall[i][j])
				continue;
			memset(edg,0,sizeof(edg));
			memset(corn,0,sizeof(corn));
			dfs2(i,j);
			int e=0,c=0;
			forn(k,6){
				if(edg[k])
					++e;
				if(corn[k])
					++c;
			}
			if(e>=3)
				fork=true;
			if(c>=2)
				bridge=true;
		}
	}
}

int dsu[6100*6100];

int get(int a){
	return dsu[a]==a?a:dsu[a]=get(dsu[a]);
}

void dfs1(int a,int b,int c){
	if(was[a][b]||wall[a][b])
		return;
	was[a][b]=true;
	dsu[get(a*n+b)]=get(c);
	forn(i,6){
		dfs1(a+da[i],b+db[i],c);
	}
}

int main(){
#ifdef __ASD__
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#endif
    //ios_base::sync_with_stdio(false);

	int tc;
	cin>>tc;
	forn(qqq,tc){
		cerr<<qqq<<endl;
		cin>>s;
		n=s+s+1;
		forn(i,n){
			forn(j,n){
				if(inside(i,j))
					wall[i][j]=false;
				else
					wall[i][j]=true;
			}
		}
		cin>>M;
		forn(i,M){
			cin>>src[i].X>>src[i].Y;
			wall[src[i].X][src[i].Y]=true;
		}

		memset(was,0,sizeof(was));
		forn(i,n*n)
			dsu[i]=i;
		forn(i,n){
			forn(j,n){
				if(inside(i,j)&&(i==1||j==1||i==n-2||j==n-2||abs(i-j)==s-1)&&!wall[i][j]){
					dsu[i*n+j]=0;
					dfs1(i,j,i*n+j);
				}
			}
		}
		int c=0;
		forn(i,n){
			forn(j,n){
				if(inside(i,j)&&!was[i][j]&&!wall[i][j]){
					++c;
					dfs1(i,j,i*n+j);
				}
			}
		}
		int rtime=M+1;
		for(int i=M-1;i>=0;--i){
			if(c)
				rtime=i+1;
			int a=src[i].X;
			int b=src[i].Y;
			wall[a][b]=false;
			++c;
			int p=get(a*n+b);
			forn(d,6){
				int aa=a+da[d];
				int bb=b+db[d];
				if(inside(aa,bb)&&wall[aa][bb])
					continue;
				int q=inside(aa,bb)?get(aa*n+bb):0;
				if(p){
					if(q){
						if(p!=q){
							dsu[q]=p;
							--c;
						}
					}else{
						p=dsu[p]=0;
						--c;
					}
				}else{
					if(q){
						dsu[q]=0;
						--c;
					}
				}
			}
		}
		if(c){
			cerr<<"oops"<<endl;
		}

		int a=0,b=M+1;
		while(b-a>1){
			int c=(a+b)/2;
			forn(i,c){
				wall[src[i].X][src[i].Y]=true;
			}
			bridge=fork=false;
			detect2();
			if(bridge||fork)
				b=c;
			else
				a=c;
			forn(i,c){
				wall[src[i].X][src[i].Y]=false;
			}
		}
		cout<<"Case #"<<qqq+1<<": ";
		if(b==M+1&&rtime==M+1)
			cout<<"none";
		else{
			vector<string> v;
			if(b<=rtime){
				forn(i,b){
					wall[src[i].X][src[i].Y]=true;
				}
				bridge=fork=false;
				detect2();
				if(bridge)
					v.pb("bridge");
				if(fork)
					v.pb("fork");
			}
			if(rtime<=b)
				v.pb("ring");
			forv(i,v){
				if(i)
					cout<<'-';
				cout<<v[i];
			}
			cout<<" in move "<<min(b,rtime);
		}
		cout<<endl;
	}

    return 0;
}
