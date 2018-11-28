#include <iostream>
#include <vector>

using namespace std;



int main(int argc, const char *argv[])
{
    int T;
    cin>>T;
    int curt = 1;

    while(T--)
    {
        int N;
        cin>>N;
        int C, somme =0, cmin = 2000000 , xorall = 0;

        for (int i = 0; i < N; i++) {
            cin>>C;
            somme += C;
            cmin = (cmin > C )? C : cmin ;
            xorall ^= C;
        } // i
        cout<< "Case #"<< curt++ << ": ";
        if (xorall)
            cout<<"NO" ;
        else
            cout<< somme - cmin;

        cout<<endl;

    }

    return 0;
}

