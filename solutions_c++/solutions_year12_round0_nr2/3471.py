#include <iostream>
#include <math.h>
using namespace std;


int main()
{
    size_t tests;
    cin >> tests;

    for(size_t i = 1;i<=tests; ++i){

        size_t goono, surp, inf,count=0;
        cin >> goono;
        cin >> surp;
        cin >> inf;

        for (;goono>0; --goono){
            size_t tmp, x, mod;
            cin >> tmp;
            mod = tmp%3;
            x= (mod != 0) ? (1 + (tmp / 3)) : (tmp/3);
            if (tmp==0 && inf!=0) continue;
            if (x>=inf) { ++count; }
            else if (surp>0 && (x+1)>=inf && mod!=1){
                    ++count;
                    --surp;

            }

        }
        cout << "Case #" << i << ": " << count <<endl;
    }
    return 0;
}
