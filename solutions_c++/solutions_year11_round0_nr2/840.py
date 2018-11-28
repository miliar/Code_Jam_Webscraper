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

string data = "QWERASDF";
vector<int> opossed[10];
vector<pair<int,char> > combine[10];

char combineIt(int a, int b) {
	for(int i=0;i<combine[a].size();i++) {
		if(combine[a][i].FT==b) {
			return combine[a][i].SD;
		}
	}
	return 0;
}

string seq;
vector<char> current;

void init() {
	for(int i=0;i<10;i++) {opossed[i].clear();combine[i].clear();}
	current.clear();
}

int getIndex(char t) {
	return data.find(t);
}
	
int main() {
	int d;scanf("%d",&d);
	int ind=1;
	while(d--) {
		scanf("%d ",&n);
		init();
		for(int i=0;i<n;i++) {
			char a,b,c;scanf(" %c%c%c",&a,&b,&c);
			int na = getIndex(a);
			int nb = getIndex(b);
			//printf("<%c %c %c> ",data[na],data[nb],data[nc]);  
			combine[na].PB(MP(nb,c));
			combine[nb].PB(MP(na,c));
		}
		scanf("%d ",&n);
		for(int i=0;i<n;i++) {
			char a,b; scanf(" %c%c",&a,&b);
			int na = getIndex(a);
			int nb = getIndex(b);
			opossed[na].PB(nb);
			opossed[nb].PB(na);
		}
		scanf("%d",&n);
		seq = scanf_string();
		for(int i=0;i<n;i++) {
			char invoked = seq[i];
			int ninvoked = getIndex(invoked);
			int combined = 0;
			if(current.size()==0) {
				current.PB(invoked);
			}
			else {
				int last = getIndex(current.back());
				if(last!=-1) {
					//printf("{%d}",last);
					char newone = combineIt(ninvoked,last);
					if(newone) {
						current.pop_back();
						current.PB(newone);
						combined=1;
					}
					else current.PB(invoked);
				}
				else {
					current.PB(invoked);
				}
			}
			if(combined==0) {
				for(int k=0;k<opossed[ninvoked].size();k++) {
					int test = opossed[ninvoked][k];
					char c = data[test];
					if(find(ALL(current),c)!=current.end()) current.clear();
				}
			}
		}
		printf("Case #%d: ",ind++); 
		printf("[");
		if(current.size()>0) printf("%c",current[0]);
		for(int i=1;i<current.size();i++) {
			printf(", %c",current[i]);
		}
		printf("]\n");
	}
	return 0;
}
