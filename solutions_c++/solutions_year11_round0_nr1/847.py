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

vector<int> points[2];
int pos[2];
int current[2];

vector<PI> seq;
int seqpos;

void init() {
	current[0]=current[1]=1;
	seqpos = pos[0] = pos[1] = 0;
	points[0].clear();
	points[1].clear();
	seq.clear();
}

int main() {
	int d;scanf("%d",&d);
	int ind = 1;
	while(d--) {
		init();
		scanf("%d ",&n);
		for(int i=0;i<n;i++) {
			int i;char c;scanf(" %c %d",&c,&i);
			int r = c == 'O';
			seq.PB(MP(r,i));
			points[r].PB(i);
		}
		int res = 0;
		while(seqpos < seq.size()) {
			PI cur = seq[seqpos];
			int time = 1+abs(current[cur.FT]-cur.SD);
			current[cur.FT] = cur.SD;
			pos[cur.FT]++;
			// rusz drugim
			int other = !cur.FT;
			if(pos[other] < points[other].size()) {
				int posnext = points[other][pos[other]];
				if(abs(current[other]-posnext)<=time) {
					current[other] = posnext;
				}
				else {
					current[other] += (posnext - current[other] > 0 ? 1 : -1)*time;
				}
			}
			seqpos++;
			res += time;
		}
		printf("Case #%d: ",ind++); 
		printf("%d\n",res);
	}
	return 0;
}
