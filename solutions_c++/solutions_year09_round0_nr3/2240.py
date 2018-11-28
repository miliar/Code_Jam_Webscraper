#include<iostream>
#define N_MAX 500
using namespace std;

int cas;
char buffor[N_MAX + 5];
const char pattern[20] = "welcome to code jam";
long long int tab[N_MAX + 5][24];

int main() 
{
    scanf("%d", &cas);
    for(int curCase = 1; curCase <= cas; curCase++) {
        scanf("\n");
        fgets(buffor, sizeof(buffor), stdin);

        int size = 0;
        while(buffor[size] != '\0') size++;
        
        for(int i = 1; i <= size; i++) {
            tab[i][1] = tab[i-1][1];
            if(buffor[i-1] == pattern[0])
                tab[i][1]++;
        }
        
        for(int i = 2; i <= 19; i++)
            for(int j = 1; j <= size; j++)
                if(pattern[i-1] == buffor[j-1])
                    tab[j][i] = (tab[j-1][i] + tab[j-1][i-1]) % 10000;
                else
                    tab[j][i] = tab[j-1][i];
                    
        for(int i = 0; i <= 19; i++)
            for(int j = 0; j <= size; j++)
                tab[i][j] = 0;
        
        /*
        for(int i = 1; i <= 19; i++) {
            for(int j = 1; j <= size; j++)
                cout<<tab[j][i]<<" ";
            cout<<endl;
        }
        */
        
        printf("Case #%d: %.4d\n", curCase, tab[size][19]);
    }
    
    return 0;
}
