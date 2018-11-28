#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <gmp.h>

using namespace std;

int main(){
	freopen("C-large.in","rt", stdin);
	freopen("C-large.out","wt",stdout);
	int T, N;
	cin>>T;
    unsigned long int num;
    unsigned long int smallest;
    unsigned long int remainder;
    int index;
    mpz_t count;
    mpz_init(count);
    
	for(int t = 0; t<T; t++){
		printf("Case #%d: ", t+1);
		cin>>N;
        int bitcounts[32] = {0};
        mpz_set_ui(count, 0);
        for (int n = 0; n<N; n++) {
            cin>>num;
            if(n==0) {
                smallest = num;
            }
            mpz_add_ui(count, count, num);
            if(num < smallest) {
                smallest = num;
            }
            index = 0;
            while (num > 0) {
                if(n==0) {
                    bitcounts[index] = 0;
                }
                remainder = num%2;
                num = num/2;
                bitcounts[index] += remainder;
                index++;
            }
        }
        bool possible = true;
        for (int i = 0; i<32; i++) {
            remainder = bitcounts[i]%2;
            if(remainder > 0 ) {
                possible = false;
                break;
            }
        }
        if(possible) {
            mpz_sub_ui(count, count, smallest);
            gmp_printf("%Zd", count);
        }else{
            cout<<"NO";
        }

		cout<<"\n";
	}
	return 0;
}