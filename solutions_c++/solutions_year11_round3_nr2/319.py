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

const int N = 1000002;
int l,n,c;
int odl[N];
int cykl[N];

LL t;

int main() {
	int d;scanf("%d",&d);
	for(int ind=1;ind<=d;ind++) {
		scanf("%d%I64d%d%d",&l,&t,&n,&c); // t to long long
		for(int i=0;i<c;i++) {
			scanf("%d",&cykl[i]);
		}
		int akt=0;
		
		LL suma=0;
		for(int i=0;i<n;i++) {
			odl[i]=cykl[akt++]*2;
			if(akt==c) akt=0;
			suma+=odl[i];
		}
		
		
		int i = 0;
		
		while(i<n&&t>=odl[i]) {
			t-=odl[i];
			i++;
		}
		if(i<n) {
			odl[i]-=t;
			
			sort(&odl[i],&odl[n],greater<int>());
			int start = i;
			for(int ll = 0; ll<l&&start<n;ll++,start++) {
				suma-=odl[start]/2;
			}
		}
		printf("Case #%d: %I64d\n",ind,suma);
	}
	return 0;
}
