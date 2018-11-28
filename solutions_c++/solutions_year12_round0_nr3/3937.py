#include<iostream>
#include<cstdio>
#include<math.h>

using namespace std;
#define TOTAL 2000000
int arr[TOTAL];
long getlen(long num)
{
    long temp,len;
     temp = num;
        while(temp)
        {
            temp = temp/10;
            len++;

        }

return len;
}


long generateAllPermutation(long num,long A,long B,long len)
{

       long temp,temp2,count2;


        temp = num;
        count2 = 1;

       for(long i=0;i<len-1;i++)
       {
           temp2 = temp%10;
           temp =temp/10;
           temp = temp2*pow(10,len-1)+temp;
          // cout<<temp<<endl;

           if((temp<=B && temp>=A)&&temp!=num&&arr[temp-A]!=1)
           {
              count2++;
            //  cout<<temp<<endl;
              arr[temp-A] = 1;
           }
       // cout<<"count2 : "<<count2;

       }
       return (count2*(count2-1))/2;
}

int main()
{

    long count,T,A,B,t,len;
    cin>>T;
    t = T;
    while(T)
    {
        cin>>A>>B;
        len = getlen(A);
        count = 0;
        for(long i=A;i<=B;i++)
        arr[i-A] = 0;

    for(long i=A;i<=B;i++)
    {
        if(arr[i-A]==0)
        {
            //cout<<"count : "<<count<<endl;
           count = count + generateAllPermutation(i,A,B,len);
        }

    }

cout<<"Case #"<<(t-T+1)<<": "<<count<<endl;
//cout<<count<<endl;
T--;

    }




    return 0;
}
