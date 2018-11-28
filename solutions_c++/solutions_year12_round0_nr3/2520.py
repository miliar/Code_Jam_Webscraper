#include <stdlib.h>
#include <stdio.h>
#include <string.h>

//Rotates the digits of a base-10 integer left
int rotateInt(int n)
{
    char intstr1[10]; //Holds int as string
    char intstr2[10];
    int rot; //Number of rotations
    int len;

    itoa(n, intstr1, 10);
    strcpy(intstr2, intstr1);

    len = strlen(intstr1);

    //Get proper number of rotations. Avoid leading zero.
    rot = 0;
    while(intstr1[++rot] == '0')
        ;

    memmove(intstr1, intstr1+rot, len-rot); //Shift the all but the first digit left
    memmove(intstr1+(len-rot), intstr2, rot);
    
    return atoi(intstr1);
}

int howMany(int x)
{
    return 1;
}

int main(int argc, char * argv[])
{
    int tests; //Number of lines
    int i, j; //iterators
    FILE *f_in, *f_out;

    int A, B;
    int n, m;
    int count;

    f_in = fopen("in.txt", "r");
    f_out = fopen("out.txt", "w");

    fscanf(f_in, "%d", &tests);
    fgetc(f_in); //Remove newline

    for(i = 0; i < tests; ++i)
    {
        fscanf(f_in, "%d", &A);
        fscanf(f_in, "%d", &B);
        fgetc(f_in); //Newline

        count = 0; //Reset counter

        for(n = A; n <= B; ++n)
        {
            //Check all recycled pairs
            for(m = rotateInt(n); m != n; m = rotateInt(m))
                if(n < m && m <= B)
                    ++count;
        }

        //Print results to file
        fprintf(f_out, "Case #%d: %d\n", i+1, count);
    }

    fclose(f_in);
    fclose(f_out);
    return 0;
}
