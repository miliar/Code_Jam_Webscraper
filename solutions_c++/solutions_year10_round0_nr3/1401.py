#include <iostream>
#include <fstream>
#include <list>
using namespace std;

int main()
{
    ifstream cin("C-large.in");
    //ifstream cin("in.txt");
    ofstream cout("OutB.txt");
    int n;
    cin >> n;
    for (int m = 0; m < n; m++) {
        long long R,k,N;
        cin >> R >> k >> N;
        //list<long long> li;
        long long li[2000];
        for (int i = 0; i < N; i++) {
            cin >> li[i];
        }
        long long result_money[2000] = {0};
        int result_st[2000] = {0};
        for (int h = 0; h < N; h++) {
            long long sum = 0;
            int st = h;
            bool done = false;
            for (int b = 0; b < N; b++) {
                if (sum + li[(h+b)%N] <= k) {
                    sum += li[(h+b)%N];
                    st = (st+1)%N;
                } else {
                    result_money[h] = sum;
                    result_st[h] = st;
                    done = true;
                    break;
                }
            }
            if (!done) {
                result_money[h] = sum;
                result_st[h] = st;
            }
        }
        long long money = 0;
        int st = 0;
        for (long long i = 0; i < R; i++) {
            /*bool done = false;
            long long total = 0;
            int it = 0;
            while (!done && it < N) {
                long long f = li[st];
                if (total + f <= k) {
                    it++;
                    st = (st+1)%N;
                    total += f;
                } else {
                    done = true;
                }
            }*/
            money += result_money[st];
            st = result_st[st];
        }
        cout << "Case #" << m+1 << ": " << money << endl;
    }
}