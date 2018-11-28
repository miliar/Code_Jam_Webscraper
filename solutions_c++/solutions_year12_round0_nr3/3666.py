#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <stdio.h>
#include <cstdlib>
using namespace std;



vector<int> shift(int a)
{

    vector <int> v;
    stringstream s;
    string A,B,fix;
    s << a;
    s >> A;

    fix = A;

    v.push_back(a);
    int size = A.length()-1;
    while(size--)
    {

        B = A.substr(0,A.length()-1);
        B = A[A.length()-1] + B;

        stringstream s1;
        s1 << B;
        A = B;

        int x;
        s1 >> x;

        string test;
        stringstream test2;
        test2 << x;
        test2 >> test;

//if(test.length() != fix.length())
// continue;

        v.push_back(x);
    }


    return v;
}



int main()
{

    freopen("C-small-attempt0.in","r",stdin);//redirects standard input
    freopen("output.out","w",stdout);//redirects standard output
    int T;
    cin >> T;
    int start = 1;

    while(start <= T)
    {

        int a,b,count = 0;
        cin >>a >> b;

        vector<int> ord;
        vector <int> mem;
        int intial = a;
        if(a >9)
            while(a <= b)
            {
                ord = shift(a);

                bool ck = false;
                for(int i = 0 ; i < ord.size(); ++i)
                {
                   // cout << ord[i] << endl;
                    if(ord[i] != a && ord[i] <=b && ord[i] >= intial)
                    {

                        for(int j = 0 ; j < mem.size(); ++j)
                        {
                            if(ord[i] == mem[j] && a == mem[j+1])
                                ck = true;
                        }


                        if(ck == false)
                        {
                            count++;
                           // cout <<a <<endl;
                            mem.push_back(a);
                            mem.push_back(ord[i]);
                            break;
                        }
                        //  cout << endl;
                    }

                }



                a++;
            }


        cout << "Case #"<<start << ": " << count << endl;
        start++;
    }


    return 0;
}
