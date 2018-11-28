#include <iostream>
#include <fstream>
#include "stdlib.h"
using namespace std;

bool cycle(int i,int j)
{
    int temp;
        char bufferi[5];
        char bufferj[5];
        itoa (i,bufferi,10);
        itoa (j,bufferj,10);
        string a=bufferi;
        string b=bufferj;

        for(int h=0; h<a.size(); h++)
        {
            temp=a[a.size()-1];
            for(int k=a.size()-1; k>0; k--)
            {
                a[k]=a[k-1];
            }
            a[0]=temp;
            if(a==b){return true;}
        }
        return false;
}

int main ()
{
    int a,b,n,count;
    ifstream input("C-small-attempt3.in");
    ofstream output ("out.txt", ios::app);
    input>>n;
    for(int h=1; h<=n; h++)
    {
        count=0;
        input>>a>>b;
        for(int i=a; i<=b; i++)
        {
            for(int j=a; j<=b; j++)
            {
                if(i!=j && (cycle(i,j)))
                    count++;
            }
        }
        output<<"Case #"<<h<< ": " << count/2 <<endl;
    }
    input.close();
    output.close();
    return 0;
}
