#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set> 
#include <map>
#include <iomanip>
using namespace std;

#define FOR0(i,n) for(int i=0;i<n;i++)
#define ALL(c) c.begin(),c.end()
#define TR(it,c) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define FORE(x,c) TR(__I,c)if(bool __B=1)for(typeof(*__I) x=*__I;__B;__B=0)
#define FOR1(i,n) for(int i=1;i<=n;i++)
#define IT(c) typeof(c.begin())
#define REP(n) for(int __z=0;__z<n;__z++)

typedef long long int lli;
typedef pair<int,int> ii;
typedef long double ld;

int A[1010];
int D[1010]; // d from i to i+1
int main()
{
    int T;
    cin >> T;
    
    FOR1(q,T)
    {
	int L,N,C;
	lli t;
	cin >> L >> t >> N >> C;
	FOR0(i,C) cin >> A[i];
	int j = 0;
	FOR0(i,N)
	{
	    D[i] = A[j];
	    j++;
	    if(j==C) j=0;
	}
	// FOR0(i,N)
	//     cout << D[i] << endl;

	lli best;
	lli ans = 0;
	FOR0(i,N) ans += 2*D[i];
	best = ans; // no speed boosters

	if(L>0)
	{ // buy at t, or some star reached after t, i.e. >= f
	    int f = -1;
	    bool g;
	    lli a = 0;
	    FOR0(i,N) // find first star where 
	    {
		if(a>=t)
		{
		    g = a==t;
		    f=i;
		    break;
		}
		a += 2*D[i]; // reach star i+1 in time a
	    }					
	    //cout << "f " << f <<' ' << g << endl;
	    if(f==-1) // no speed boosters for me
	    {
		L=0;
	    }
	    // compute for buying at t
	    if(L==1)
	    {
		a = 0;
		if(!g)
		{
		    FOR0(i,N)
		    {
			//cout << "Reached " << i << ' ' << a << endl;
			if(i==f-1)
			{
			    lli x = t-a;
			    lli y = D[i]-(x/2); // div works, t even
			    a += x + y;
			    continue;
			}
			a += 2*D[i];
		    }
		
		    if(a<best)
			best = a;
		}
		//cout << best << endl;

		// compute time for buying at a star
		for(int s=f;s<N;s++)
		{
		    a = 0;
		    FOR0(i,N)
		    {
			if(i==s)
			    a += D[i];
			else
			    a += 2*D[i];
		    }
		    if(a < best)
			best = a;
		}
	    }
	    else if(L==2)
	    {
		// buy one at a star, the other at t
		if(!g)
		    for(int s=f;s<N;s++)
		    {
			a = 0;
			FOR0(i,N)
			{
			    if(i==f-1)
			    {
				int x = t-a;
				int y = D[i]-(x/2);
				a += x + y;
				continue;
			    }
			    if(i==s)
				a += D[i];
			    else
				a += 2*D[i];
			}
			if(a < best)
			    best = a;
		    }

		// buy both at stars
		for(int s1=f;s1<N;s1++)
		{
		    for(int s2=s1+1;s2<N;s2++)
		    {
			a = 0;
			FOR0(i,N)
			{
			    if(i==s1 or i==s2)
				a += D[i];
			    else
				a += 2*D[i];
			}
			if (a<best)
			    best = a;
		    }
		}

	    }

	}

	cout << "Case #"<<q<<": " << best << endl;
    }
    return 0;
}
