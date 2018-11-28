
#include <iostream>
#include <vector>
#include <list>
#include <map>

using namespace std;
int *a;

int c;
int n;
bool * boosters;

long long int t;


long long int contar()
{
    long long int res = 0;
    double acum = 0.0;
    for(int i = 0; i < n ;++i)
    {
        if(boosters[i] && (t ) <= res)
        {
            res += a[ i % c ] ;
        }
        else
        {
            if(boosters[i] && (t) < res + 2 * a[i%c])
            {
                double dist = double(a[i%c]);
                double recorrida = (double(t) - double(res)) / 2.0;
                dist -= recorrida;
                acum += (dist);
                res = t;
                
                //~ acum += (4.0 * (double(t<<1) - res)) + 2.0*(double(res + 2 * a[i%c]) - double(t<<1));
            }
            else
            {
                res += a[i%c] << 1;
            }
        }
    }
    return res + static_cast<long long int>(acum);
}
int main()
{
    int tn;
    cin >> tn;
    for(int i = 0 ; i <  tn; ++i)
    {
        int star1, star2;
        int l;
        cin >> l >> t >> n >> c;
        a = new int[c];
        boosters = new bool[n];
        for(int b = 0; b < n; ++b)
        {
            boosters[b] = false;
        }
        for( int ci = 0; ci <c ; ++ci)
        {
            cin >> a[ci];
        }
        long long int best = contar() ;
        star1 = -1;
        star2 = -1;
        for(int j=0; l > 0 && j < n; ++j)
        {
            boosters[j] = true;
            for(int k=j+1; l > 1 && k < n; ++k)
            {
                boosters[k] = true;
                long long int temp = contar();
                if(best > temp)
                {
                    best = temp;
                    star1 = j;
                    star2 = k;
                }
                boosters[k] = false;
            }
            if(l==1)
            {
                long long int temp = contar();
                if(best > temp)
                {
                    best = temp;
                    star1 = j;
                }
            }
            boosters[j] = false;
        }
        cout << "Case #" << i+1 << ": "<< (best) << endl; 
        delete [] a;
        delete [] boosters;
    }

    return 0;
}


