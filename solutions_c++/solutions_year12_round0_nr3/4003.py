#include <iostream>
#include <fstream>

using namespace std;

int radc(int a)
{
        int an=a;
        int num=0;
        while(an>0)
        {
            num++;
            an/=10;
        }
        int ra=1;
        while(num--)
        {
            ra*=10;
        }
        ra/=10;
        return ra;
}

int main()
{
    int n,a,b;
    ifstream Vstup("input");
    Vstup >> n;
    int test=n;
    ofstream Vystup("output");
    while(n--)
    {
        Vystup << "Case #" << test-n << ": ";
        int res=0;
        Vstup >> a >> b;

        int rad = radc(a);

        //samotny vypocet
        for(int i=a; i<=b; i++)
        {
            int act = i;
            do
            {
                act = (act%10)*rad + act/10;
                if(i<act && rad == radc(act) && act <= b) res++;//cout << i << " " << act << endl;
            }while(act!=i);
        }
        Vystup << res << endl;
    }
    Vystup.close();
    return 0;
}
