#include<stdio.h>
#include<iostream>
#include<string.h>

using namespace std;

// Global Variables


int main()
{
    char filename[32], state[4];
	char infile[32]="A-large.in";
	FILE *fp=fopen(infile, "r");
    
    int a[31],n=30,i,j,tc,cases;
    unsigned long long int p[31],k, rem;
    
    for(i=0;i<=30;i++) { p[i]=1; for(j=1;j<=i;j++) p[i]*=2; }

    fscanf(fp, "%d", &cases);
    for(tc=1;tc<=cases;tc++)
	{
         fscanf(fp, "%d%d", &n, &k);
         rem = k % p[n];
         cout<<"Case #"<<tc<<": ";
         if (rem==(p[n]-1)) 
         {
             cout<<"ON"<<endl; 
         }
         else { cout<<"OFF"<<endl; }
    }  
    return 0;
}
