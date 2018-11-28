#include<iostream.h>
using namespace std;

int i,j,k,N;
int cnt, c, m, T;
char str[50];
int v[40];
int maxblah;


void swap(int i, int j)
{
     int temp=v[i];
     v[i]=v[j];
     v[j]=temp;
}

int main()
{
    cin>>T;
    for(c=1; c<=T; c++)
    {
        cin>>N;
        for(i=0; i<N; i++)
        {
             cin>>str;
             for(j=N-1; j>=0; j--)
             {
                 
                 if(str[j] == '1')
                     break;
             }
             v[i] = j+1;
        }
        
        for(i=0; i<N; i++)
            cerr<<v[i];
        cnt = 0;
        bool done = false;
        while(!done)
        {
            for(i=0; i<N; i++)
            {
                if(v[i] > i+1 )
                    break;
            }
            if(i==N)
                break;
            
            for(j=i+1; j<N; j++)
            {
                if(v[j] <= i+1)
                    break;
            }
            
            for(k=j-1; k>=i; k--)
            {
                 cnt++;
                 swap(k,k+1);
            } 
            
            
        }
        cout<<"Case #"<<c<<": "<< cnt  <<endl;
    }
}
