#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main()
{
    freopen("C-small-attempt0(3).in","rt",stdin);

      freopen("out.out","wt",stdout);
    int T;
    cin>>T;

    for(int TT=1;TT<=T;TT++)
    {
        //cout<<10%20<<endl;
        int N,L,H;
        cin>>N>>L>>H;
        vector<int>pp;
        for(int i=0;i<N;i++)
        {
            int h;
            cin>>h;
            pp.push_back(h);
        }
        bool isFin=0;
        cout<<"Case #"<<TT<<": ";
        for(int x=L;x<=H;x++)
        {
            bool isGood=1;
          //  cout<<x<<endl;
            for(int i=0;i<N;i++)
            {
                int n1,n2;
                n1=max(x,pp[i]);
                n2=min(x,pp[i]);

                if(n1%n2!=0&&pp[i]!=1)
                {
                   // cout<<"!"<<pp[i]<<" "<<x%pp[i]<<endl;
                    isGood = 0;
                    break;

                }
            }

            if(isGood)
            {
                isFin=1;
                cout<<x<<endl;
                break;
            }
        }
        if(!isFin)
        cout<<"NO"<<endl;
    }

}
