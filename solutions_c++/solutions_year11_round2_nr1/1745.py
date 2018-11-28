#include <cstdio>
#include <iostream>
using namespace std;
#define MAX 128

int main()
{
    double RPI[MAX];
    double WP[MAX];
    double OWP[MAX];
    double OOWP[MAX];
    char schedule[MAX][MAX];
    int t,n;
    
    scanf("%d",&t);
    for(int c=1;c<=t;c++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%s",schedule[i]);
        for(int i=0;i<n;i++)
        {
            double win=0.0,total=0.0;
            for(int j=0;j<n;j++)
                if(schedule[i][j]!='.')
                {
                    total++;
                    if(schedule[i][j] == '1')
                        win++;
                }
            WP[i] = win/total;
        }
        for(int i=0;i<n;i++)
        {
            double total=0.0,sum=0.0;
            for(int j=0;j<n;j++)
                if(schedule[i][j]!='.')
                {
                    total++;
                    //sum+=WP[j];
                    double tmpTot=0.0,tmpWp=0.0;
                    for(int k=0;k<n;k++)
                    {
                        if(k!=i && schedule[j][k]!='.')
                        {
                            tmpTot++;
                            if(schedule[j][k] == '1')
                                tmpWp++;
                        }
                    }
                    //cout << endl << tmpWp << " " << tmpTot << endl;
                    tmpWp = tmpWp/tmpTot;
                    sum += tmpWp;
                }
            OWP[i] = sum/total;
            //cout << "OWP: " << OWP[i] << endl;
//            printf("%lf\n",OWP[i]);
        }
        for(int i=0;i<n;i++)
        {
            double total=0.0,sum=0.0;
            for(int j=0;j<n;j++)
                if(schedule[i][j]!='.')
                {
                    total++;
                    sum+=OWP[j];
                }
            OOWP[i] = sum/total;
        }
        printf("Case #%d:\n",c);
        for(int i=0;i<n;i++)
        {
            RPI[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
            //cout<< WP[i] << " " << OWP[i] << " " << OOWP[i] << " " << RPI[i]<<endl;
            cout<< RPI[i] << endl;
        }
    }

    return 0;
}
