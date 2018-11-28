
#include <iostream>

using namespace std;


int T; /* Max 20 */
int N;

long double RPI[100];
long double WP[100];
long double Div;
long double Mid;
long double OWP[100];
long double OOWP[100];

char Arr[100][100];

void Clear()
{
    for(int x=0;x<100;x++)
    {
        RPI[x] = 0;
        WP[x] = 0;
        OWP[x] = 0;
        OOWP[x] = 0;
        Div = 0;
        Mid = 0;
    }
}

int main()
{
    int i;
    int j;
    int k;
    int Temp;
    
    cin>>T;
    for(int t=0; t<T; t++)
    {
        Clear();
        cin>>N;
        
        for(i=0;i<N;i++)
            for(j=0;j<N;j++)
                cin>>Arr[i][j];
        
       
        for(i=0;i<N;i++)
        {
            Temp = 0;
            for(j=0;j<N;j++)
            {
                if(Arr[i][j]!='.')
                {
                    Temp++;
                    WP[i] = WP[i] + (int)Arr[i][j] -48;
                
                }
                
            }
            if(Temp!=0)
                WP[i] = WP[i]/(double)Temp;
        }
        
            
                   
        for(i=0;i<N;i++)
        {        
            Temp = 0; 
            for(k=0;k<N;k++)
            {
                Mid = 0;
                Div = 0;
                if(k!=i && Arr[k][i]!='.')
                {  

                    Temp++;
                    for(j=0;j<N;j++)
                        if(j!=i && Arr[k][j]!='.')
                        {
                            Div++;
                            Mid = Mid + (int)Arr[k][j] -48;
                        }
                    
                    if(Div!=0)
                        Mid/=(double)Div;  
                    
                }
                
                OWP[i] = OWP[i] + Mid;
                
                
            }            
             
            if(Temp!=0)
                OWP[i] = OWP[i]/(double)Temp;            
        }   
        
        
        for(i=0;i<N;i++)
        {
            Temp=0;
            for(j=0;j<N;j++)
                if(Arr[i][j]!='.' && i!=j)
                {   Temp++;
                    OOWP[i] = OOWP[i] + OWP[j];
                }
            
            if(Temp!=0)
                OOWP[i]/=(double)Temp;
        }
        
        cout<<"Case #"<<t+1<<":\n";
        for(i=0;i<N;i++)
        {
            RPI[i] =  0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
            cout<<RPI[i]<<endl;
        }
  
        
        
    }
    
    return 0;
}