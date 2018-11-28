#include <iostream>
#include<vector>
#include<set>
using namespace std;

int main()
{

    int i,j,k,T,N,mecz,wygr,l;
    double tymowp,wynik;
    char a;
    cin>>T;
    for(i=0;i<T;i++)
        {
            cin>>N;
            int tab[N][N];
            double mecz[N][5];
            for(j=0;j<N;j++)
            {
                for(k=0;k<5;k++)
                {
                    mecz[j][k]=0;
                }
            }
            for(j=0;j<N;j++)
            {
                for(k=0;k<N;k++)
                {
                    cin>>a;
                    if(a=='.') tab[k][j]=-1;
                    else
                    {
                        mecz[j][0]++;
                        if(a=='1')
                        {
                             mecz[j][1]++;
                             tab[k][j]=1;
                        }
                        else tab[k][j]=0;
                    }
                }
            }
            for(j=0;j<N;j++)
            {
                mecz[j][2]=mecz[j][1]/mecz[j][0];
            }
            for(j=0;j<N;j++)
            {
                tymowp=0;
                l=0;
                for(k=0;k<N;k++)
                {
                    if(j!=k&&tab[k][j]!=-1)
                    {
                        l++;
                        if(tab[k][j]==0)
                        {
                            tymowp+=(mecz[k][1]-1)/(mecz[k][0]-1);
                        }
                        else tymowp+=(mecz[k][1])/(mecz[k][0]-1);
                    }
                }
                mecz[j][3]=tymowp/l;
            }
            for(j=0;j<N;j++)
            {
                tymowp=0;
                l=0;
                for(k=0;k<N;k++)
                {
                    if(j!=k&&tab[k][j]!=-1)
                    {
                        l++;
                       tymowp+=mecz[k][3];
                    }
                }
                mecz[j][4]=tymowp/l;
            }
            cout<<"Case #"<<i+1<<":"<<endl;
            for(j=0;j<N;j++)
            {
                wynik=0.25*mecz[j][2]+ 0.50 *mecz[j][3]+ 0.25 *mecz[j][4];
                printf("%f\n", wynik);
            }
        }
    return 0;
}
