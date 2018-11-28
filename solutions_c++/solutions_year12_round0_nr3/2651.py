#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <map>
#include <set>
#include <assert.h>
#define JAM 1
#define TAM 2000010
using namespace std;

int pot[10];
int digs[TAM];
bool vistos[TAM];
int esReciclado(int x, int y)
{
    int i=1;
    /*int l = floor(log10(x))+1;
    int k = floor(log10(y))+1;*/
    int l=digs[x];
    int k= digs[y];
    if(l!=k) return 0;
    if(x==y) return 0;
    if(l==1) return 0;
    while(i<l)
    {
        int mod = pot[i];//floor(pow(10,i));
        int div = pot[l-i];//floor(pow(10,l-i));

        if((x%mod)==(y/div))
        {
            if((x/mod)==(y%div))
                return 1;
        }
        i++;
    }
    return 0;

}

int rotar(int num, int n, int dig)
{
    int arriba;
    arriba = (num%pot[n])*pot[dig-n];
    int abajo = (num/pot[n]);
    return arriba+abajo;
}

int main()
{
    #ifdef JAM
        freopen("input.in","r",stdin);
        freopen("output.out","w",stdout);
    #endif

    int n;
    cin >>n >> ws;
    int a, b;
    for(int i=0; i<10; i++)
        pot[i] = floor(pow(10,i));

    digs[0]=0;
    for(int i=1; i<TAM; i++){
        digs[i] = floor(log10(i))+1;

    }

    for(int i=0;i<n;i++)
    {
        int answer =0;
        cin >>a >> b;
        cout << "Case #" << i+1 << ": ";
        for(int x=a;x<b;x++)
        {
            set<int> rots;
            for(int y=1;y<digs[x];y++)
            {
                int rotado = rotar(x,y,digs[x]);

                if((rotado<=b)&&(rotado>x))
                    if(digs[x]==digs[rotado])
                    {
                        if(rots.count(rotado)==0)
                        {
                            answer++;
                            rots.insert(rotado);
                        }
                    }

            }

        }
        cout << answer;
        if(i!=n-1) cout << endl;
    }

    return 0;
}
