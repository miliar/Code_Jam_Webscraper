#include <cstdio> 
#include <iostream> 
#include <string> 
#include <vector> 
#include <list>
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
	int T, t;
	READ_INT(T);
	REP(t,T){
		int C, D;
		READ_INT(C);
		READ_INT(D);
		vector<int> P(C);
		vector<int> V(C);
		int i,j;
		REP(i, C){
			READ_INT(P[i]);
			READ_INT(V[i]);
		}
		double up= 8.0e15;
		double down = 0.0;
		double now;
		double limit;
		int flag;
		REP(i,300){
			now = (up+down)/2.0;
			limit = -4.0e15;
			flag = 0;
			REP(j, C){
				if((V[j]-1)*D>now*2){
					down = (up+down)*0.5;
					flag = 1;
					break;
				}
				limit = ((P[j]-now > limit)?(P[j]-now):(limit)) + D*V[j];
				if(limit - D >= P[j] + now){
					down = (up+down)*0.5;
					flag=1;
					break;
				}
			}
			if(flag==0)up = (up+down)*0.5;
		}

		printf("Case #%d: %.8f\n", t+1, up);
	}
}