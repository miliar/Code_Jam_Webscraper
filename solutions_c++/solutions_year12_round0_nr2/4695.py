
#include <iostream>
#include<fstream>
using namespace std;
void dancing();
ifstream din("abc12345.txt");
ofstream dout("out12345678.txt");
int testcount=1,N,S,p,numbers[100];
int main ()
{

    int t;
    din>>t;
    while(testcount<=t)
    {
        dancing();
        testcount++;
        //cout<<testcount<<" test count \n";
    }
    din.close();
    dout.close();
    return 0;
}
void dancing()
{
    //cout<<"N S p \n";
    din>>N>>S>>p;
    //cout<<"Input taken\n";
    for(int i=0;i<N;i++)
    {
        din>>numbers[i];
    }
    int count=0,scount=0,br;
    for(int i=0;i<N;i++)
    {
        int n=numbers[i];
        if(n%3==0)
        {
            br=n/3;
        }
        else
        {
            br=(n/3)+1;
        }
        if(br>=p)
            count++;
        else if(p-br==1&&n%3!=1&&n>=3)
        {
            if(scount<S)
            {
                count++;
                scount++;
            }
        }
    }
    dout<<"Case #"<<testcount<<": "<<count<<endl;
}
