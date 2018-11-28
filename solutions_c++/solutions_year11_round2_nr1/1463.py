#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
    fstream fout, fin;
    fout.open("output.txt");
    fin.open("input.txt");
    int t, T, N;
    fin>>T;
    for(t=1; t<=T; ++t)
    {
        fin>>N;
        int M[101*101]={0};
        char c;
        double wp[101]={0}, owp[101] = {0}, oowp[101] = {0}, RPI[101] = {0};
        int WP[101] = {0},  totalgames[101]={0}, totalowp[101] = {0}, totaloowp[101] = {0};
        for(int n=0; n<N; ++n)
        {
            for(int m=0; m<N; ++m)
            {
            fin>>c;
            if(c=='.')
                M[n*N+m] = -1;
            else if(c=='1')
                M[n*N+m] = 1, WP[n]+=1, totalgames[n]+=1;
            else if(c=='0')
                M[n*N+m] = 0, totalgames[n]+=1;
            else return -1;
            }
            wp[n] = (double)WP[n]/(double)totalgames[n];
        }
        for(int m=0; m<N; ++m)
        {
            for(int n=0; n<N; ++n)
            {
                if(M[n*N+m]!=-1)
                    owp[m] += (WP[n]-M[n*N+m])/(double)(totalgames[n]-1), totalowp[m]+=1;
            }
            owp[m] = owp[m] / totalowp[m];
        }
        for(int n=0; n<N; ++n)
        {
            for(int m=0; m<N; ++m)
            {
                if(M[n*N+m]!=-1)
                    oowp[n] += owp[m], totaloowp[n]+=1;
            }
            oowp[n] = oowp[n] / totaloowp[n];
        }
        fout<<"Case #"<<t<<":"<<endl;
        for(int n=0; n<N; ++n)
        {
            RPI[n] = 0.25*wp[n] + 0.5*owp[n] + .25*oowp[n];
            fout.precision(12);
            fout<<RPI[n]<<endl;
        }
    }

}
