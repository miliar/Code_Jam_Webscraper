#include <iostream>

using namespace std;

int min(int x)
{
    int y;
    for(y=1;y<=100;y++)
        if((y*x)%100==0)
            return y;
}

int main()
{
    long long int T,a,b,c,x;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        cin>>a>>b>>c;
        if(c==0)
        {
            if(b==0)
            {
                cout<<"Case #"<<i<<": Possible"<<endl;
                continue;
            }
            else
            {
                cout<<"Case #"<<i<<": Broken"<<endl;
                continue;
            }

        }
        if(c==100)
        {
            if(b==100)
            {
                cout<<"Case #"<<i<<": Possible"<<endl;
                continue;
            }
            else
            {
                cout<<"Case #"<<i<<": Broken"<<endl;
                continue;
            }

        }
        x=min(b);
        if(x<=a)
        {
            cout<<"Case #"<<i<<": Possible"<<endl;
            continue;
        }
        else
        {
            cout<<"Case #"<<i<<": Broken"<<endl;
            continue;
        }
    }
    return 0;
}
