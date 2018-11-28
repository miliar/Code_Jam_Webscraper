#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <fstream>

using namespace std;


int numPair (int a, int b)
{
    std::stringstream Num;
    std::string str;

    string A;

    int num = 0;
    string c, d;
    int k;

    Num << a;
    A = Num.str();

    int n = 0;
    int l = A.length ();
    //cout << a << ":"<<endl;

    while (n<l)
    {
        d= A;
        c = A.substr (l-1-n, n+1);

        d.erase (l-1-n, n+1);
        //cout << c << " " <<d << endl;

        d = c + d;

        //cout <<d << endl;
        //system("PAUSE");
        n++;
        //cout <<d<< endl;
        //system("PAUSE");
       if (d[0]!='0')
        {
            k = atoi(d.c_str());
            //cout << "   k= " << k << endl;

            if (k==b)
            {
                return true;
                //cout << a << " " << k << endl;
                //system("PAUSE");
                //num++;

            }
        }
    }
    //return num;

return false;
}


int main()
{
    int t,i,j;

    int a, b;
    int res = 0;
    string A, B;

    ifstream input;
    input.open ("input.txt");

    ofstream output;
    output.open ("output.txt");

    //cin >> t;

    input >> t;
    for (i = 0; i < t; i++)
    {
        //cin >> a >> b;
        input >> a >> b;

        for (j = a; j <b; j++)
        {
            for (int m = j+1; m <=b; m++){
                if (numPair(j,m))
                {
                    res++;
                }
            }
        }
        output <<"Case #"<<i+1 <<": "<< res<<endl;
        //cout << res <<endl;
        res = 0;
    }
    input.close ();
    output.close ();
    return 0;
}
