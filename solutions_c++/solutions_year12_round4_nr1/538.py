#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <list>
#include <utility>
#include <cmath>
#include <ctime>
#include <functional>
#include <numeric>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int,int> pii;
typedef pair<int64,int64> pii64;
typedef pair<double,double> pdd;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<int64> vi64;

const double pi=acos(-1.0);
const double eps=1e-11;
const int    p=1000000007;
int countbit(int n){return n==0?0:countbit(n/2)+n%2;}
int lowbit(int n){return (n^(n-1))&n;}
int64 gcd(int64 a, int64 b){return b==0?a:gcd(b, a%b);}
int64 lcm(int64 a, int64 b){return a*b/gcd(a,b);}
template<typename T> T sqr(T n){return n*n;}

int main()
{
    ifstream in("C:\\Users\\Olexandr\\Desktop\\A-large.in");
    ofstream out("C:\\Users\\Olexandr\\Desktop\\output.txt");
    int T;
    in>>T;


    for(int t=0; t<T; t++)
    {
        out<<"Case #"<<(t+1)<<": ";
        //code here:
        int N;
        in>>N;
        vector<pii> vine(N);
        for(int i=0; i<N; i++)
        {
            in>>vine[i].first>>vine[i].second; // distance, length
        }
        int D;
        in>>D;
        bool OK=false;
        vector<int> gg(N);
        gg[0]=vine[0].first;
        for(int i=0; i<N; i++)
        {
            if(gg[i])
            {
                if(D-vine[i].first<=gg[i])
                    OK=true;
                for(int j=i+1; j<N; j++)
                {
                    if(vine[j].first-vine[i].first<=gg[i])
                    {
                        gg[j]=max(gg[j], min(vine[j].first-vine[i].first,   vine[j].second));
                    }

                }
            }
        }

        out<<(OK?"YES":"NO")<<endl;
    }
    system("pause>nul");
    return 0;
}