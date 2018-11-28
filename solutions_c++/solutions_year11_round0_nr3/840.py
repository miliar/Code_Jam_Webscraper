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
int n;

int main() {
	int d;scanf("%d",&d);
	for(int ind = 1;ind<=d;ind++) {
		int res = 0;
		scanf("%d",&n);
		int minimum = INF;
		int sum = 0;
		for(int i=0;i<n;i++) {
			int tmp; scanf("%d",&tmp);
			res^=tmp;
			minimum = min(minimum,tmp);
			sum += tmp;
		}
		printf("Case #%d: ",ind);
		if(res==0) {
			printf("%d\n",sum - minimum);
		}
		else printf("NO\n");
	}
	return 0;
}
