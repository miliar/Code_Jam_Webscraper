#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
template <class T> inline string itos(T n) {return (n)<0?"-"+itos(-(n)):(n)<10?(string)("")+(char)('0'+(n)):itos((n)/10)+itos((n)%10);}

int case_number;
#define printg case_number++, printf("Case #%d: ",case_number), printf
#define gout case_number++, printf("Case #%d: ",case_number), cout

void main2(void){

    int R, C;
    cin >> R >> C;
    int i, j;
    char inp[C+1];
    int mat[R][C];
    int count = 0;
    REP(i, R) {
        cin >> inp;
        REP(j, C) {
            if(inp[j] == '.') mat[i][j] = 0;
            else {
                mat[i][j] = 1;
                count++;
            }
        }
    }

    REP(i, R) {
        REP(j, C) {
            if(mat[i][j] == 1) {
                if(i+1 < R && mat[i+1][j] == 1) {
                    if(j+1 < C && i+1 < R && mat[i+1][j+1] == 1) {
                        if(j+1 < C && mat[i][j+1] == 1) {
                            mat[i][j] = 2;
                            mat[i][j+1] = 5;
                            mat[i+1][j+1] = 4;
                            mat[i+1][j] = 3;
                            count -= 4;
                        }
                    }
                }
            }
        }
    }

    gout << "\n";
    if(count != 0) {
        cout << "Impossible\n";
    }
    else {
        REP(i, R) {
            REP(j, C) {
                if(mat[i][j] == 0) cout << ".";
                else if(mat[i][j] == 2) cout << "/";
                else if(mat[i][j] == 3) cout << "\\";
                else if(mat[i][j] == 4) cout << "/";
                else if(mat[i][j] == 5) cout << "\\";
            }
            cout << "\n";
        }
    }
}

int main(void){
	int number_of_test_cases,i;
	cin >> number_of_test_cases;
	REP(i,number_of_test_cases) main2();
	return 0;
}
