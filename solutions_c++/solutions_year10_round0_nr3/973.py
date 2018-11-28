#include <stdio.h>


void do_program(int casenum)
{
    int R, k, N;
    scanf("%d %d %d", &R, &k, &N);

    int* arr = new int[N];
    for (int i=0;i<N;i++)
        scanf("%d",arr+i);

    int* load = new int[N];
    int* groups = new int[N];
    int last_sum = -1;
    int sum_index = 0;
    for (int i=0;i<N;i++) {
        int sum=0;

        // minus phase;
        if (i==0)
            sum = 0; // the first time 
        else {
            sum = last_sum - arr[i-1];
        }
        //printf("i %d sum %d index %d\n",i, sum, sum_index);

        // add phase
        int j;
        for (j=0; (j==0) || ((j+sum_index)%N)!=i; j++) {
            int idx = (j+sum_index)%N;

            if ( (sum+arr[idx]) <= k) {
                sum+=arr[idx];
                //printf("i %d sum %d index %d\n",i, sum, sum_index);
            }
            else
                break;
        }
        sum_index = (j+sum_index)%N;

        last_sum = sum;
        load[i] = sum;

        if (sum_index < i)
            groups[i] = sum_index+N-i;
        else
            groups[i] = sum_index-i;
    }
    //for (int i=0;i<N;i++)
        //printf("%d %d\n", load[i], groups[i]);

    int* before = new int[N];
    int* round = new int[N];
    for (int i=0;i<N;i++) {
        before[i] = 0;
        round[i] = -1;
    }

    int idx=0;
    int money=0;
    while (R>0) {
        if (before[idx]!=0) {
            int rounddiff = round[idx]-R;
            int repeats = R/rounddiff;
            money += (money-before[idx])*repeats;
            R=R%rounddiff;
        }
        if (R>0) {
            before[idx] = money;
            money += load[idx];
            round[idx] = R;
            idx = (idx+groups[idx])%N;
            R--;
        }else
            break;
    }
    printf("Case #%d: %d\n", casenum, money);
    delete [] before;
    delete [] round;
    delete [] arr;
    delete [] load;
    delete [] groups;
}

int main()
{
    int T;

    scanf("%d\n", &T);

    for (int i=0;i<T;i++) {
        do_program(i+1);
    }

    return 0;
}
