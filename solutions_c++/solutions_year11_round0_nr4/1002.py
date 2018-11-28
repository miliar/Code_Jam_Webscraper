#include <stdio.h>
#include <stdlib.h>
#include <string> 
#include <iostream>

using namespace std;

int num[1005];
int sor[1005];

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
        int cua;
        cin >> cua;

        for (int i = 0; i < cua; i++) {
            cin >> num[i];
            sor[i] = num[i];
        }

        qsort (sor, cua, sizeof(int), compare);
        int diff = 0;

        for (int i = 0; i < cua; i++) {
            if(sor[i] != num[i])
                diff++;
        }

        cout << "Case #" << c << ": " << diff << ".000000" << endl;

        casos--; 
        c++;
    }

    return 0;
}
