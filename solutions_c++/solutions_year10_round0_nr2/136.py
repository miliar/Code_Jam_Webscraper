/*
 * Google Code Jam template :-)
 */

#include <iostream>
#include <string>
#include <sstream>
//#include <algorithm>
#include <vector>
//#include <ctype.h>
//#include <assert.h>
//#include <math.h>
//#include <set>
//#include <map>
#include <gmp.h>


using namespace std;

typedef unsigned idx;
typedef unsigned int num;

char bigbuf[1000];

template<class T> void line2list(string &str, vector<T> &v)
{
    istringstream ss(str,istringstream::in);
    T t;
    while (ss >> t)
    {
	v.push_back(t);
    }
}

void solve(const num c)
    /*
     * 1) Subtract the shortest event: t1, t2, ..., tk (one is 0)
     * 2) set m1 = t2, and repeat mi = gcd (m(i-1), t(i+1)), to get m(k-1)
     * 3) return m(k-1)-t1 % m(k-1);
     */
{
    num N;
    string line;
    vector<string> vs;
    mpz_t m,tm; //gcd and t_min

    cin >> N;
    getline(cin,line);
    line2list(line,vs);

    //read
    mpz_t t[N];
    for (idx i=0; i<N; ++i)
    {
	mpz_init_set_str(t[i],vs[i].c_str(),10);
    }

    //find smallest and subtract
    mpz_init_set(tm,t[0]);
    for (idx i=1; i<N; ++i)
    {
	if (mpz_cmp(tm,t[i])>0 /*tm>t[i]*/) mpz_set(tm,t[i]);
    }
    for (idx i=0; i<N; ++i)
    {
	mpz_sub(t[i],t[i],tm);
    }

    //compute gcd
    mpz_init_set(m,t[0]);
    for (idx i=1; i<N; ++i)
    {
	mpz_gcd(m,t[i],m);
    }

    mpz_sub(tm, m, tm); //tm = m - tm
    mpz_mod(tm, tm, m); //tm = tm % m

    mpz_get_str(bigbuf,10,tm);

    cout << "Case #" << c << ": " << bigbuf << endl;

    mpz_clear(m);
    mpz_clear(tm);
    for (idx i=0; i<N; ++i)
    {
	mpz_clear(t[i]);
    }
}

int main(void)
{
    num C;

    cin >> C;
    for(num t=1; t<=C; ++t) solve(t);

    return 0;
}

