#include <stdio.h>
#include <math.h>
#include <list>

using namespace std;


int pot(int a, int b){
        int w=a;
        while(b>1){
                w*=a;
                b--;
        }
        return w;
}

int main(){
        int T = 1;
        int num1, num2;
        int temp1, temp2, temp3;
        long long licz = 0;
        list<int> lista;
        scanf("%d", &T);
        for ( int i = 0; i < T; i++){
		licz = 0;
                scanf("%d", &num1);
                scanf("%d", &num2);
                int l1, l2;
                l2 = log10(num2);
                for ( int j = num1; j <= num2; j++ ){
                	for ( int k = 1; k < log10(j); k++){
                		temp3 = j % pot(10,k);
                		temp2 = j / pot(10,k);
                		temp1 = temp3 * pot(10,l2-k+1) + temp2;
                		if ( temp1 > j && temp1 <= num2)lista.push_back(temp1);
                	}
                	lista.unique();
                	licz+=lista.size();
                	lista.clear();

                }
                printf("Case #%d: %lld\n", i+1, licz);
        }

        return 0;

}

