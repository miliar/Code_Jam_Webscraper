#include <stdio.h>
#include <string.h>
#include <string>
#include <map>
#include <iostream>

using namespace std;

int main(){
    
    //freopen ("C-small-attempt0.in","r",stdin);
    //freopen ("salida.txt","w",stdout);
    int t,a,b;
    scanf("%d", &t);
    for(int i=0; i<t; i++){
            scanf("%d %d\n", &a,&b);
            char buffer [8];
            itoa(b,buffer,10);
            int cantidad = 0;
            for(int j=a; j<b; j++){
                    char buffer2 [8];
                    itoa(j,buffer2,10);
                    string sA(buffer2);
                    int tam = sA.length()-1;
                    for(int h=1;h<=tam;h++){
                            string resultado = sA.substr(h,tam) + sA.substr(0,h);
                            int result = atoi(resultado.c_str());
                            
                            if(result>j && result<=b){
                                        cantidad++;
                            }
                    }
            }
            printf("Case #%d: %d\n",i+1,cantidad);
    }
   // fclose(stdin);
   // fclose(stdout);
return 0;    
}
