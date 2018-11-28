#include<fstream>
#include<cmath>
using namespace std;

int main()
{
    ifstream fin("B.in");
    ofstream fout("B.out");
    
    int t,l,p,c,tri;
    fin>>t;
    
    for(int i=1;i<=t;i++)
    {
        fin>>l>>p>>c;
        tri=(int)ceil((float)p/(float)l);
        tri=(int)ceil((log(tri)/log(c)));
        tri=(int)ceil((log(tri)/log(2)));
        fout<<"Case #"<<i<<": "<<tri<<endl;
    }
}
