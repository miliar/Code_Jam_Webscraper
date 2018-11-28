#include<iostream>
using namespace std;

int groups[1000];
int total[1000];
int jump_to[1000];

int main()
{
    int T,R,k,N,i,j,c;
    cin>>T;
    for(c=1; c<=T; c++)
    {
        cin>>R>>k>>N;
        for(i=0; i<N; i++)
            cin>>groups[i];
        
        for(i=0; i<N; i++)
        {
            total[i]=0;
            for(j=i;;)
            {
                if(total[i]+groups[j] > k)
                {
                    jump_to[i]=j;
                    cerr<<j<<' ';
                    break;
                }
                total[i]+=groups[j];
                j++;
                if(j==N) j=0;
                if(j==i)
                {
                    jump_to[i]=i;
                    cerr<<i<<' ';
                    break;
                }
            }
        }
        
        long long euros = 0;
        for(i=0, j=0; i<R; i++)
        {
            euros+=total[j];
            j=jump_to[j];
        }
        
        cout<<"Case #"<<c<<": "<<euros<<endl;
    }
}
                
                
