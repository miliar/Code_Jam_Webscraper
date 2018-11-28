#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>

using namespace std;

int main() {
        int t_table[200][2];
        int f_table[200][2];
        int N, T, NA, NB;
        int m_time, as, bs, minvalue, minflag;
        char time[6];
        char blank;

        cin >> N;
        scanf("%c", &blank);
        for(int i=1 ; i <= N ; i++) {
                cin >> T;
                scanf("%c", &blank);
                cin >> NA >> NB;
                as = NA; bs = NB;
                memset(f_table, 0, sizeof(f_table));
                for(int j=0 ; j < NA+NB ; j++) {
                        scanf("%s", time);
                        m_time = (time[0]-48)*10*60 + (time[1]-48)*60 + (time[3]-48)*10 + (time[4]-48);
                        t_table[j][0] = m_time;
                        scanf("%s", time);
                        m_time = (time[0]-48)*10*60 + (time[1]-48)*60 + (time[3]-48)*10 + (time[4]-48);
                        t_table[j][1] = m_time;
                }

                for(int j=0 ; j < NA ; j++) {
                        minvalue = 1440;
                        for(int k=NA ; k < NA+NB ; k++) {
                                if(t_table[j][1]+T <= t_table[k][0] && f_table[k][0] == 0) {
                                        if(minvalue > (t_table[k][0] - t_table[j][1])) {
                                                minvalue = t_table[k][0] - t_table[j][1];
                                                minflag = k;
                                        }
                                }
                        }
                        if(minvalue < 1440) {
                                f_table[minflag][0] = 1;
                                bs--;
                        }
                }

                for(int j=NA ; j < NA+NB ; j++) {
                        minvalue = 1440;
                        for(int k=0 ; k < NA ; k++) {
                                if(t_table[j][1]+T <= t_table[k][0] && f_table[k][0] == 0) {
                                        if(minvalue > (t_table[k][0] - t_table[j][1])) {
                                                minvalue = t_table[k][0] - t_table[j][1];
                                                minflag = k;
                                        }
                                }
                        }
                        if(minvalue < 1440) {
                                f_table[minflag][0] = 1;
                                as--;
                        }
                }

                printf("Case #%d: %d %d\n", i, as, bs);
        }
}
