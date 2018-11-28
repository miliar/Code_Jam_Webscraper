#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef set<int> se;
typedef pair<int,int> pii;
typedef long long int tint;

#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define all(c) (c).begin(), (c).end()
#define D(a) << #a << "=" << a << " "


#define sz(a) int((a).size())
#define pb push_back



int main () {
	//freopen("A-small.in","r",stdin);
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);

    int R,k,N,g;
    int T,plata;
    int ia,ind,sum;
    vi Nums;
    bool viaje=false;

    cin>>T;

    forn(i,T)
    {
        cin>>R>>k>>N;

        forn(j,N)
        {
            cin>>g;
            Nums.pb(g);
        }

        plata=0;
        sum=0;
        ind=0;

        while(R>0)
        {
            viaje=false;
            ia=0;
            while(ia<N)
            {
                if ((sum+Nums[ind])==k)
                {
                    viaje=true;
                    R--;
                    plata+=sum+Nums[ind];
                    ind=(ind+1)%N;
                    sum=0;
                    break;
                }
                else if ((sum+Nums[ind])<k)
                {
                    sum+=Nums[ind];
                    ind=(ind+1)%N;
                }
                else // if ((sum+Nums[ind])>k)
                {
                    viaje=true;
                    R--;
                    plata+=sum;
                    sum=Nums[ind];
                    ind=(ind+1)%N;
                    break;
                }
                if ((ia==N-1) && (!viaje))
                {
                    plata+=sum;
                    sum=0;
                    R--;
                }
                ia++;
            }
        }

        cout<<"Case #"<<i+1<<": "<<plata<<endl;
        Nums.clear();
    }


  return 0;

}


