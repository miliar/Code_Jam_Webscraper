#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

typedef unsigned long long ulong;

int main() {
    ifstream input("C-large.in");
    ofstream output("C-large.out");
    ulong t;
    input>>t;
    for (ulong i = 0; i < t; i++) {
        ulong money = 0;
        ulong r, k, n;
        input>>r>>k>>n;
        ulong camefrom[n];
        ulong goneto[n];
        ulong queue[n];
        ulong sum[n];
        for (ulong j = 0; j < n; j++){
            input>>queue[j];
            camefrom[j] = 10000;
            goneto[j] = 10000;
            sum[j] = 0;
        }
        ulong runs = 0;
        ulong laststart = 10001;
        ulong currentstart = 0;
        while (runs < r) {
            if (camefrom[currentstart] == laststart) {
                ulong tracesum = sum[currentstart];
                ulong traceback = laststart;
                ulong traceruns = 1;
                while (traceback != currentstart) {
                    tracesum += sum[traceback];
                    traceback = camefrom[traceback];
                    traceruns++;
                }
                money += ((r - runs) / traceruns) * tracesum;
                runs += ((r - runs) / traceruns) * traceruns;
                while (runs < r) {
                    money += sum[currentstart];
                    runs++;
                    currentstart = goneto[currentstart];
                }
            } else {
                camefrom[currentstart] = laststart;
                ulong gang = queue[currentstart];
                ulong currentit = (currentstart + 1) % n;
                while (gang <= k) {
                    if (currentit == currentstart) break;
                    if (gang + queue[currentit] > k) break;
                    gang += queue[currentit];
                    currentit = (currentit + 1) % n;
                }
                sum[currentstart] = gang;
                laststart = currentstart;
                goneto[currentstart] = currentit;
                currentstart = currentit;
                money += gang;
                runs++;
            }
        }
        output<<"Case #"<<i + 1<<": "<<money<<endl;
    }
}
