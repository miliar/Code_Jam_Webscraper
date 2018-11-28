//h4tguy
#include<cmath>
#include<cstdio>
#include<fstream>
#include<iostream>
#include<vector>
#include<list>
#include<algorithm>
#include<utility>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<string>
#include<cstdlib>
#include<bitset>
#include<cassert>

#define f(i,a,b) for(int (i)=(a);(i)<(b);(i)++)
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define inp(x) scanf("%d",&(x))

using namespace std;

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef pair<int,bool> pib;



int main()
{
    ifstream fin("C-large.in");
    ofstream fout("C.out");
    int t,n,sum,mini,x,temp;
    fin>>t;
    f(cas,1,t+1)
    {
                fout<<"Case #"<<cas<<": ";
                fin>>n;
                x=0;
                sum=0;
                mini=2000000000;
                f(i,0,n)
                {
                        fin>>temp;
                        sum+=temp;
                        x^=temp;
                        mini=min(mini,temp);
                }
                if(x!=0)
                {
                        fout<<"NO\n";
                        continue;
                }
                fout<<sum-mini<<"\n";
    }
    fin.close();
    fout.close();
    return 0;
}
