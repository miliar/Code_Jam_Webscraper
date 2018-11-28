#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <queue>
#include <map>
#include <vector>
#include <stack>
#include <stdio.h>

#define pular 80

using namespace std;

int main()
{
    int t;
    cin>>t;
    int cont = 1;
    string saida = "";
    while(t>0)
    {
        t--;
        int n;
        cin>>n;
        int o = 1;
        int b = 1;
        int total = 0;
        int anteriorb = -1;
        int anterioro = -1;
        char anterior = 'A';
        for(int i=0;i<n;i++)
        {
            char atual;
            int val;
            cin>>atual>>val;
            int esta = 0;
            if(atual=='O')
            {
                esta = o;
                o = val;
            }
            else
            {
                esta = b;
                b = val;
            }
            int somar = abs(val-esta)+1;
            if(anterior=='B' && atual=='O' && anteriorb>0)
            {
                somar-=anteriorb;
                if(somar<=0)
                    somar = 1;
            }
            if(anterior=='O' && atual=='B' && anterioro>0)
            {
                somar-=anterioro;
                if(somar<=0)
                    somar = 1;
            }
            if(atual=='B')
            {
                if(anterior=='B')
                    anteriorb += somar;
                else
                    anteriorb = somar;
            }
            else
            {
                if(anterior=='O')
                    anterioro += somar;
                else
                    anterioro = somar;
            }
            anterior = atual;
            total+=somar;
        }
        cout<<"Case #"<<cont<<": "<<total<<endl;
        cont++;
    }
    return 0;
}
