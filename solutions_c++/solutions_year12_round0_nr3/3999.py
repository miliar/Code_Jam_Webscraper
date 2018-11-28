#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
int numberOfDigitsInNumber(long int);
long int rotateNumbers(long int, int);

int main()
{
    FILE *ip = fopen("C-large.in","r");
    FILE *op = fopen("C-Output-Large.txt","w");

    int t;
    long int count;
    fscanf(ip,"%d",&t);
   //cin>>t;
    for(int z=1; z<=t; z++)
    {


        long int A,B;
        fscanf(ip,"%ld%ld",&A,&B);

        count = 0;
        int numberOfDigits = numberOfDigitsInNumber(A);

        for(long int i=A;i<B;i++)
        {

            long int number;
            long int dup[10];
            for(int j=1; j<numberOfDigits; j++)
            {
                number = rotateNumbers(i,j);
                dup[j-1] = number;

                int flag = -1;
                for(int k = 0; k < j; k++)
                {
                    if(dup[j-1] == dup[k])
                        flag++;
                }

                if(flag==0)
                    if(number>=A && number<=B && number>i)
                    {
                        count++;
                    }
            }

        }
        fprintf(op,"Case #%d: %ld\n",z, count);
    }
    return 0;
}


long int rotateNumbers(long int n, int times)
{

        int noOfDigits = numberOfDigitsInNumber(n);
        long int rotation = (long int)(pow(10,times)+0.1);

        long int rem = n%rotation;
        long int quo = n/rotation;

        long int factor = (int)(pow(10,(noOfDigits-times))+0.1);

     //   printf("Number: %d, Quo: %d, Rem: %d, factor: %d\n", n, quo, rem, factor);

        n =  factor * rem + quo;

        return n;
}

int numberOfDigitsInNumber(long int n)
{
        int numberOfDigits = 0;
        long int num = n;
        while(num!=0)
        {
            num = num/10;
            numberOfDigits++;
        }
        return numberOfDigits;
}
