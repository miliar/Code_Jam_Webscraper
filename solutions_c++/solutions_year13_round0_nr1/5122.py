#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <cstdio>
#include <set>
#include <map>
#include <cstdlib>
#include <cstring>
#include <stack>
#include <cassert>
#include <limits.h>
#include <unistd.h>
#include <stdint.h>

typedef unsigned long long ULL;
typedef long long LL;

#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define ABS(a) ((a>0)?a:-a)

#define SZ(a) ((int)a.size())
#define PB(a) push_back(a)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define REP(i,n) FOR(i,0,(int)(n-1))
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define printv(v) REP(i,SZ(v))printf("%d ",v[i]);
#define mp(a,b) make_pair(a,b)
#define PII pair<int,int>

#define Sd(t)   scanf("%d",&t)
#define Slld(t) scanf("%lld",&t)
#define Ss(t)   scanf("%s",t)
#define Slf(t)  scanf("%lf",&t)

#define Pd(t)   printf("%d",t)
#define Plld(t) printf("%lld",t)
#define Ps(t)   printf("%s",t)
#define Plf(t)  printf("%lf",t)

#define Pc(t)   printf("%c",t)
#define Pn	Pc('\n')
#define MOD 1000000007
#define MX 10000

class FastInput {
	public:
		FastInput() {
			m_dataOffset = 0;
			m_dataSize = 0;
			m_v = 0x80000000;
		}
		uint32_t ReadNext() {
			if (m_dataOffset == m_dataSize) {
				int r = read(0, m_buffer, sizeof(m_buffer));
				if (r <= 0) return m_v;
				m_dataOffset = 0;
				m_dataSize = 0;
				int i = 0;
				if (m_buffer[0] < '0') {
					if (m_v != 0x80000000) {
						m_data[m_dataSize++] = m_v;
						m_v = 0x80000000;
					}
					for (; (i < r) && (m_buffer[i] < '0'); ++i);
				}
				for (; i < r;) {
					if (m_buffer[i] >= '0') {
						m_v = m_v * 10 + m_buffer[i] - 48;
						++i;
					} else {
						m_data[m_dataSize++] = m_v;
						m_v = 0x80000000;
						for (i = i + 1; (i < r) && (m_buffer[i] < '0'); ++i);
					}
				}
			}
			return m_data[m_dataOffset++];
		}
	public:
		uint8_t m_buffer[32768];
		uint32_t m_data[16384];
		size_t m_dataOffset, m_dataSize;
		uint32_t m_v;
};

using namespace std;
int main(){
    freopen("./A-large.in","r",stdin);
    freopen("./A_large_out.txt","w",stdout);
    int T,cnt=0;
    char grid[5][5],checkX[5][5],checkO[5][5];
    Sd(T);
    getchar();
    REP(cs,T){
        cnt = 0;
        REP(i,4){
            REP(j,4){
                grid[i][j] = getchar();
                checkX[i][j] = checkO[i][j] = grid[i][j];
                if(grid[i][j] == 'T'){
                    checkX[i][j] = 'X';
                    checkO[i][j] = 'O';
                }
                if(grid[i][j] == '.')
                    cnt++;
            }
            getchar();
        }
        getchar();
        int flag = 0;
        /*REP(i,4){
            REP(j,4){
                putchar(grid[i][j]);
            }
            Pn;
        }
        Pn;
        REP(i,4){
            REP(j,4){
                putchar(checkX[i][j]);
            }
            Pn;
        }
        Pn;
        REP(i,4){
            REP(j,4){
                putchar(checkO[i][j]);
            }
            Pn;
        } */
        REP(i,4){

            if(checkX[0][i] == 'X' && checkX[1][i] == 'X' && checkX[2][i] == 'X' && checkX[3][i] == 'X')
                flag = 2;
            if( checkX[i][0] == 'X' && checkX[i][1] == 'X' && checkX[i][2] == 'X' && checkX[i][3] == 'X')
                flag = 2;
            if( checkO[i][0] =='O' && checkO[i][1] =='O' && checkO[i][2] =='O' && checkO[i][3] == 'O')
                flag = 1;
            if(checkO[0][i] == 'O' && checkO[1][i] == 'O' && checkO[2][i] == 'O' && checkO[3][i] == 'O')
                flag = 1;
        }
        if(checkX[0][0] == 'X' && checkX[1][1] == 'X' && checkX[2][2] == 'X' && checkX[3][3] == 'X')
            flag = 2;
        if(checkX[0][3] == 'X' && checkX[1][2] == 'X' && checkX[2][1] == 'X' && checkX[3][0] == 'X')
            flag = 2;
        if(checkO[0][0] == 'O' && checkO[1][1] == 'O' && checkO[2][2] == 'O' && checkO[3][3] == 'O')
            flag = 1;
        if(checkO[0][3] == 'O' && checkO[1][2] == 'O' && checkO[2][1] == 'O' && checkO[3][0] == 'O')
            flag = 1;
        if(flag == 1){
            printf("Case #%d: O won\n",cs+1);
        }
        else if(flag == 2){
            printf("Case #%d: X won\n",cs+1);
        }
        else{
            if(cnt>0)
                printf("Case #%d: Game has not completed\n",cs+1);
            else
            printf("Case #%d: Draw\n",cs+1);
        }
    }
	return 0;
}
