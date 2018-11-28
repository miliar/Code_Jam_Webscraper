#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main()
{
    freopen("C-large (1).in","rt",stdin);

     freopen("out.out","wt",stdout);
    int T;
    cin>>T;

    for(int TT=1;TT<=T;TT++)
    {
        int nT;
        cin>>nT;
        vector<int>vn(nT,0);
        for(int i=0;i<nT;i++)
        {
            cin>>vn[i];
        }

        int vnh = vn[0];
        for(int i=1;i<nT;i++)
        {
            vnh = vnh^vn[i];
        }
        if(vnh!=0)
        {
            cout<<"Case #"<<TT<<": NO"<<endl;
            continue;
        }


        sort(vn.begin(),vn.end());
    //    cout<<vn[0];
        int curInd =1;
//cout<<"X" <<endl;
        for(;curInd<vn.size();curInd++)
        {
            int vn1 = vn[0];
            for(int i=1;i<curInd;i++)
            {
                vn1 = vn1^vn[i];
            }

            int vn2 = vn[curInd];
            for(int i=curInd+1;i<vn.size();i++)
            {
               // cout<<"X"<<vn2<<endl;
                vn2 = vn2^vn[i]; //cout<<"X"<<vn2<<endl;
            }
     //   cout<<vn1<<" "<<vn2<<endl;
            if(vn1==vn2)
            {
                int summ = 0;
                for(int i=curInd;i<vn.size();i++)
                {
                    summ+=vn[i];
                }
                cout<<"Case #"<<TT<<": "<<summ<<endl;

                break;
            }
        }





   // cout<<"Case #"<<TT<<": "<<totalTime<<endl;




    }

}
