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
	char buf[1024];
	
	REP(i,T){
		ret = 0;
		int N, tmp;
		vector<pair<char ,int>> seq;
		READ_INT(N);
		int turn=0, B=1, O=1;
		int flag;
		REP(j, N){
			READ_STRING(buf);
			READ_INT(tmp);
			if(j == 0)flag = buf[0];
			if(buf[0] == flag){
				if(buf[0] == 'B'){
					turn += (tmp - B > 0)?(tmp-B+1):(B-tmp+1);
					B=tmp;
				}else{
					turn += (tmp - O > 0)?(tmp-O+1):(O-tmp+1);
					O=tmp;
				}
			}else{
				ret += turn;
				flag = buf[0];
				int turn2;
				if(buf[0] == 'B'){
					turn2 = (tmp - B > 0)?(tmp-B):(B-tmp);
					if(turn2 < turn){
						turn = 1;
						B = tmp;
					}else{
						turn = turn2 - turn + 1;
						B=tmp;
					}
				}else{
					turn2 = (tmp - O > 0)?(tmp-O):(O-tmp);
					if(turn2 < turn){
						turn = 1;
						O = tmp;
					}else{
						turn = turn2 - turn + 1;
						O=tmp;
					}
				}

			}
		}
		ret += turn;
		printf ("Case #%d: ", i+1);
		printf ("%d\n", ret);
	}
	return 0;
}
