#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>


using namespace std;
typedef long long LL;

#define REP(x,n) for(int x=0;x<(n);++x)
#define FOR(x,b,e) for(int x=b;x<=(e);++x)
#define FORD(x,b,e) for(int x=b;x>=(e);--x)
#define PB push_back

#define PRINT_OUT REP(nir,n){REP(nic,n)cout<<b[nir][nic];cout<<endl;}
#define PRINT_VAR(k,l,m,n) cout<<".:"<<k<<" .:"<<l<<" .:"<<m<<" .: "<<n<<endl;
#define WAIT char t;cin>>t;

int t,n;
int a1,a2,b1,b2;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("A-small-attempt3.in");
    fout.open("A-small-attempt3.out");

    fin>>t;
    REP(ti, t){
		fin>>n;
        fout<<"Case #"<<ti+1<<": ";
        if(n==2){
            fin>>a1;fin>>b1;
            fin>>a2;fin>>b2;
            if(a1>a2){
                if(b1<b2)
                    fout<<1<<endl;
                else
                    fout<<0<<endl;
            }
            else{
                if(b1>b2)
                    fout<<1<<endl;
                else
                    fout<<0<<endl;
            }
        }
        else{
            fin>>a1;fin>>b1;
            fout<<0<<endl;
        }

    }

    fin.close();
    fout.close();
    return 0;
}
