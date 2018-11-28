#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    int T;
    cin>>T;
    int caseno=0;

    while(T--)
    {
        caseno++;
        int N,S,P;
        cin>>N>>S>>P;
        int count=0;

        for(int i=1;i<=N;i++)
        {
            int ti;
            cin>>ti;

            if(ti>=3*P)
            {
                count++;
                continue;
            }
            else
            {
                if(P-1>=0)
                {
                    if(ti==(3*P-1))
                    {
                        count++;
                        continue;
                    }
                    else if(ti==(3*P-2))
                    {
                        count++;
                        continue;
                    }
                    else if(P-2>=0)
                    {
                        if(ti==(3*P-3) && S)
                        {
                            count++;
                            S--;
                            continue;
                        }
                        else if(ti==(3*P-4) && S)
                        {
                            count++;
                            S--;
                            continue;
                        }

                    }
                }
            }
        }
        cout<<"Case #"<<caseno<<": "<<count<<endl;

    }
    return 0;
}
