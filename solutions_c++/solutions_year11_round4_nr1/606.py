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

const int N = 1010;
int n,l,s,t,r;

PI pos[N];
int dl[N];
int speed[N];

PI sd[N];

int main() {
	int d;scanf("%d",&d);
	for(int ind=1;ind<=d;ind++) {
		scanf("%d%d%d%d%d",&l,&s,&r,&t,&n);
		int suma=0;
		for(int i=0;i<n;i++) {
			int a,b;scanf("%d%d%d",&a,&b,&speed[i]);
			pos[i]=MP(a,b);
			dl[i]=b-a;
			sd[i]=MP(speed[i],dl[i]);
			suma+=dl[i];
		}
		sd[n]=MP(0,l-suma);
		sort(sd,sd+n+1);
		//sort(sd,sd+n+1,greater<PI>());
		double time=0;
		double tmpt=t;
		//for(int i=0;i<=n;i++) printf("%d %d ,",sd[i].FT,sd[i].SD);
		for(int i=0;i<=n;i++) {
			if(tmpt>0) {
				double runtime=(double)sd[i].SD/(sd[i].FT+r);
				if(tmpt>runtime) {
					tmpt-=runtime;
					time+=runtime;
				}
				else {
					double lenrun=tmpt*(sd[i].FT+r);
					double newlen=sd[i].SD-lenrun;
					
					double walktime=(double)newlen/(sd[i].FT+s);
					time+=tmpt+walktime;
					tmpt=0;
				}
			}
			else {
				double walktime=(double)sd[i].SD/(sd[i].FT+s);
				time+=walktime;
			}
		}
		printf("Case #%d: %lf\n",ind,time);
	}
	return 0;
}
