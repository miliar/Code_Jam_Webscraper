#include<iostream>
#include<algorithm>
#include<cassert>
#include<utility>
#include<limits>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<sstream>
#include<cmath>
#include<ctime>
#include<vector>
#include<bitset>
#include<string>
#include<map>
#include<set>
#include<iomanip>
#include<queue>
#include<stack>
#include<numeric>
using namespace std;
typedef long long ll;
#define EPS (1e-8)
#define ALL(x) (x).begin(),(x).end()
#define AS assert
#define clr clear
#define PB push_back
#define SZ(x) ((int)(x).size())
#define MP make_pair
#define X first
#define Y second
#define PII pair<int,int>
#define VI vector<int>
#define VD vector<double>
#define VS vector<string>
#define FORD(i,b,c) for(int (i)=(b);(i)>=c;(i)--)
#define REPD(i,c) FORD(i,c,0)
#define FOR(i,b,c) for(int (i)=(b);(i)<(c);(i)++)
#define REP(i,c) FOR(i,0,c)
#define PQ priority_queue
#define LL(x) ((x)<<1)
#define RR(x) ((x)<<1|1)
#define READ freopen("data.in","r",stdin)
#define see(x) (cerr<<"[Line:"<<__LINE__<<"]: "<<#x<<"="<<x<<'\n')
#ifndef INT_MAX
#define INT_MAX (numeric_limits<int>::max())
#define INT_MIN (numeric_limits<int>::min())
#endif
#define ll_max (numeric_limits<long long>::max())
#define ll_min (numeric_limits<long long>::min())
#define CB __builtin_popcount
//prime 999983 100003 899981 900001 900007
const int dm[8][2]={{0,1},{-1,1},{-1,0},{-1,-1},{0,-1},{1,-1},{1,0},{1,1}};
//const int dm[8][2]={{2,-1},{2,1},{1,2},{-1,2},{-2,1},{-2,-1},{-1,-2},{1,-2}};
//const int dm[4][2]={{0,1},{1,0},{-1,0},{0,-1}};
template<class itype,class otype>void convert(otype&out,const itype&in){istringstream str(in);str>>out;}//slow
struct Combine{
	char a,b;
	char c;
	Combine(){}
	Combine(char a,char b,char c):a(a),b(b),c(c){}
};
struct Opposed{
	char a,b;
	Opposed(){}
	Opposed(char a,char b):a(a),b(b){}
};
void show(vector<char>str){
	for(int i=0;i<str.size();i++){
		printf("%c%c%c",i?' ':'[',str[i],i==str.size()-1?']':',');
	}
	if(str.size()==0){
		printf("[]");
	}
	puts("");
}
int main(){
	int T,cas=0;
	scanf("%d",&T);
	while(T--){
		cas++;
		int C,D,N;
		scanf("%d",&C);
		vector<Combine>arrc;
		vector<Opposed>arro;
		char a,b,c;
		for(int i=0;i<C;i++){
			scanf(" %c %c %c",&a,&b,&c);
			arrc.push_back(Combine(a,b,c));
		}
		scanf("%d",&D);
		for(int i=0;i<D;i++){
			scanf(" %c %c",&a,&b);
			arro.push_back(Opposed(a,b));
		}
		scanf("%d",&N);
		vector<char>str;
		for(int i=0;i<N;i++){
			scanf(" %c",&a);
			str.push_back(a);
			bool succ=true;
			while(succ){
				succ=false;
				if(str.size()<=1)continue;
				int len=str.size();
				for(int j=0;j<C;j++){
					if((str[len-1]==arrc[j].a&&str[len-2]==arrc[j].b)||(str[len-1]==arrc[j].b&&str[len-2]==arrc[j].a)){
						str.erase(str.begin()+len-2,str.end());
						str.push_back(arrc[j].c);
						succ=true;
						break;
					}
				}
				if(succ)continue;
				for(int j=0;j<D;j++){
					if(str[len-1]==arro[j].a){
						for(int k=0;k<len;k++){
							if(str[k]==arro[j].b){
								str.clear();
								succ=true;
								break;
							}
						}
						if(succ)break;
					}
					if(str[len-1]==arro[j].b){
						for(int k=0;k<len;k++){
							if(str[k]==arro[j].a){
								str.clear();
								succ=true;
								break;
							}
						}
						if(succ)break;
					}
				}
			}
		}
		printf("Case #%d: ",cas);
		show(str);
	}
}
