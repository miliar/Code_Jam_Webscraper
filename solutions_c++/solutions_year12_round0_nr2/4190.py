#include<iostream>
using namespace std;
int main()
{
    long long test,q=1;
    cin>>test;
    while(test--)
    {
    long long n,p,k,i,x,m=0;
    cin>>n>>k>>p;
    //cout<<n<<" "<<k<<" "<<p<<" ";
    for(i=0;i<n;i++)
    {
        cin>>x;
       //  cout<<x<<" ";
      //  cout<<m<<endl;
        if(p==0)
        {
            m=n;
        }
        else
        {
        if(x>=((p*3)-2))
            {
                m++;
            }
        if(p!=1)
        {
            if((x>=((p*3)-4))&&(x<((p*3)-2))&&(k>0))
            {
                m++;
                k--;
            }
        }
        }

    }
    //cout<<endl;
    cout<<"Case #"<<q<<": "<<m<<endl;
    q++;
    }

}

