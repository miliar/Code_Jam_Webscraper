#include <fstream>
#include <string>
#include <math.h>

using namespace std;

int main() 
{

        int t;
        long long int n, k;
        string ans;

        ifstream fin("A-large.in");
        ofstream fout("A-large.out");

        fin>> t;

        for(int i=0; i<t; i++) {
                fin>> n>> k;
                if (k % (long long int)pow(2,n) == pow(2,n)-1) ans = "ON";
                else ans = "OFF";
                fout<< "Case #"<<i+1<<": "<<ans<<endl;
        }

        fin.close();
        fout.close();

        return 0;

}
