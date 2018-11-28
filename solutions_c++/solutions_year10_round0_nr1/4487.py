#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int solve(int n,int k)
{
    int snappers[n];
    int power[n+1];
    memset(snappers,0,n*4);
    memset(power,0,(n+1)*4);
    power[0] = 1;
    int i,j;
    for(i = 0; i< k ; i++)
    {
        for(j=0; j<n; j++)
            if(power[j])
                snappers[j] = !snappers[j];
        for(j=0; j<n; j++)
        {
            if(power[j] && snappers[j])
                power[j+1] = 1;
            if(!snappers[j])
                power[j+1] = 0;
        }
    }
    return(power[n] && snappers[n-1]);
}

int main()
{
    int test_cases,n,k;
    FILE * infile = fopen("A-small.in","r");
    FILE * outfile = fopen("A-small.out","w");
    fscanf(infile,"%d",&test_cases);
    for(int i=0; i<test_cases; i++)
    {
        fscanf(infile,"%d %d",&n,&k);
        int result = solve(n,k);
        if(result)
            fprintf(outfile,"Case #%d: ON\n",i+1);
        else
            fprintf(outfile,"Case #%d: OFF\n",i+1);
    }
}
