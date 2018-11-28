#include <cstdio>
const int MAX=50;
struct snapper {
    bool energia;
    bool estado;
    void reset(){
    	energia=false;
    	estado=false;
    }
    void intercambiar(){
    if(estado==false)
    	estado=true;
    else
    	estado=false;
    }
    bool encendido(){
    	if(estado==true&&energia==true)
    		return true;
    	else
    		return false;
    }
};
snapper cadena[MAX];

int main(){
	//freopen("entrada.in","r",stdin);
    freopen("A-small-attempt3.in","r",stdin);
    freopen("A-small-attempt3.out","w",stdout);
    int T,N;
    long K;
    scanf ("%d", &T);

    for(int cas=1;cas<=T;cas++){
        scanf ("%d %ld", &N, &K);
        for(int i=0;i<N;i++){
        	cadena[i].reset();
        }
        cadena[0].energia=true;
        for(long ki=0;ki<K;ki++){
        	for(int ni=0;ni<N;ni++)
        		if(cadena[ni].energia )
        			cadena[ni].intercambiar();
            for(int ni=0;ni<N;ni++){
            	if(cadena[ni].energia&&cadena[ni].estado)
            		cadena[ni+1].energia=true;
                else
                    cadena[ni+1].energia=false;
            }
        }
        if(cadena[N-1].encendido()==true)
            printf ("Case #%d: ON\n",cas);
        else
            printf ("Case #%d: OFF\n",cas);
    }
    return 0;
}
