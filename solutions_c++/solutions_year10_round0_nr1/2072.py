#include<iostream>
#include<math.h>
//#include<conio.h>

using namespace std;

int compute_state(long n, long k)
{
    long int temp = pow(2,n);
    //cout<<"temp "<< temp<<"\n";
    long dup = k-(temp-1);
    //cout<<"dup "<< dup<<"\n";
    if(dup == 0)
    return(1);
    else if(dup%temp == 0)
    return(1);
    else
    return(0);
}

int main()
{
    int tc;
    long int n,k;
    int i =0;
    cin>>tc;
    while(i<tc)
    {
               cin>>n>>k;
               if (compute_state(n,k) == 1)
               {
                  cout<<"Case #"<<i+1<<": "<<"ON\n";
               }
               else if(compute_state(n,k) == 0)
               {
                                       cout<<"Case #"<<i+1<<": "<<"OFF\n";
                                       
               }
               i++;
               
    }
    //getch();
               
}              //End of main()
