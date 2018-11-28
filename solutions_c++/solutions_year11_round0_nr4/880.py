#include <stdio.h>
#include <assert.h>

int T;              // no of test cases
int N;              // no of elements in array
int arr[2000];      // the array to sort
int hits;           // expected no of hits needed to sort the array

// Goro has enough fingers to hold all the elements that are sorted
// for k un-sorted elements, expected no of hits = k
void goroSort()
{
    hits=0;
    for(int i=1; i<=N;i++)
    {
        if(arr[i] !=i)   // not already at it's place
        {
            hits ++; 
        }
    }
}

int main()
{
    FILE *fp = fopen("c:\\inp.txt", "r+"); // get input data from file
    fscanf(fp, "%d", &T);

    FILE *fpo = fopen("c:\\op.txt", "w+"); // write op data to file

    for(int c=1;c<=T;c++)    // process each test case
    {
        fscanf(fp, "%d", &N);
        for(int i=1;i<=N;i++)
            fscanf(fp, "%d", &arr[i]);

        goroSort();
        fprintf(fpo, "Case #%d: %d\n", c, hits);
    }

    fclose(fp);
    fclose(fpo);
    return 0;
}

