#include <iostream>
#include <fstream>
using namespace std;

int main()
{
   ifstream input("C:\\Users\\Mimo\\Desktop\\B-large.in");
   ofstream output;
   output.open("output.txt");
   int t,n,s,p,result;
   int* input1 ;
   int* input2 ;
   int *input3;
   int base,difference;
   input>>t;
   for(int i=1;i<=t;i++)
   {
       result=0;
       input>>n;
       input>>s;
       input>>p;
       base=p*3;
        int* sum=new int[n];
        input1=new int[n];
       for(int j=0;j<n;j++)
        input>>sum[j];
        for(int j=0;j<n;j++)
        {
           difference=base-sum[j];
           if(difference<3)
           result++;
           else if (difference < 5 && s > 0 && p > 1)
                    {
                       result++;
                        s--;
                    }
        }

       output<<"Case #"<<i<<": "<<result<<endl;
   }
    return 0;
}
