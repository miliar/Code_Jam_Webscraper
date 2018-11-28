#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <stack>
#include <vector>
using namespace std;

long C(long m, long n) 
{ 
    long result=1; 
    if (n>m-n) 
    { 
        n=m-n; //C(m,n)==C(m,m-n) 取较小的来计算 
    } 
    for (int i=1;i<=n;i++) 
    { 
        result*=(long)((double)(m-n+i)/i);// 
    } 
    return result; 
}

int main()
{
    ifstream inputFile;
    ofstream outputFile;

    inputFile.open("C-small-attempt0.in");
    outputFile.open("C-small-attempt0.out");

    int T;
    int i,j,k;
    int A,B;
    int const sz = 2000001;
    int* table= new int[sz];

    int count;
    int rel;
    int temp;
    int base;
    int ex;

    while(inputFile>>T)
    {
        for (i=0;i<T;i++)
        {
            rel=0;
            memset(table,0,sizeof(int)*sz);
            inputFile>>A;
            inputFile>>B;

            temp=B;

            base=1;
            ex=0;
            while(temp/10!=0)
            {
                base*=10;
                ex++;
                temp/=10;
            }

            for (j=A;j<=B;j++)
            {
                if (table[j]!=0)
                {
                    continue;
                }

                temp=j;
                count=1;
                for(k=0;k<ex;k++)
                {
                    int post=temp/base;
                    temp=(temp%base)*10+post;
                    if(temp<=B&&temp>=A&&temp!=j)
                    {
                        if(table[temp]==0)
                        {
                            count++;
                        }
                        table[j]+=1;
                        table[temp]+=1;
                    }
                }
                if(count!=1)
                {
                    rel+=C(count,2);
                }

            }
            outputFile<<"Case #"<<i+1<<": ";
            outputFile<<rel<<endl;
        }

    }

    system("pause");
    return 0;
}