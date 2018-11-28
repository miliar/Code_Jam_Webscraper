#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <sstream>
using namespace std;
const int Mmod = 1000;
const int maxPrime = 1000000;
bool isprime[maxPrime];
vector<int> primelist;
vector< pair<int, int> > fac;
int n;
void Sieve()
{
   int i, j, k;
   memset(isprime, true, sizeof(isprime));
   isprime[0] = isprime[1] = false;
   primelist.push_back(2);
   for (i = 3; i < maxPrime; i += 2)
      if (isprime[i])
      {
         primelist.push_back(i);
         if (i * i > maxPrime) break;
         for(j = i * i, k = i * 2; j < maxPrime; j += k)
            isprime[j] = false;
      }
   for (i += 2 ; i < maxPrime; i += 2)
      if (isprime[i]) primelist.push_back(i);
}
long long MPow(int a, int t){
    if (t == 0) return 1;
    if (t == 1) return a % Mmod;
    if (t % 2 == 1)
        return MPow(a, t - 1) * a % Mmod;
    long long tp = MPow(a, t / 2);
    return tp * tp % Mmod;
}
void factor(int n){
    fac.clear();
    for(int i = 0; i < primelist.size() && primelist[i] * primelist[i] <= n; ++ i)//vector<int>::iterator it = primelist.begin(); it != primelist.end(); ++ it)//int i = 0; i < primelist.size() && primelist[i] * primelist[i] <= n; ++ i)
        if (n % primelist[i] == 0){
            int d = 0;
            while (n % primelist[i] == 0){
                n /= primelist[i];
                d ++;
            }
            fac.push_back(make_pair(primelist[i], d));
        }
    if (n != 1) fac.push_back(make_pair(n, 1));
}
void dfactor(int n, int d){
    int p = 0;
    for(int i = 0; i < primelist.size() && primelist[i] * primelist[i] <= n; ++ i)//vector<int>::iterator it = primelist.begin(); it != primelist.end(); ++ it)//int i = 0; i < primelist.size() && primelist[i] * primelist[i] <= n; ++ i)
        if (n % primelist[i] == 0){
            int d = 0;
            while (n % primelist[i] == 0){
                n /= primelist[i];
                d ++;
            }
            while (p < fac.size() && primelist[i] < fac[p].first) ++ p;
            if (fac[p].first == primelist[i]) fac[p].second -= d;
        }
    if (n != 1) {
        while (p < fac.size() && n < fac[p].first) ++ p;
        if (fac[p].first == n) fac[p].second -= d;
    }
}
long long Mcmn(int n, int k){
    long double d = 1;
    for(int i = 0; i < k; ++ i)
        d = d * (n - i) / (k - i);
    long long ret = (long long)round(d) % Mmod;
    //cout << "C[" << n << "," << k << "]=" << ret << endl;
    return ret;
}
string calc(int n){
    //cout << n << endl;
    long long ret = 0;
    for(int k = 0; k <= n; k += 2){
        ret = (ret + (Mcmn(n, k) * MPow(3, n - k)) % Mmod * MPow(5, k / 2) % Mmod) % Mmod;
        //cout << ret << endl;
    }
    ret = (ret * 2 - 1) % Mmod;
    if (ret == -1) return "999";
    stringstream ss;
    if (ret < 10) ss << "00" << ret;
    else if (ret < 100) ss << "0" << ret;
    else ss << ret;
    return ss.str();
}
int main(){
    ifstream cin("C-small-attempt1.in");
    ofstream cout("out.txt");
    int T;
    //Sieve();
    cin >> T;
    for(int t = 1; t <= T; ++ t){
        cin >> n;
        //factor(n);
        //cout << "hoho" << endl;
        cout << "Case #" << t << ": " << calc(n) << endl;
    }
    return 0;
}
