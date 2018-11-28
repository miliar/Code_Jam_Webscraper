#include <iostream>
#include <math.h>
using namespace std;


bool recycled(const int& n1, const int& n2){
    if (n1==n2) return true;
    int tmp = n2;
    int digitsnum = 0;
    while(tmp != 0) {tmp/=10; ++digitsnum;}
    --digitsnum;
    tmp=n2;
    for (int i=0; i<=digitsnum; ++i){
        tmp=(tmp%10) * pow(10,digitsnum) + tmp/10;
        //cout << tmp << endl;
        if (n1==tmp) return true;
    }
    return false;
}


int main()
{
    size_t tests;
    cin >> tests;

    for(size_t i = 1;i<=tests; ++i){
        int n1,n2, count=0;
        cin >> n1 >> n2;
        for (int a=n1; a<=n2; ++a){
            for (int b=a+1; b<=n2; ++b)
                if (recycled(a,b))
                    ++count;
        }
        cout << "Case #" << i << ": " << count <<endl;

    }
    return 0;
}
