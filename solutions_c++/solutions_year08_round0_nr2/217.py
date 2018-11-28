#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

class Time{
        public:
                Time(){}
                Time(int a, int b, int c, int d, char f){
                        sh = a;
                        sm = b;
                        eh = c;
                        em = d;
                        st = sh * 60 + sm;
                        et = eh * 60 + em;
                        from = f;
                }
                char from;
                int sh, sm, eh, em;
                int st, et;
                bool operator<( Time a ) const {
                        return st < a.st;
                }
};

Time timeTable[1000];
int AN, BN, N, time;

int FREEA[24*60], FREEB[24*60];

int main()
{
        int a, b, c, d;
        int caseN;
        int COUNTA, COUNTB;
        scanf("%d",&caseN);
        for(int x=0;x<caseN;x++){
                scanf("%d",&time);
                scanf("%d%d",&AN, &BN);
                N = AN + BN;
                for(int i=0;i<AN;i++){
                        scanf("%d:%d %d:%d\n", &a, &b, &c, &d);
                        timeTable[i] = Time( a, b, c, d, 'a');
                }
                for(int i=0;i<BN;i++){
                        scanf("%d:%d %d:%d\n", &a, &b, &c, &d);
                        timeTable[i+AN] = Time( a, b, c, d, 'b');
                }
                memset(FREEA, 0, sizeof(FREEA));
                memset(FREEB, 0, sizeof(FREEB));
                COUNTA = COUNTB = 0;

                sort( timeTable, timeTable + N );

                for(int i = 0, j=0;i<24*60 && j < N;i++){
                        while(j < N && timeTable[j].st == i){
                                if(timeTable[j].from == 'a'){
                                        if(FREEA[i] > 0)
                                                FREEA[i]--;
                                        else
                                                COUNTA++;
                                        FREEB[ timeTable[j].et + time ]++;
                                }else{
                                        if(FREEB[i] > 0)
                                                FREEB[i]--;
                                        else
                                                COUNTB++;
                                        FREEA[ timeTable[j].et + time ]++;
                                }
                                j++;
                        }
                        FREEA[i+1] += FREEA[i];
                        FREEB[i+1] += FREEB[i];
                }
                printf("Case #%d: %d %d\n", x+1, COUNTA, COUNTB);
        }
}

