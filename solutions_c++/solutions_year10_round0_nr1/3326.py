#include<stdio.h>
#include<math.h>
#include<fstream>
using namespace std;
int main()
{
 int T,i;
 char arr1[]="Case #";
 char arr2[]="OFF";
 char arr3[]="ON";
 ifstream infile;
 infile.open("input.txt");
 ofstream outfile("output1.txt");
 if(infile.is_open())
 {
  infile>>T;
  for(i=1;i<=T;i++)
  {
           int n,k,j,sum=0;
           infile>>n;
           infile>>k;
           for(j=0;j<n;j++)
                            sum=sum+(1<<j);
           if(sum>k)
           {
            outfile<<arr1<<i<<": "<<arr2<<endl;
           }
           else
           {
               k=k-sum;
               sum=(1<<j)-1;
               printf("%d%d",k,sum);
               if((k&sum)==0)
                           outfile<<arr1<<i<<": "<<arr3<<endl;
               else
                           outfile<<arr1<<i<<": "<<arr2<<endl;
           }
  }
}
infile.close();
outfile.close();
return 0;
}
