#include<iostream>
#include<cmath>
using namespace std;
int giveNoOfDigit(int n);
int makePower(int base,int exp);

int main()
{
    int i,j,k;
    int low,high,testCase;
    int count,noOfDigit,lastDigits,firstDigits,temp,pair;
    cin>>testCase;
    for(int t=0;t<testCase;t++)
    {
        count=0;
        cin>>low>>high;
        noOfDigit=giveNoOfDigit(low);
       // cout<<"digit  :"<<noOfDigit<<endl;
        for(i=0;i<noOfDigit-1;i++)
        {
            for(j=low;j<high;j++)
            {

                lastDigits=j%(makePower(10,(i+1)));

                firstDigits=j/makePower(10,(i+1));
      //          cout<<j<<" "<<lastDigits<<" "<<firstDigits<<endl;

                temp=lastDigits*makePower(10,(noOfDigit-i-1));
     //           cout<<i<<" "<<makePower(10,3);
    //            cout<<"temp :"<<temp<<endl;
                pair=temp+firstDigits;
                //cout<<i+1<<" ";
                if(pair<=high && pair>j)
                {
                    count++;
                   // cout<<"now  "<<j<<endl;
                   // cout<<"generated : "<<pair<<endl;
                   // cout<<"cnat :"<<count<<endl;

                }
                else if(j!=pair)
                {
                    //cout<<"breakig for  :"<<pair<<endl;
                   // cout<<count<<endl;
                   // break;
                }


            }
        }

        cout<<"Case #"<<t+1<<": "
        <<count<<endl;
    }

    return 0;
}

int giveNoOfDigit(int n)
{
    int cnt=0;
    while(n=n/10)
    {
        cnt++;
    }
    return ++cnt;
}

int makePower(int base,int exp)
{
    int res=base;
    for(int i=1;i<exp;i++)
    {
         res= res*base;
    }
    return res;
}
