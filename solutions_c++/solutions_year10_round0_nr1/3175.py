#include <stdio.h>
#include <stdlib.h>
#include <memory.h>



void Toggles(int &data) {

    if ( data == 0 ) data = 1;
    else data = 0;


}

int pow(int n) {

    int data = 1;

    for ( int i = 0 ; i < n ; i++ )
        data *= 2;

    return data;

}


int Snapper(int n, int k) {

    int *s = new int[n];
    int j = 0;
    int cnt = 0;
    int rev = 1;

    memset(s, 0, sizeof(int) * n);
    int power = pow(n);
    
    if ( k > power ) k = k % power;

    while ( j < k ) {
        
        if ( s[0] == 0 ) {
            s[0] = 1;
        }
        else {
            for ( int i = 0 ; i < n ; i++ ) {
                if ( s[i] == 0 ) {
                    s[i] = 1;
                    break;
                }
                else {
                    s[i] = 0;
                }
            }
        }

                
        // 소켓 출력
        //for ( int i = 0 ; i < n ; i++ ) 
        //    printf("%d ", s[i]);     

        //printf("\n");
        j++;

        cnt++;
        if ( cnt == n ) cnt = 0;

    }

    for ( int i = 0 ; i < n ; i++ ) {
        if ( s[i] == 0 ) {
            return 0;
        }
    }

    delete []s;

    return 1;
}



int main(int argc, char **argv) {

    //printf("\nLIGHT : %d", Snapper(4, 47));

    FILE *fp = fopen("large.txt", "r");
    FILE *fp2 = fopen("result.txt", "w");
    
    int t;
    int n, k;
    fscanf(fp, "%d", &t);

//    printf("%d\n", t);

    for ( int i = 0 ; i < t ; i++ ) {
        fscanf(fp, "%d %d", &n, &k);
//        printf("%d %d\n", n, k);
        if ( Snapper(n, k) == 0 ) {
            // OFF
            fprintf(fp2, "Case #%d: OFF\n", i+1);
            printf("Case #%d: OFF\n", i+1);
        }
        else {
            // ON
            fprintf(fp2, "Case #%d: ON\n", i+1);
            printf("Case #%d: ON\n", i+1);
        }

    }
    


    fclose(fp);
    fclose(fp2);

    return 0;
}