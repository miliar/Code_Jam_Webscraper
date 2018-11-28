#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int t, c=1;
    cin>>t;
    while(t--)
    {
        double n, p1, p2;
        cin>>n>>p1>>p2;
        bool poss = false;
        for(double i=1;i<=n;i++)
        {
            if(i*p1/100==floor(i*p1/100))
            {
                poss = true;
            }
        }
        if(p2==100 && p1!=100)
            poss = false;
        if(p2==0 && p1!=0)
            poss = false;
        cout<<"Case #"<<c++<<": ";
        if(poss)
        {
            cout<<"Possible";
        }
        else
        {
            cout<<"Broken";
        }
        cout<<endl;
    }
    return 0;
}
