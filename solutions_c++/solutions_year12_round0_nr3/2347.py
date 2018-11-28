#include <cstdlib>
#include <iostream>
#include<fstream>
#include<Math.h>

using namespace std;

int main(int argc, char *argv[])
{
    int test;
    int a,b,count,len,mul,rem,quo,temp;
    ifstream infile("C:\\Users\\Flirt-PC\\Desktop\\input_rec.txt");
    ofstream outf("C:\\Users\\Flirt-PC\\Desktop\\output_rec.txt");
    infile>>test;
    for(int i=1;i<test+1;i++)
    {
         count=0;   
         infile>>a;
         infile>>b;
         mul=10;
         while(mul<=a)
         {
                      mul=mul*10;
         }
         mul=mul/10;
         for(int j=a;j<=b;j++)
         {
                temp=j;
                rem=temp%10;
                quo=temp/10;
                temp=mul*rem+quo;
                while(temp!=j)
                {
                              if(temp>j && temp<=b)
                              {
                                        count++;      
                              }
                              rem=temp%10;
                              quo=temp/10;
                              temp=mul*rem+quo;
                } 
         } 
         outf<<"Case #"<<i<<": "<<count<<"\n";  
    }
    system("PAUSE");
    return EXIT_SUCCESS;
}
