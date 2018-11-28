#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
    int T;
    cin>>T;
    
    for(int c=1;c<=T;c++)
    {
        int N;
        char **result;
        int i,j;
        string line;
        
        cin>>N;
        result=new char*[N];
        for(i=0;i<N;i++)
            result[i]=new char[N];
        
        for(i=0;i<N;i++)
        {
            cin>>line;
            for(j=0;j<N;j++)
                result[i][j]=line[j];
        }
        
        double *RPI,*WP,*OWP,*OOWP,*games;
        RPI=new double[N];
        WP=new double[N];
        OWP=new double[N];
        OOWP=new double[N];
        games=new double[N];
        
        for(i=0;i<N;i++)
        {
            int win=0,lose=0;
            
            for(j=0;j<N;j++)
                switch(result[i][j])
                {
                    case '1':
                        win++;
                        break;
                    case '0':
                        lose++;
                        break;
                }
            WP[i]=(double)win/(win+lose);
            games[i]=win+lose;
        }
        for(i=0;i<N;i++)
        {
            int count=0;
            OWP[i]=0;
            for(j=0;j<N;j++)
                if(result[i][j]!='.')
                {
                    count++;
                    if(result[i][j]=='0')
                        OWP[i]+=((WP[j]*games[j]-1)/(games[j]-1));
                    else
                        OWP[i]+=((WP[j]*games[j])/(games[j]-1));
                }
            OWP[i]/=count;
        }
        for(i=0;i<N;i++)
        {
            int count=0;
            OOWP[i]=0;
            for(j=0;j<N;j++)
                if(result[i][j]!='.')
                {
                    count++;
                    OOWP[i]+=OWP[j];
                }
            OOWP[i]/=count;
        }
        
        cout<<"Case #"<<c<<":\n";
        for(i=0;i<N;i++)
        {
            RPI[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
            cout<<setprecision(12)<<RPI[i]<<endl;
        }
    }
    
    return 0;
}
