#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <cstdio>
#include <cmath>
#include <queue>
#include <sstream>
#include <map>
#include <set>
#include <stack>
using namespace std;

typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<char> VC;
typedef vector<VI> VVI;
typedef vector<VC> VVC;
typedef vector<bool> VVB;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<long long> VL;
typedef vector<VL> VVL;
const int INF = 1000000000;

int main() {
    int casos;
    cin >> casos;
    for (int z = 1; z <= casos; ++z) {
        cout << "Case #" << z << ": ";
        long long r, cap, n;
        cin >> r >> cap >> n;
        VL v(n), lastin(n), S(n);
        for (int i = 0; i < n; ++i) cin >> v[i];
        for (int i = 0; i < n; ++i) {
            lastin[i] = i;
            long long sum = v[i];
            for (int j = 1; sum + v[(i+j)%n] <= cap and j < n; ++j) {
                sum += v[(i+j)%n];
                lastin[i]++;
            }
            S[i] = sum;
        }
        VL guany(n, -1); //Ganancia obtenida en el momento en que el primer grupo era i
        VL veces(n, -1);
        long long total = 0;
        long long first = 0;
        long long cuenta = 0;
        while (guany[first] < 0 and cuenta < r) {
            guany[first] = total;
            veces[first] = cuenta;
            total += S[first];
            first = (lastin[first] + 1)%n;
            cuenta++;
        }
        if (cuenta < r) {
            long long intervalo = total - guany[first];
            long long subidas = cuenta - veces[first];
            long long restantes = r - cuenta;
            total += intervalo*(restantes/subidas);
            cuenta += subidas*(restantes/subidas);
        }
        while (cuenta < r) {
            total += S[first];
            first = (lastin[first] + 1)%n;
            cuenta++;
        }
        cout << total << endl;
    }
}
