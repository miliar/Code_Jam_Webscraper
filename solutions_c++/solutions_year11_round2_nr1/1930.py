#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;

int maz[101][101];
double WB[101];
double OWB[101];
double OOWB[101];
double fin[101];
int main()
{
    freopen("A-large (2).in","rt",stdin);

     freopen("out.out","wt",stdout);
    int T;
    cin>>T;

    for(int TT=1;TT<=T;TT++)
    {
        int N;
        cin>>N;

        for(int i=0;i<N;i++)
        {
            WB[i]=0;
            OWB[i]=0;
            OOWB[i]=0;
            fin[i]=0;
        }
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
            {
                char hc;
                cin>>hc;

                if(hc=='1')
                {
                    maz[i][j]=1;

                }else if(hc == '0')
                {
                    maz[i][j]=0;
                }else{
                    maz[i][j]=-1;
                }
            }
        }

            for(int i=0;i<N;i++)
            {
                int cW=0;int cL=0;

                for(int j=0;j<N;j++)
                {
                    if(maz[i][j]==1)
                    {
                        cW++;
                    }else if(maz[i][j]==0)
                    {
                        cL++;
                    }
                }
                WB[i] = (double)cW/(double)(cW+cL);
               // cout<<cW<<" "<<cL<<endl;


            }

            for(int i=0;i<N;i++)
            {

                double hOWB=0;
                int np =0 ;
                for(int j=0;j<N;j++)
                {
                    if(maz[i][j]==-1)
                    {
                        continue;
                 //      np++;
                   //hOWB += WB[j];
                    }
                    else
                    {
                        np++;
                        int cW=0;
                        int cL=0;
                        double newWB;
                        for(int x=0;x<N;x++)
                        {
                            if(x==i) continue;
                            if(maz[j][x]==1) cW++;
                            else if(maz[j][x]==0) cL++;

                        }
                        newWB = (double)cW/(double)(cW+cL);
                        hOWB +=newWB;

                     //   cout<<"X"<<newWB<<endl;

                    }

                }  //  cout<<"Z"<<endl;
                    hOWB /= (double)np;

                    OWB[i] = hOWB;
            }






        for(int i=0;i<N;i++)
        {  int nnn=0;
            for(int j=0;j<N;j++)
            {
                if(maz[i][j]!=-1)
                {OOWB[i]+=OWB[j];
                 nnn++;
                }
            }
            OOWB[i]/=nnn;
        }
        cout<<"Case #"<<TT<<":"<<endl;
        for(int i=0;i<N;i++)
        {
       //   cout<<WB[i]<<" "<<OWB[i]<<" "<<OOWB[i]<<endl;
            fin[i] = 0.25*WB[i] + 0.5*OWB[i] + 0.25*OOWB[i];
            cout<<fin[i]<<endl;
        }

    }

}
