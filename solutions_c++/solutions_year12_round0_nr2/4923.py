#include <iostream>
using namespace std;
int main()
{
    int t;
    int n;
    int s,sTmp;
    int p;
    int gs;
    int greater;
    int canNotSurprise;

    int i,j;

    cin >> t;
    for (i=0; i<t; i++)
    {
        canNotSurprise=0;
        greater=0;
        cin>>n>>s>>p;
        sTmp=s;
        for (j=0; j<n; j++)
        {
            cin>>gs;
            if (gs>=(3*p))
                greater++;
            else if (((gs+1)>=(3*p))&&(gs>=1))
                greater++;
            else if (((gs+2)>=(3*p))&&(gs>=2))
                greater++;
            else if (((gs+3)>=(3*p))&&(sTmp>0)&&(gs>3))
            {
                greater++;
                sTmp--;
            }
            else if (((gs+4)>=(3*p))&&(sTmp>0)&&(gs>4))
            {
                greater++;
                sTmp--;
            }

            if ((gs<2)||(gs>28))
                canNotSurprise++;
        }
        if (canNotSurprise+s>n)
            greater=greater-(canNotSurprise+s-n);

        cout <<"Case #"<<i+1<<": "<< greater<<endl;
    }
    return 0;
}
