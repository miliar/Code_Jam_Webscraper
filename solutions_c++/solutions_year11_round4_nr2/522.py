#include <stdio.h>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
using namespace std;

typedef long long LL;
typedef pair<int,int> PI;
typedef pair<LL,LL> PL;
typedef pair<PL,LL> STAN;
typedef vector<int> VI;
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair
#define FT first
#define SD second
#define Y first
#define X second

vector<string>token(string a) {
    vector<string>w;a.push_back(' ');
    while(!a.empty()){w.push_back(a.substr(0,a.find(" ")));a=a.substr(a.find(" ")+1,a.size()-1);}return w;
}

map<string,int> mapik;
vector<string> amapik;
int dodaj(string a) {if(mapik.count(a)==0) {mapik[a]=mapik.size()-1;amapik.PB(a);}return mapik[a];}

#define INF 1000000000

char tmp_str[1000];
string scanf_string() {
	scanf("%s",tmp_str);
	return tmp_str;
}

const int N = 600;
int n,b,m;

char data[N][N];

STAN rzedy[N][N];
STAN kolumny[N][N];

void preprocess() {
	for(int i=0;i<n;i++) {
		LL sumx=0;
		LL sumy=0;
		LL masa=0;
		rzedy[i][0]=MP(MP(sumx,sumy),masa);
		for(int i2=1;i2<=m;i2++) {
			int mass=data[i][i2-1]-'0'+b;
			masa+=mass;
			sumx+=(LL)((i2-1)*2+1)*mass;
			sumy+=(LL)((i)*2+1)*mass;
			rzedy[i][i2]=MP(MP(sumx,sumy),masa);
			//printf("rze i=%d,i2=%d,masa=%I64d sumx = %I64d, sumy = %I64d\n",i,i2,masa,sumx,sumy); 
		}
	}
	
	
	
	for(int i=0;i<m;i++) {
		LL sumx=0;
		LL sumy=0;
		LL masa=0;
		kolumny[i][0]=MP(MP(sumx,sumy),masa);
		for(int i2=1;i2<=n;i2++) {
			int mass=data[i2-1][i]-'0'+b;
			masa+=mass;
			sumx+=(LL)((i)*2+1)*mass;
			sumy+=(LL)((i2-1)*2+1)*mass;
			kolumny[i][i2]=MP(MP(sumx,sumy),masa);
			//printf("kol i=%d,i2=%d,masa=%I64d sumx = %I64d, sumy = %I64d\n",i,i2,masa,sumx,sumy); 
		}
	}

}

STAN wylicz(STAN sumy[][N], int i, int a, int b) {
	STAN res;
	res.SD=sumy[i][b+1].SD-sumy[i][a].SD;
	res.FT.FT=sumy[i][b+1].FT.FT-sumy[i][a].FT.FT;
	res.FT.SD=sumy[i][b+1].FT.SD-sumy[i][a].FT.SD;
	return res;
}

void dodaj(STAN &i, STAN b) {
	i.SD+=b.SD;
	i.FT.FT+=b.FT.FT;
	i.FT.SD+=b.FT.SD;
}

void odejmij(STAN &i, STAN b) {
	i.SD-=b.SD;
	i.FT.FT-=b.FT.FT;
	i.FT.SD-=b.FT.SD;
}

bool ok(STAN s, int y, int x, int k) {
	STAN tmp = s;
	odejmij(tmp,wylicz(rzedy,y,x,x)); // x,y  x,y+k  x+k,y ,x+k,y+k
	odejmij(tmp,wylicz(rzedy,y,x+k-1,x+k-1)); // x,y  x,y+k  x+k,y ,x+k,y+k
	odejmij(tmp,wylicz(rzedy,y+k-1,x,x)); // x,y  x,y+k  x+k,y ,x+k,y+k
	odejmij(tmp,wylicz(rzedy,y+k-1,x+k-1,x+k-1)); // x,y  x,y+k  x+k,y ,x+k,y+k
	s=tmp;
	return s.FT.FT*2 == (2*x+k)*2*s.SD && s.FT.SD*2 == 2*(2*y+k)*s.SD;

}

int main() {
	int d;scanf("%d",&d);
	for(int ind=1;ind<=d;ind++) {
		scanf("%d%d%d",&n,&m,&b);
		b=0;
		for(int i=0;i<n;i++) scanf("%s",data[i]);
		preprocess();
		int best=0;
		for(int i=0;i<=n-3;i++) for(int i2=0;i2<=m-3;i2++){
			STAN stan=MP(MP(0,0),0);
			dodaj(stan,wylicz(rzedy,i,i2,i2+1));
			//printf("i=%d,i2=%d,k=%d,sumax=%I64d sumay=%I64d masa=%I64d\n",i,i2,2,stan.FT.FT,stan.FT.SD,stan.SD);
			dodaj(stan,wylicz(rzedy,i+1,i2,i2+1));
			
			//printf("i=%d,i2=%d,k=%d,sumax=%I64d sumay=%I64d masa=%I64d\n",i,i2,2,stan.FT.FT,stan.FT.SD,stan.SD);
			for(int k=3;k+i<=n;k++) if(i2+k<=m){
				dodaj(stan,wylicz(rzedy,i+k-1,i2,i2+k-1));
				dodaj(stan,wylicz(kolumny,i2+k-1,i,i+k-2));
				//printf("i=%d,i2=%d,k=%d,sumax=%I64d sumay=%I64d masa=%I64d\n",i,i2,k,stan.FT.FT,stan.FT.SD,stan.SD);
				if(ok(stan,i,i2,k)) {
					best = max(best,k);
				}
			}
		}
		
		printf("Case #%d: ",ind);
		if(best!=0) printf("%d\n",best);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
