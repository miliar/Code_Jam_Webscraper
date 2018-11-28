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

const int N = 10060;
int n;
int l,h;

int f[N];

int sprawdz(int k) {
	for(int i=0;i<n;i++) {
		if(!(f[i]%k==0||k%f[i]==0)) {
			return false;
		}
	}
	return true;
}

int main() {
	int d;scanf("%d",&d);
	for(int ind=1;ind<=d;ind++) {
		scanf("%d%d%d",&n,&l,&h);
		for(int i=0;i<n;i++) {
			scanf("%d",&f[i]);
		}
		int res = -1;
		for(int i=l;i<=h;i++) {
			if(sprawdz(i)) {
				res = i;
				break;
			}
		}
		printf("Case #%d: ",ind);
		if(res == -1) printf("NO\n");
		else printf("%d\n",res);
	}
	return 0;
}
