#include <iostream>
using namespace std;
int C,A,M,N;
int main()
{
    int Ci,x1,y1,x2,y2;
    bool flag;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    cin>>C;
    for (Ci=1;Ci<=C;Ci++)
    {
        cin>>N>>M>>A;
        flag=true;
        cout<<"Case #"<<Ci<<": ";
        for (x1=0;x1<=N;x1++) if (flag)
            for (y1=0;y1<=M;y1++) if (flag)
                for (x2=0;x2<=N;x2++) if (flag)
                    for (y2=0;y2<=M;y2++) if (flag)
                        if (abs(x1*y2-x2*y1)==A)
                        {
                            cout<<"0 0 "<<x1<<' '<<y1<<' '<<x2<<' '<<y2<<endl;
                            flag=false;
                            break;
                        }
        if (flag)
            cout<<"IMPOSSIBLE"<<endl;
    }
    //system("pause");
}
