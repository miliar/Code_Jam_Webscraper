#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
#define vsort(v) sort((v).begin(), (v).end());
#define vrsort(v) sort((v).begin(), (v).end(), greater<int>());
#define loop(n) for (int i=0;i<n;i++)
#define vforeach(i,v) for (i=0;i<(int)(v).size();i++)
#define forspan(i,s,e) for (i=s;i<e;i++)

struct Chick {
    int x;
    int v;
    int b;
};
bool operator<(Chick x, Chick y) { return x.x < y.x; }
bool operator>(Chick x, Chick y) { return x.x > y.x; }

void
solve(int num)
{
    int N, K, B, T;
    vi X, V;
    vector<Chick> chicks;
    int result;
    int slow;
    int i;

    cin >> N >> K >> B >> T;
    chicks.resize(N);
    forspan(i,0,N) { cin >> chicks[i].x; }
    forspan(i,0,N) {
        cin >> chicks[i].v;
        chicks[i].b = chicks[i].x + chicks[i].v * T;
    }
    vsort(chicks);

//    forspan(i,0,N) {
//        cout << chicks[i].x << "(" << chicks[i].v << ") ";
//    }
//    cout << endl;

    result = slow = 0;
    for (i = N - 1; i >= 0; i--) {
//cerr << "checking " << i << ": ";
        if (chicks[i].b >= B) { //ok
//cerr << chicks[i].b << " is ok" << endl;
            if (slow) result += slow;
            if (--K <= 0) break;
        } else {
            slow++;
//cerr << chicks[i].b << " is slow " << slow << endl;
        }
    }

    cout << "Case #" << num << ": ";
    if (K > 0) {
        cout << "IMPOSSIBLE";
    } else {
        cout << result;
    }
    cout << endl;
}

int
main()
{
    int N, i;

    cin >> N;
    for (i = 0; i < N; i++) {
        solve(i + 1);
    }
}

