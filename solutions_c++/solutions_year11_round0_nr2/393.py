#include <cstdio> 
#include <iostream> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <functional> 
#include <cmath> 
#include <utility> 
 
#define MP make_pair 
#define PB push_back 
 
using namespace std; 
 
#define REP(i,n) for(i=0;(i)<(int)(n);(i)++) 
typedef long long ll; 
 
#define READ_INT(a) scanf("%d", &a); 
#define READ_LL(a) scanf("%I64d", &a); 
#define READ_STRING(a) cin >> a; 


int main ()
{
	int T;
	int i, j;
	int ret;
	READ_INT(T);
	int C,D,N;
	REP(i,T){
		READ_INT(C);
		vector<string> trans(C);
		REP(j, C)READ_STRING(trans[j]);
		READ_INT(D);
		vector<string> del(D);
		REP(j, D)READ_STRING(del[j]);
		READ_INT(N);
		string query;
		READ_STRING(query);
		int delflag[28];
		memset(delflag, 0, sizeof(int)*28);
		int k;
		int flag=0;
		j=0;
		while(j != query.size()){
			if(j != 0){
				REP(k, C){
					if((query[j] == trans[k][0] && query[j-1] == trans[k][1]) || (query[j-1] == trans[k][0] && query[j] == trans[k][1])){
						query[j-1] = trans[k][2];
						query.erase(j, 1);
						memset(delflag, 0, sizeof(int)*28);
						flag = 1;
						break;
					}
				}
				if(flag){
					flag = 0;
					j=0;
					continue;
				}
			}
			REP(k, D){
				if(delflag[k] == 0){
					if(del[k][0] == query[j])delflag[k]=2;
					if(del[k][1] == query[j])delflag[k]=1;
				}else{
					if(del[k][delflag[k]-1] == query[j]){
						query.erase(0, j+1);
						j=0;
						memset(delflag, 0, sizeof(int)*28);
						flag = 1;
						break;
					}
				}
			}
			if(flag){
				flag = 0;
				continue;
			}
			j++;
		}
		if(query.size() == 0){
			printf("Case #%d: []\n", i+1);
			continue;
		}
		printf("Case #%d: [%c", i+1, query[0]);
		REP(j, query.size()-1)printf(", %c", query[j+1]);
		printf("]\n");
	}
	return 0;
}
