#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int size;
    cin >> size;

    for(int set=1; set<=size; set++)
    {
        cout << "Case #" << set << ": ";
        int inputA=0, inputB=0, sol=0;
        cin >> inputA; cin >> inputB;
        int digits=log10(inputB)+1;
        bool *possible = new bool [inputB*sizeof(bool)];
        if(digits>1)
        {
            while(inputA<inputB)
            {
                int *a = new int [digits*sizeof(int)];
                for(int i=0; i<digits; i++)
                {
                    a[i] = (inputA/static_cast<int>(pow(10, digits-i-1)))%10;
                }

                for(int i=0; i<=inputB; i++)
                    possible[i] = true;
                for(int i=1; i<digits; i++)
                {
                    int  nb2=0;
                    for(int k=0; k<digits; k++)
                    {
                        nb2 += a[(i+k)%digits]*pow(10,digits-1-k);
                    }

                    if(nb2>inputA && nb2<=inputB && possible[nb2])
                    {
//                        cout << inputA << ":" << nb2 << endl;
                        possible[nb2] = false;
                        sol++;
                    }

                }

                inputA++;
            }
        }

        cout << sol << endl;
    }
//    delete a;
//    delete possible;
    return 0;
}
