#include <iostream>
#include<fstream>
#include<math.h>
using namespace std;
void fun();
ifstream din("abcd1111.txt");
ofstream dout("output1234.txt");
int testcase =1;
int main()
{
    int t;
    din>>t;
    while(t--)
    {
        fun();
    }
    return 0;
}
void fun()
{

    int A,B,nod=0,count=0,tnod,ext_dig=10;
    din>>A>>B;
    int temp=A;
    //cout<<pow(10,2);
    while(temp!=0)
    {
        temp=temp/10;
        nod++;
    }
    for(int n=A;n<=B;n++)
    {   ext_dig=10;
        tnod=nod;
       // cout<<" no of digits "<<nod<<endl;
        while(tnod--)
        {
            int d=n%ext_dig;
            int m=d*pow(10,tnod)+(n/ext_dig);
           // cout<<"n :"<<n<<" m : "<<m<<" "<<endl;
            if(m>n&&m<=B)
            {
                count++;
                //cout<<"("<<n<<","<<m<<") "<<count<<endl;

            }
            ext_dig=ext_dig*10;
        }
    }
    dout<<"Case #"<<testcase<<": "<<count<<endl;
    testcase++;

}
