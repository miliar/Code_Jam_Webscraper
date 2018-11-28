#include<iostream>
#include<fstream>
using namespace std;
int main()
{
     int t,t1,i,j,n;
     char a[100][100];
     float owp[100],oowp=0.0,wp[100][2];;
    char c;
    ifstream fi("input.txt");
    ofstream fo("output.txt");
    fi>>t;
    for(t1=1;t1<=t;t1++)
    {
        fi>>n;
        fo<<"Case #"<<t1<<":\n";
        for(i=0;i<n;i++)
        {
            wp[i][0]=wp[i][1]=0.0;
            for(j=0;j<n;j++)
            {
                fi>>a[i][j];
                if(a[i][j]!='.')
                {
                    wp[i][0]+=float(a[i][j]-48);
                    wp[i][1]=wp[i][1]+1.0;
                }       
            }
        }  
        for(i=0;i<n;i++)
        {
            owp[i]=0.0;
            for(j=0;j<n;j++)
            {
                if(a[i][j]!='.')
                {                
                    owp[i]+=(float)((wp[j][0]-(a[j][i]-48))/(wp[j][1]-1));
                }      
            }
            owp[i]/=wp[i][1];
        }
        for(i=0;i<n;i++)
        {
            oowp=0.0;
            for(j=0;j<n;j++)
            {   
                if(a[i][j]!='.')
                oowp+=owp[j];   
            }
            oowp/=wp[i][1];
            //fo<<(float)(wp[i][0]/wp[i][1])<<' '<<float(owp[i])<<' '<<float(oowp)<<'\n';
           fo<<(((float)(wp[i][0]/wp[i][1]))*0.25+ 0.5*owp[i]+0.25*oowp)<<'\n';     
        }
    }          
    return 0;        
}            
