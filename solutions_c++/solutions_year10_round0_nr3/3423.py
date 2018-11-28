#include<iostream>
using namespace std;

long long sol;

int main ( )
{
int t; scanf("%d", &t); for(int it=1; it<=t; it++)
{
int r, n, k; scanf("%d%d%d", &r, &k, &n);
int a[n], indeksi[2*n], koliko[n], kamo[n];
for(int i=0; i<n; i++) indeksi[i] = indeksi[i+n] = i;
for(int i=0; i<n; i++) scanf("%d", a+i);
for(int i=0; i<n; i++) 
{
        koliko[i] = 0;
        int c = 0, j = i;
        for( ; j<n+i && c + a[indeksi[j]] <= k; j++ ) { c += a[indeksi[j]]; koliko[i] += a[indeksi[j]]; }
        kamo[i] = j%n;
}
int prvi = 0; sol = 0;
while(r--) { sol += koliko[prvi]; prvi = kamo[prvi]; }
cout << "Case #" << it << ": " << sol << endl;
}
return 0;
}
