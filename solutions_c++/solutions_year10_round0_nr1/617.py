#include<fstream>

using namespace std;

const char iname[]="A-small.in";
const char oname[]="A-small.out";

ifstream f(iname);
ofstream g(oname);

int n,i,x,y;

int main()
{
    f>>n;
    for(i=1;i<=n;++i)
    {
        f>>x>>y;
        g<<"Case #"<<i<<": "<<(((y+1)%(1<<x)==0)?"ON":"OFF")<<"\n";
    }
}
