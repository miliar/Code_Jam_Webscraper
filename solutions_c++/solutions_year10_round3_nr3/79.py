#include<iostream>
using namespace std;

bool pickable[512][512][512];
bool grid[512][512];
int num[512];

int main()
{
    int T,t,M,N,k,i,j,i1,i2,j1,k1,val;
    char str[200];
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>M>>N;
        for(k=0; k<M; k++) {
        cin>>str;
        for(i=0;i<<2<N;i++)
        {
            if(str[i]>='A' && str[i]<='F')
                val = str[i]-'A'+10;
            else
                val = str[i]-'0';
            
            int i2=0;
            for(j=8;j>0;j=j>>1)
            {
                grid[k][(i<<2) + i2] = ((val&j)> 0);
                i2++;
            }
        }
        }
        
        for(i=0; i<M; i++)
            for(j=0; j<N; j++)
                 cerr<<grid[i][j];
        
        for(i=0; i<M; i++)
            for(j=0; j<N; j++)
                pickable[i][j][1]=true;
        
        int maxk = 1;    
        for(k=2; k<=min(M,N); k++)
        {
            cerr<<"k="<<k;
            for(i=0; i<M-k+1; i++)
               for(j=0; j<N-k+1; j++)
               {
                   if(k==2)
                   {
                       pickable[i][j][k] = (grid[i][j]==grid[i+1][j+1] && grid[i+1][j] == grid[i][j+1] && grid[i][j]!= grid[i][j+1]);
                   }
                   else
                   {
                       pickable[i][j][k] = (pickable[i][j][k-1] && pickable[i][j+1][k-1] && pickable[i+1][j][k-1] && pickable[i+1][j+1][k-1]);
                   }
                   
                   if(pickable[i][j][k]) 
                   {
                       maxk = k;
                       }
               }
        }
        int nums=0;
        
        for(k=maxk; k>0; k--)
        {
            cerr<<"k="<<k<<endl;
            num[k] = 0;
            for(i=0; i<M-k+1; i++)
                for(j=0; j<N-k+1; j++)
                {
                    if(pickable[i][j][k])
                    {
                        num[k]+=1;
                        for(k1=1; k1<=k; k1++)
                            for(i1=max(i-k1+1,0); i1<min(i+k,M-k1+1); i1++)
                                for(j1=max(j-k1+1,0); j1<min(j+k,N-k1+1); j1++)
                                {
                                    pickable[i1][j1][k1] = false;
                                    }
                                    
                                    
                    }
                }
            if(num[k]!=0) nums++;
        }
        
        cout<<"Case #"<<t<<": "<<nums<<endl;
        for(k=maxk; k>0; k--)
        {
            if(num[k]!=0)
                cout<<k<<' '<<num[k]<<endl;
        }
    }
}
                
        
            
