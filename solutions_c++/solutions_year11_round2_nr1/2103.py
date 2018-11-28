#include <fstream>
#include <iostream>

using namespace std;

int main()
{
    ifstream fin("input.in");
    ofstream fout("output.in");
    int test;
    fin>>test;
    for(int i=1;i<=test;i++)
    {
        fout<<"Case #"<<i<<":"<<endl;
        int n;
        fin>>n;
        char **init=new char*[n];
        double *totals=new double[n];
        double *wins=new double[n];
        double *owp=new double[n];
        for(int j=0;j<n;j++)
        {
            char ch;
            init[j]=new char[n];
            double total=0;
            double win=0;
            for(int k=0;k<n;k++)
            {
                fin>>ch;
                init[j][k]=ch;
                if(ch=='1')
                {
                    total++;
                    win++;
                }
                else if(ch=='0')
                {
                    total++;
                }
            }
            totals[j]=total;
            wins[j]=win;
            //fout<<"win"<<wins[j]<<"total"<<totals[j]<<endl;
        }

        for(int j=0;j<n;j++)
        {
            double avg=0;
            double count=0;
            for(int k=0;k<n;k++)
            {
                double twin=wins[k];
                double ttotal=totals[k];
                if(k==j)
                continue;
                if(init[k][j]=='1')
                {
                        twin--;
                        ttotal--;
                        count++;

                if(ttotal!=0)
                avg+=twin/ttotal;
                }
                else if(init[k][j]=='0')
                {
                    ttotal--;
                    count++;


                if(ttotal!=0)
                avg+=twin/ttotal;
                }
            }
            avg=avg/count;
            owp[j]=avg;
            //fout<<"owg"<<owp[j];
        }
        for(int j=0;j<n;j++)
        {
            double avg=0;
            double count=0;
            for(int k=0;k<n;k++)
            {
                if(j==k)
                continue;
                if(init[j][k]=='1'||init[j][k]=='0')
                {
                    count++;
                    avg+=owp[k];
                }
            }
            avg=avg/count;
            double rpi=((double)0.25)*(wins[j]/totals[j]);
            rpi+=((double)0.5)*owp[j];
            rpi+=((double)0.25)*avg;
           // fout<<"avh"<<avg<<endl;
            fout.precision(7);
            fout<<rpi<<endl;
        }
        for(int j=0;j<n;j++)
        {
            delete[] init[j];
        }
        delete[] totals;
        delete[] wins;
        delete[] owp;

    }
    return 0;
}
