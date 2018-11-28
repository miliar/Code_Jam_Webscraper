#include <iostream>
using namespace std;

// Shield your eyes!

int check(int n, int m)
{
    char cn[8];
    char cm[8];
    int mag = 1;
    for(int i=0; i<8; i++)
    {
        cn[7-i]=(n/mag)%10;
        mag *= 10;
    }
    mag = 1;
    for(int i=0; i<8; i++)
    {
        cm[7-i]=(m/mag)%10;
        mag *= 10;
    }

    int digits;
    for(digits=0; digits<8; digits++)
    {
        if(cn[digits] != 0) break;
    }
    digits = 8-digits;
    for(int i=0; i<digits; i++)
        cn[i] = cn[8-digits+i];
    for(int i=0; i<digits; i++)
        cm[i] = cm[8-digits+i];

    bool fail = false;
    for(int i=0; i<digits; i++)
    {
        fail=false;
        for(int j=0; j<digits; j++)
        {
            if(cn[j] != cm[(i+j)%digits]) { fail = true; break; }
        }
        if(!fail) return 1;
    }

    return 0;
}

int main(int argc, const char *argv[])
{
    int T;
    cin >> T;

    for(int ca=0; ca<T; ca++)
    {
        long c = 0;
        int A,B;
        cin >> A >> B;

        // how many distinct recycled pairs (n, m)
        // are there with A ≤ n < m ≤ B?

        for(int n=A; n<B; n++)
            for(int m=n+1; m<=B; m++)
                c += check(n,m);

        cout << "Case #"<<(ca+1)<<": "<<c<<"\n";
    }

    return 0;
}
