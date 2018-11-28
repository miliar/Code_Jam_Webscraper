#include<iostream>
#include<cmath>
using namespace std;

bool func(int n, int m)
{
    int orig = n;
    if(n !=m)
    {
        int digs = log10(n)+1;
        //cout<<digs<<endl;
        int exp=pow(10, digs-1);
        //cout<<"exp = "<<exp<<endl;

        for(int i =1 ; i < digs; i++)
        {
            int dig = n%10;
            n/=10;
            n+= dig*exp;
            //cout<<n<<" versus "<<m<<endl;
            if(n ==m)
            {
             //   cout<<orig<<"  "<<m<<endl;
                return true;
            }

        }
    }
    return false;
}

int main()
{

    int cont = 0;
    int ini = 1111;
    int num = 2000000;

    int cases;
    cin>>cases;
    for(int k = 1; k <= cases; k++)
    {
        cont = 0;
        cin>>ini>>num;
        for(int i = ini; i <= num; i++)
        {
            for(int j = i+1; j<=num; j++)
            {
                //cout<<i<< " "<<j<<endl;
                if(func(i, j))
                {
                    cont++;
                }
            }
        }
        cout<<"Case #"<<k<<": "<<cont<<endl;
    }

    //func(1234, 1000);

    return 0;
}
