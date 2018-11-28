#include <fstream>

using namespace std;

ifstream fin("C-small-attempt0.in");
ofstream fout("C-small-attempt0.out");

int gcd(int a,int b)
{
    if(a%b==0) return b;
    else return gcd(b,a%b);
}

int t,ti,n,l,r,i,j;
int a[102];
bool bo;

int main()
{
    fin>>t;
    for(ti=1;ti<=t;ti++)
    {
        fin>>n>>l>>r;
        for(i=1;i<=n;i++) fin>>a[i];
        fout<<"Case #"<<ti<<": ";
        for(i=l;i<=r;i++)
        {
            bo=true;
            for(j=1;j<=n;j++)
            {
                //fout<<i<<a[j]<<endl;
                if(i>a[j]) { if(i%a[j]!=0) {bo=false; break;}}
                if(i<a[j]) { if(a[j]%i!=0) {bo=false; break;}}
            }
            if(bo) { fout<<i<<endl; break; }
        }
        if(!bo) fout<<"NO"<<endl;
    }
    return 0;
}
