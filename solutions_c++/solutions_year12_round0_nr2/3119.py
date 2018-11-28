#include<iostream>

using namespace std;

int main()
{
    int c;
    cin>>c;
    int cs;

    for(cs=1;cs<=c;cs++)
    {
        int n,s,p;
        cin>>n>>s>>p;
        int f=0;

        for(int i=1;i<=n;i++)
        {
            int t;
            cin>>t;

            if(t>=p*3)
            {
                f++;
            }
            else
            {
                if(p-1>=0)
                {
                    if(t==(3*p-1))
                                  f++;
                    else if(t==(3*p-2))
                                       f++;
                    else if(p-2>=0)
                    {
                        if(t==(3*p-3) && s)
                        {
                            f++;
                            s--;
                        }
                        else if(t==(3*p-4) && s)
                        {
                            f++;
                            s--;
                        }

                    }
                }
            }
        }
        cout<<"Case #"<<cs<<": "<<f<<endl;

    }
}
