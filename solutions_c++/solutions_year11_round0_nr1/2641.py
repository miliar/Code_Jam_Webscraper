#include<iostream>
#include<vector>
#include <stdio.h>

using namespace std;
struct block
{
    int type;
    int ind;
};
int main()
{
    freopen("A-large (1).in","rt",stdin);

    freopen("out.out","wt",stdout);
    int T;
    cin>>T;

    for(int TT=1;TT<=T;TT++)
    {
        int nT;
        cin>>nT;
        vector<int> W;
        vector<int> B;
        vector<block> bs;
        for(int i=0;i<nT;i++)
        {
            block h;
            char c;
            cin>>c;
            if(c=='B')
                h.type = 1;
            else
                h.type = 0;

            int hi;
            cin>>hi;

            h.ind = hi;

            if(h.type==1)
            {
                B.push_back(h.ind);
            }else
                W.push_back(h.ind);

            bs.push_back(h);

        }

            vector<int>B2;
              vector<int>W2;
              B2 = B;
              W2 = W;

        for(int i=1;i<B.size();i++)
        {
                B2[i] = max(B[i]-B[i-1] , (B[i]-B[i-1])*(-1)) ;
                B2[i] ++;
        }
        for(int i=1;i<W.size();i++)
        {
                W2[i] = max(W[i]-W[i-1] , (W[i]-W[i-1])*(-1)) ;
                W2[i]++;
        }
        B = B2;
        W = W2;

        if(B.size()==0)
            B.push_back(0);
        if(W.size()==0)
            W.push_back(0);
        int curW=0,curB=0;
        int totalTime = 0;
        for(int i=0;i<bs.size();i++)
        {
            if(bs[i].type == 1)
            {
                int help = B[curB];
                B[curB]-= help;
                W[curW]= max(W[curW]-help,1);
                curB++;
                totalTime += help;
            }else{
                int help = W[curW];
                W[curW] -= help;
                B[curB] = max(B[curB]-help,1);
                curW++;
                totalTime += help;
            }



    //     cout<<"total "<<totalTime<<endl;



        }
            cout<<"Case #"<<TT<<": "<<totalTime<<endl;




    }

}
