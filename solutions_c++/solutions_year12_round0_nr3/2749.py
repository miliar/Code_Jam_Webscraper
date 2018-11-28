#include <cstdlib>
#include <iostream>
#include <fstream>
#include <set>

using namespace std;

int main(int argc, char *argv[])
{
    char *fname;
    int T, A, B;
    
    if(argc > 1) fname = argv[1];
    else fname = "C.in";
    
    ifstream in(fname);
    in >> T;
    
    for(int C=1;C<=T;C++)
    {
        set< pair<int,int> > s;
        in >> A >> B;
        for(int i=A;i<=B;i++)
        {
            int p=1,q=i;
            while(q/=10) p++;

            for(int j=1;j<p;j++)
            {
                int k=j, l=p-j, r=1, z=1, t;
                while(k--) r*=10;
                while(l--) z*=10;
                t = (i-r*(i/r)) * z + i/r;
                
                if(t>=A && t<=B && t>i)
                   s.insert(make_pair(i,t));
            }
        }
        
        cout << "Case #" << C << ": ";
        cout << s.size() << endl;
    }
    
    //system("PAUSE");
    return EXIT_SUCCESS;
}
