#include <stdio.h>
#include <stdlib.h>
#include <string> 
#include <iostream>
#include <queue>

using namespace std;

int num[1005];
int sum[1005];

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int main(void)
{
    int casos;
    int c = 1;
    cin >> casos;

    while(casos){
        int cuantos;
        cin >> cuantos;

        for (int i = 0; i < cuantos; i++) {
            cin >> num[i];
        }

        qsort (num, cuantos, sizeof(int), compare);

        sum[0] = num[0];
        int xoxo2 = num[0];
        for (int i = 1; i < cuantos; i++) {
            sum[i] = sum[i-1] + num[i];
            xoxo2 ^= num[i];
        }

        int i = 0;
        int iguales = 0;
        int resultado;
        int gane = 0;
        int xoxo1 = 0;
        while(sum[i] <= (sum[cuantos-1]-sum[i])){
            xoxo1 ^= num[i];
            xoxo2 ^= num[i];
            if(xoxo1 == xoxo2){
                gane=1;
                break;
            }

            if(sum[i] == (sum[cuantos-1]-sum[i]))
                iguales = 1;

            i++;
        }

        if(gane)
            cout << "Case #" << c << ": " <<  (sum[cuantos-1]-sum[i]) << endl;
        else if (iguales)
            cout << "Case #" << c << ": " <<  (sum[cuantos-1]-sum[i]) << endl;
        else
            cout << "Case #" << c << ": NO"  << endl;

        casos--; 
        c++;
    }



    return 0;
}
