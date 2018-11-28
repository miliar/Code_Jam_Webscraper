#include <iostream>
#include <algorithm>
using namespace std;

int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        cout << "Case #" << i << ": ";
        int R, k, N;
        cin >> R >> k >> N;
        int *p = new int[N];
        int *pi = new int[N];
        int *pre = new int[N];
        for(int j = 0; j < N; j++)
        {
            cin >> p[j];
        }
        long long int re = 0;
        for(int j = 0; j < N; j++)
        {
            int one = 0;
            int lji = 0;
            for(int ji = j; (one + p[ji]) <= k && lji < N;)
            {
                pi[j] = ji + 1;
                one += p[ji++];
                if(ji >= N) ji = 0;
                lji++;
            }
            if(pi[j] >= N) pi[j] = 0;
            pre[j] = one;
        }
        int *h = new int[N + 1];
        int *hre = new int[N + 1];
        int j = 0;
        if(R > N){
        h[0] = 0;
        hre[0] = pre[0];
        int ji;
        j = 1;
        for(; j <= N; j++)
        {
            h[j] = pi[h[j-1]];
            hre[j] = pre[h[j]];
            ji = 0;
            for(; ji < j; ji++)
            {
                if(h[j] == h[ji]) break;
            }
            if(j != ji) break;
        }
        for(int ti = ji; ti < j; ti++)
        {
            re += hre[ti];
        }
        re *= (R - ji) / (j - ji);
        for(int ti = 0; ti < ji; ti++) re += hre[ti];
        R = (R - ji) % (j - ji);
        j = h[j];
        }
        while(R > 0)
        {
            re += pre[j];
            j = pi[j];
            R--;
        }
        delete h;
        delete hre;
        delete p;
        delete pi;
        delete pre;
        cout << re << endl;
    }
    return 0;
}
