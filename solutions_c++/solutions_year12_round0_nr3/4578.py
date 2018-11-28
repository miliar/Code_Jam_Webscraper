#include<iostream>
#include<cmath>
using namespace std;

int main()      {
        int T, k=1;
        int A, B, d, digit, temp, n, m, count;
        cin >> T;

        while (T>0)     {
                cin >> A >> B;
                count = 0;
                temp = A;
                digit = 0;
                while (temp >0) {
                        temp /= 10;
                        digit++;
                }

                for (n=A; n<B; n++)     {
                        temp = n;
                        for (d=1; d<digit; d++) {
                                m = n/((int)pow(10, d)) + (n%((int)pow(10, d)))*(int)pow(10,digit-d);

                                if (m<=B && n<m && m!=temp)     {
//                                      cout << n << " " << m << endl;
                                        temp = m;
                                        count++;
                                }

                        }


                }
                cout << "Case #" << k << ": " << count << endl;
                k++;
                T--;


        }




        return 0;
}
