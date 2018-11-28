#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int T,wynik, A,B,m,n,tmp,lc=0;
    char tab1[8], tab2[8];
    bool jest;
    cin >> T;
    for(int t =0;t<T;t++)
    {
        wynik=0;
        lc=0;
        cin >> A;
        cin >> B;
        tmp=A;
        while(tmp!=0)
        {
            lc++;
            tmp/=10;
        }
        for(m=A;m<B;m++)
        {
            for(n=m+1;n<=B;n++)
            {
                sprintf(tab1,"%d",m);
                sprintf(tab2,"%d",n);

                for(int p=0;p<lc;p++)
                {   jest=true;
                    for(int k=0;k<lc;k++)
                    {
                        if(p+k<lc)
                        {
                            if(tab1[k]==tab2[p+k])
                            {
                                continue;
                            }
                            else
                            {
                                jest=false;
                                break;
                            }
                        }
                        else
                        {
                            if(tab1[k]==tab2[p+k-lc])
                            {
                                continue;
                            }
                            else
                            {
                                jest=false;
                                break;
                            }
                        }
                    }
                    if(jest)
                    {
                        wynik++;
                        break;
                    }
                }
            }
        }
        cout << "Case #"<<t+1<<": "<< wynik<<endl;
    }
    return 0;
}
