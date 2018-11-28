
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
#define stala 3005
string opis;
int nx[]={1,0,-1,0};
int ny[]={0,1,0,-1};
char jest[stala*2+4][stala*2+4];
char str[40];
int main(){
	int cas;
	cin>>cas;
	fup(c,1,cas){
		int par;
		opis.clear();
		cin>>par;	
		memset(jest,0,sizeof(jest));
		fup(i,1,par){
			int ile;
			scanf("%s%d",str,&ile);
			string a(str);
	//		cin>>a>>ile;
			fup(i,1,ile)opis+=a;
		}
		int dir=0;
		int x,y;
		x=stala;y=stala;
		int mini=inf;
		int mdir=0;
		
		fup(i,0,siz(opis)-1){
			char c=opis[i];
			if(c=='R'){dir=(dir+1)%4;continue;}
			if(c=='L'){dir=(dir-1+4)%4;continue;}
			if(c=='F'){
				if(y<mini&&(dir%2==0)){mini=y;mdir=dir;}
				x+=nx[dir];y+=ny[dir];
			}
		}
		if(mdir==2){
			fup(i,0,siz(opis)-1){
				if(opis[i]=='L'){opis[i]='R';continue;}
				if(opis[i]=='R'){opis[i]='L';continue;}
			}
		}

		fup(i,0,siz(opis)-1){
			char c=opis[i];
			if(c=='R'){dir=(dir+1)%4;continue;}
			if(c=='L'){dir=(dir-1+4)%4;continue;}
			if(c=='F'){
				if(dir==0)jest[x][y]=1;
				if(dir==1)jest[x-1][y]=1;
				if(dir==2)jest[x-1][y-1]=1;
				if(dir==3)jest[x][y-1]=1;

				x+=nx[dir];y+=ny[dir];}		
		}
		queue<pair<int,int> > Q;
		Q.push(MP(0,0));
		while(!Q.empty()){
			int x,y;
			x=Q.front().FI;
			y=Q.front().SE;
			Q.pop();
			jest[x][y]=-1;
			fup(i,0,3){
				int xx,yy;xx=nx[i]+x;yy=ny[i]+y;
				if(xx<0||yy<0||xx>stala*2||yy>stala*2)continue;
				if(jest[xx][yy]!=0)continue;
				Q.push(MP(xx,yy));
				jest[xx][yy]=-1;
			}	
		}
//		cout<<"DONE "<<endl;
		int suma=0;
		fup(i,0,2*stala){
			int l,r;
			l=inf;r=-inf;
			fup(j,0,2*stala)if(jest[i][j]==1){l=mini(l,j);r=maxi(r,j);}			
			if(l==inf)continue;
//			cout<<"H "<<i-stala<<" "<<l-stala<<" "<<r-stala<<endl;
			fup(j,l,r){
				if(jest[i][j]==-1){jest[i][j]=2;suma++;}
			}
		}
		fup(j,0,2*stala){
			int dol,gora;
			dol=inf;gora=-inf;
			fup(i,0,2*stala)if(jest[i][j]==1){dol=mini(dol,i);gora=maxi(gora,i);}
			if(dol==inf)continue;
			fup(i,dol,gora){
				if(jest[i][j]==-1){jest[i][j]=2;suma++;}
			}
		}
		printf("Case #%d: %d\n",c,suma);
	}
	return 0;	
}
