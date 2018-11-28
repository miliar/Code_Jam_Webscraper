#include <stdio.h>
#include <stdlib.h>
#include <memory.h>


int *group;


int CalcCost(int r, int k, int n) {

    int cost = 0;
    int start = 0 , end = 0;
    int passenger;

    for ( int i = 0 ; i < r ; i++ ) {

        passenger = 0;

//        printf("{ ");
        while ( 1 ) {
            // 최대 탑승객을 넘지 말라
            if ( passenger + group[start] > k ) {
                end = start;
                break;
            }
            
//            printf("%d ", group[start]);
            passenger += group[start];

            start = (start + 1) % n;

            if ( start == end ) {
                break;
            }

        }

//        printf(" } \n");

        cost += passenger;

    }    

    return cost;
}

int main() {

    FILE *fp = fopen("small.txt", "r");
    FILE *fp2 = fopen("result.txt", "w");

    int data;
    int r, k, n;

    fscanf(fp, "%d", &data);
  //  printf("%d\n", data);

    for (int i = 0 ; i < data ; i++ ) {
        fscanf(fp, "%d %d %d", &r, &k, &n);
    //    printf("%d %d %d\n", r, k, n);

        group = new int[n];

        for ( int j = 0 ; j < n ; j++ ) {
            fscanf(fp, "%d ", &group[j]);
      //      printf("%d ", group[j]);
        }

        //printf("\n비용 : %d\n", CalcCost(r, k, n));

        fprintf(fp2, "Case #%d: %d\n", i+1, CalcCost(r, k, n));
        //printf("\n");
        
        delete []group;
    }



    fclose(fp);
    fclose(fp2);


    return 0;
}