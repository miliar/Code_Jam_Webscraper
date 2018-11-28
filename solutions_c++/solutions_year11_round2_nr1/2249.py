#include <cstdio>
#include <math.h>
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <iomanip>
using namespace std;

int TC = 1, T, N;
int main ()
{
    FILE * p;

  p = fopen ("2Asource.txt","r+");
 std::ofstream os("2A.txt");
    for (fscanf (p,"%d", &T); TC <= T; TC++)
    {
        fscanf (p,"%d", &N);
        char zeichen[N][N];
        for (int i=0;i<N;i++)
        {
            char zeichen1[N];
            fscanf(p,"%s", &zeichen1);
            for (int j=0;j<N;j++)
            {
                zeichen[i][j]=zeichen1[j];
            }
        }
        os<<"Case #"<<TC<<":\n";
        //Berechnen
        //DER WP_________________________________
        int wp1[N],wp2[N];
        for (int i=0;i<N;i++)
        {
            wp1[i]=0;
            wp2[i]=0;
        }
        double wp[N];
        for (int i=0;i<N;i++)
        {
            for (int j=0;j<N;j++)
            {
                if (zeichen[i][j]=='0'){wp2[i]++;}
                else if (zeichen[i][j]=='1'){wp1[i]++;wp2[i]++;}
            }
            wp[i]=(double)wp1[i]/(double)wp2[i];
        }
        //DER OWP________________________________________
        double owp[N];
        int owpcount[N];
        double owpsum[N];
        for (int i=0;i<N;i++)
        {
            owpcount[i]=0;
            owpsum[i]=0;
            
        }
        for (int i=0;i<N;i++)
        {
            //os<<"Für Team "<<i<<":\n";
            for (int j=0;j<N;j++)
            {
                double owpsummand;
                if (zeichen[i][j]=='0'){
                   owpcount[i]++;
                   double owpx=double (wp1[j]-1);double owpy=double (wp2[j]-1);
                   //owpsum[i]+=(double)(wp1[j]-1)/(double)(wp2[j]-1);}
                   owpsummand=(double)owpx/(double)owpy;
                   owpsum[i]=(double)owpsum[i]+(double)owpsummand;
                   }
                else if (zeichen[i][j]=='1'){
                     owpcount[i]++;
                     double owpx=(double)wp1[j];double owpy=(double)wp2[j]-1;
                     //owpsum[i]+=(double)(wp1[j])/(double)(wp2[j]-1);
                     owpsummand=(double)owpx/(double)owpy;
                     owpsum[i]=owpsum[i]+(double)owpsummand;
                }
                //os<<"Team "<<j<<" hat WP "<<owpsummand<<"\n";
            }
            //os<<"Also OWP von "<<owpsum[i]<<" / "<<owpcount[i]<<"\n";
            owp[i]=(double)owpsum[i]/(double)owpcount[i];
        }
        //DER OOWP_____________________________________________________
        int oowpcount[N];
        double oowpsum[N];
        double oowp[N];
        for (int i=0;i<N;i++)
        {
            oowpcount[i]=0;
            oowpsum[i]=0;
            
        }
        for (int i=0;i<N;i++)
        {
            for (int j=0;j<N;j++)
            {
                if (zeichen[i][j]!='.'){oowpcount[i]++;oowpsum[i]+=(double)owp[j];}
            }
            //os<<"Also OOWP von "<<oowpsum[i]<<" / "<<oowpcount[i]<<"\n";
            oowp[i]=(double)oowpsum[i]/(double)oowpcount[i];
        }
        //DER RPI______________________________________________________
        double rpi [N];
        for (int i=0;i<N;i++)
        {
            rpi[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
        }
        for (int i=0;i<N;i++)
        {os<<setprecision(11)<<rpi[i]<<"\n";
        }
    }
    getch();
    return 0;
}
