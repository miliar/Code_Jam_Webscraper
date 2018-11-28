#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <ctime>
#include <string>
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cctype>

#define inputfilename "a.in"
#define outputfilename "a.out"

using namespace std;

int main ()
{
	//freopen(inputfilename , "r" , stdin);
	//freopen(outputfilename , "w" , stdout);

    int number, times;
    cin >> number;
    for (times = 0; times < number; times++)
    {
        cout <<"Case #"<<times+1<<": ";
        int n, pd, pg;
        int i;
        cin >> n >> pd >> pg;
        if (pg == 100 && pd != 100)
        {
            cout <<"Broken"<< endl;
            continue;
        }
        else if (pg == 0 && pd != 0)
        {
            cout <<"Broken"<< endl;
            continue;
        }
        int p = 100;
        for (i = 2; i <= 100; i++)
        {
            while (p % i == 0 && pd % i == 0)
            {
                p /= i;
                pd /= i;
            }
            if (pd == 1)
                break;
        }
        //cout << p << endl;
        if (p > n)
            cout <<"Broken"<< endl;
        else
            cout <<"Possible"<< endl;

    }



	return 0;
}

 
