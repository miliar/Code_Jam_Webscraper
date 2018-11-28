#include <fstream>

using namespace std;

int main(int argc, char * argv[])
{
    ifstream in;
    ofstream out;
    
    in.open("a-large.in");
    out.open("rezultat.txt");
    
    long n,k,m;
    in >> m;
    for (long i=0; i<m; i++)
    {
        in >> n >> k;
        long s=1;
        s=s << n;
        if ((k+1) % s == 0)
        out << "Case #"<< i+1 << ": ON"<< endl;
        else out << "Case #"<< i+1 << ": OFF"<< endl;
    }
    return 0;
}
