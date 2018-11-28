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
        char temp[1000];
        char blank;
        int N, S, Q;
        int solution;

        cin >> N;
        scanf("%c", &blank);

        for(int i=1 ; i <= N ; i++) {
                cin >> S;
                scanf("%c", &blank);
                vector <string> SS(S);
                for(int j=0 ; j < S ; j++) {
                        getline(cin, SS[j]);
                }
                cin >> Q;
                scanf("%c", &blank);
                vector <string> QQ(Q);
                for(int k=0 ; k < Q ; k++) {
                        getline(cin, QQ[k]);
                }

                vector <bool> flag(Q);
                for(int k=0 ; k < Q ; k++)
                        flag[k] = false;

                solution = 0;
                int j;
                for(int k=0 ; k < Q ; k++) {
                        for(j=0 ; j < S ; j++) {
                                if(QQ[k].compare(SS[j]) == 0) {
                                        flag[j] = true;
                                        break;
                                }
                        }
                        int l;
                        for(l=0 ; l < Q ; l++) {
                                if(flag[l] == false)
                                        break;
                        }
                        if(l == S) {
                                solution++;
                                for(int m=0 ; m < Q ; m++)
                                        flag[m] = false;
                                flag[j] = true;
                        }
                }
                printf("Case #%d: %d\n", i, solution);
        }
}
