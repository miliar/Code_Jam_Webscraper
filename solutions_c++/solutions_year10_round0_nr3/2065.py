#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main ()
{
    long long T, R, k, N;
    cin >> T;
    long long casos = 0;
    while (T--)
    {
        casos++;
        cin >> R >> k >> N;
        vector <long long> V (N);
        long long max = 0;
        for (long long i = 0; i < N; i++)
        {
            cin >> V[i];
            max += V[i];
        }
        vector <long long> U (N, -1);
        long long index = 0, suma = 0, misuma = 0, indexparc = 0;
        while(U[index] <= 0)
        {
            U[index]++;
            suma = 0;
            indexparc = index;
            while (suma <= k && suma < max)
            {
                suma += V[index];
                index = (index+1)%N;
            }
            if (suma > k)
            {
                suma -= V[(index-1+N)%N];
            }
            index = (index-1+N)%N;
        }
        long long indexM = index;

        long long ite = 0;
        long long sumaparcial = 0;

        do
        {
            ite++;
            suma = 0;
            while (suma <= k && suma < max)
            {
                suma += V[index];
                index = (index+1)%N;
            }
            if (suma > k)
            {

                suma -= V[(index-1+N)%N];
            }
            sumaparcial += suma;
            index = (index-1+N)%N;
        }
        while (indexM != index);
        //IndexM en donde se inicia
        //sumaparcial cuanto gana
        //ite cuantas veces
        misuma = 0;

        //Hasta que sea indexM
        index = 0;
        while (indexM != index && R)
        {
            suma = 0;
            while (suma <= k && suma < max)
            {
                suma += V[index];
                index = (index+1)%N;
            }
            if (suma > k)
            {
                suma -= V[(index-1+N)%N];
            }
            index = (index-1+N)%N;
            misuma += suma;
            R--;
        }

        if (ite)
        {
            long long faltan = R/ite;
            R = R%ite;
            misuma += sumaparcial*faltan;

            while (R--)
            {
                suma = 0;
                while (suma <= k && suma < max)
                {
                    suma += V[index];
                    index = (index+1)%N;
                }
                if (suma > k)
                {
                    suma -= V[(index-1+N)%N];
                }
                index = (index-1+N)%N;
                misuma += suma;
            }
        }

        cout << "Case #" << casos << ": " << misuma << endl;
    }
    return 0;
}
