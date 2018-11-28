#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <iostream>
#include <set>

using namespace std;
int main()
{
    int nr;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> nr;
    int nrtot = 0;
    int nrc=0;


    for (int i=0;i<nr;i++)
    {
        int a,b;
        cin >> a >> b;

        int aux=a;
        int total=1;
        while (aux!=0)
        {
            nrc++;
            aux/=10;
            total*=10;
        }

        nrtot=0;
        for (int j=a;j<=b;j++)
        {
            set <int> hs;
            int p=1;
            while (p<=j)
            {
                int temp = (j/p) + j%p * (total/p);
                if ((temp<= b)&&(temp>=a)&&(temp>j))
                {
                    //nrtot++;
                    hs.insert(temp);
//                    cout << j <<"   " <<temp <<endl;
                }

                p*=10;
            }
            nrtot+= hs.size();


        }
        cout <<"Case #"<<i+1<<": "<< nrtot<<endl;
    }

    return 0;
}
