#include <vector>
#include <string>
#include <map>
#include <cstdio>
#include <cmath>
using namespace std;

bool without[31][11];
bool with[31][11];

bool withoutCheck(int score, int want)
{
	for(int i=want;i<=10;++i){
		if(without[score][i]) return true;
	}
	return false;
}

bool withCheck(int score,int want)
{
	for(int i=want;i<=10;++i){
		if(with[score][i]) return true;
	}
	return false;
}

int main()
{
	for(int i=0;i<=10;++i){
		for(int j=0;j<=10;++j)if(abs(i-j) <= 2){
			for(int k=0;k<=10;++k)if(abs(i-k) <= 2 && abs(j-k) <= 2){
				if(abs(i-j) <= 1 && abs(i-k) <= 1 && abs(j-k) <=1){
					without[i+j+k][i] = true;
					without[i+j+k][j] = true;
					without[i+j+k][k] = true;
				}else{
					with[i+j+k][i] = true;
					with[i+j+k][j] = true;
					with[i+j+k][k] = true;
				}
			}
		}
	}

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test){
		int n,surp,p, val;
		int ansCnt = 0;
		int canCnt = 0;
		scanf("%d %d %d",&n,&surp,&p);
		for(int i=0;i<n;++i){
			scanf("%d",&val);
			if(withoutCheck(val, p))
				++ansCnt;
			else{
				if(withCheck(val,p)){
					++canCnt;
				}
			}
		}
		if(canCnt >= surp){
			ansCnt += surp;
		}else{
			ansCnt += canCnt;
		}

		printf("Case #%d: %d\n",test, ansCnt);
	}
	return 0;
}
