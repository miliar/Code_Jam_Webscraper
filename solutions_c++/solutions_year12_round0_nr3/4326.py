#include <iostream>
#include <cstdlib>
#include <string.h>
#include <stdio.h>

using namespace std;



int main()
{
    freopen("input.in", "r", stdin);
    freopen("output3.txt", "w", stdout);
    int tt; cin>>tt;
    for(int cont=0; cont<tt; cont++){
        int A,B;
        cin>>A>>B;
        int max=0;
        for(int cont2=A; cont2<=B; cont2++){
            char num[33];
            itoa(cont2,num,10);
            for(int cont3=0; cont3<strlen(num)-1; cont3++){
                if(strlen(num)>1){
                char aux=num[0];
                for(int cont5=0; cont5<strlen(num)-1; cont5++){
                    num[cont5]=num[cont5+1];
                }
                num[strlen(num)-1]=aux;
                }
                int t=atoi(num);
                if((t>cont2)&&(t<=B)){
                    max++;

                }
            }

        }
        cout<<"Case #"<<cont+1<<": "<<max<<endl;

    }
    return 0;
}
