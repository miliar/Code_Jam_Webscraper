#include <iostream>

using namespace std;

typedef long long tint;

#define forn(i,n) for (int (i)=0; (i) < (n); (i)++)

tint next[1024], g[1024], p[1024];
tint R, N, k, tt;
tint ciclo, pciclo, tciclo, resto;
tint plata;


void check(int i)
{
    if (next[i] !=-1) ciclo = i;
    else
    {
        tint suma = 0;
        int j = 0;
        while (suma + g[(i+j)%N] <= k && j < N)
        {
            suma += g[(i+j)%N];
            j++;
        }
        next[i] = (i+j)%N;
        p[i] = suma;
        check ((i+j)%N);
    }
}

int main(){
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    cin >> tt;
    forn(t,tt)
    {
        cin >> R >> k >> N;
        forn(i,N) cin >> g[i];
        forn(i,N) next[i]= -1;
        check(0);
        plata = 0;
        int j = next[ciclo];
        tint pciclo = p[ciclo];
        tciclo=1;
        while (j != ciclo)
        {
            pciclo += p[j];
            j = next[j];
            tciclo++;
        }
        j = 0;
        resto = R;
        while (j != ciclo)
        {
            plata += p[j];
            resto--;
            j = next[j];
        }
        tint m = resto / tciclo;
        plata += m*pciclo;
        resto = resto % tciclo;
        while (resto != 0)
        {
            plata += p[j];
            j = next[j];
            resto--;
        }
        cout << "Case #" << t+1 << ": " << plata << endl;
    }
    return 0;
}
