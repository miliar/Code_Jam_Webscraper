#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("p2small1.out","w",stdout);
    int T;
    cin>>T;
    for (int asd=0; asd<T; asd++)
    {
        int N,S,P;
        cin>>N>>S>>P;
        int tot=0;
        for (int i =0; i<N; i++)
        {
            int G;
            cin>>G;
            int D=G/3;
            if (G%3 !=0 and G>1)
                D++;
             if (D>=P)
                tot++;
            else if (D+1==P and S>0 and G>2)
            {
                S--;
                tot++;
            }
        }
        cout<<"Case #"<<asd+1<<": "<<tot<<endl;
    }
}
