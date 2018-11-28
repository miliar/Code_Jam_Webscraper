#include <stdio.h>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
using namespace std;

typedef long long LL;
typedef pair<int,int> PI;
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

const int N = 1000;
int n,r,c;
char mapa[100][100];

int dasie(int i, int j) {
	return i<r-1&&j<c-1&&mapa[i][j]=='#'&&mapa[i][j+1]=='#'&&mapa[i+1][j]=='#'&&mapa[i+1][j+1]=='#';
}

int main() {
	int d;scanf("%d",&d);
	for(int ind=1;ind<=d;ind++) {
		scanf("%d%d",&r,&c);
		for(int i=0;i<r;i++) scanf("%s",mapa[i]);
		int ok=1;
		for(int i=0;i<r;i++) for(int j=0;j<c;j++) {
			if(mapa[i][j]=='#') {
				if(!dasie(i,j)) {
					ok=0;
					i=r;
					break;
				}
				else {
					mapa[i][j]='/';
					mapa[i][j+1]='\\';
					mapa[i+1][j]='\\';
					mapa[i+1][j+1]='/';
				}
			}
		}
		
		printf("Case #%d:\n",ind);
		if(ok==0) printf("Impossible\n");
		else {
			for(int i=0;i<r;i++) printf("%s\n",mapa[i]);
		}	
	}
	return 0;
}
