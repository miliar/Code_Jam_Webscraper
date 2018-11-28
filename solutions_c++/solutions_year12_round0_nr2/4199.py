#include<iostream>

using namespace std;

int main()
{
    int T;
    cin>>T;
    for(int t1=1;t1<=T;t1++)
    {
        int N,S,P;
        int t;
        cin>>N>>S>>P;
        int count=0;

        for(int i=0;i<N;i++)
        {
            cin>>t;
            if(t%3==0)
            {
                if(t/3>=P)
                    count++;
                else
                    if(int (t/3)+1>=P && S>0 && t>=2 && t <= 28)
                    {
                        count++;
                        S--;
                    }

            }
            else if(t%3==1)
            {
                if(int (t/3)+1>=P)
                {
                    count++;
                }
            }
            else if(t%3==2)
            {
                if(int (t/3)+1>=P)
                {
                    count++;
                }
                else if(int (t/3)+2 >=P && S>0 && t>=2 && t<=28)
                {
                    count++;
                    S--;
                }
            }
        }

        cout<<"Case #"<<t1<<": "<<count<<endl;
    }
return 0;
}
