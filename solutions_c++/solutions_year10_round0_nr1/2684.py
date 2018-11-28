#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;


unsigned long long str2long(string s)
{
    stringstream ss;
    unsigned long long lv;
    ss << s; ss >> lv;
    return lv;
}

int main(int argc, char *argv[])
{
    ifstream ifs("A-large.in", ifstream::in);
    int T, i = 1;
    ifs >> T;
    while(i <= T)
    {
        int N;
        unsigned long long K;
        ifs >> N;
        ifs >> K;
        long double p = pow(2,N);
        p -= 1;
        if(K == 0)
        {
           cout << "Case #" << i << ": OFF" << endl;
        }
        else
        {
            if(p == (long double)K)
            {
                cout << "Case #" << i << ": ON" << endl;
            }
            else
            {
                bool flag = false;
                long double tmp = p+1;
                while(p < (long double)K)
                {
                    p += tmp;
                    if(p == (long double) K)
                    {
                        cout << "Case #" << i << ": ON" << endl;
                        flag = true;
                        break;
                    }
                }
                if(!flag)
                {
                    cout << "Case #" << i << ": OFF" << endl;
                }
            }
        }
        i++;
    }
    ifs.close();
    return 0;
}
