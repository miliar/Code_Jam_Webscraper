#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

long gcd(long a, long b) {return (b==0?a:gcd(b,a%b));}

int main() {
  long C, N;
  cin >> C;
  for (long c=1; c<=C; c++) {
    cin >> N;
    vector<long> events(N), diff;
    long maxN;
    for (long i=0; i<N; i++) cin >> events[i];
    maxN = *max_element(events.begin(), events.end());
    for (long i=0; i<N; i++) if (maxN-events[i]) diff.push_back(maxN-events[i]);
    long hcf = diff[0];
    for (long i=0; i<diff.size(); i++) hcf = gcd(hcf, diff[i]);
    long out = hcf - (maxN%hcf);
    if (!(maxN%hcf)) out=0;
    cout << "Case #" << c << ": " << out << endl;
  }
}
