# include <iostream>
# include <vector>
# include <string>

using namespace std;

int main ()
{
    int test;
    cin>>test;
    for (int testid = 1; testid <=test;testid++)
    {
        vector <long long> Cval,Nval,Nsum;
        long long L,N,C;
        long long t;
        long long temp;
        cin>>L>>t>>N>>C;
        //cout<<t;
        long long sum =0;
        for (int i=0;i<C;i++)
        {
            cin>>temp;
            Cval.push_back (temp);
        }
        Nsum.push_back (0);
        for (int i=1;i<=N;i++)
        {
            int index =  (i-1)%Cval.size();
            //Nval.push_back (Cval[index]);
            Nsum.push_back (Nsum[i-1] + 2 * Cval[index]);
        }
        long long minsum;
        
        sum = Nsum[Nsum.size() - 1];
        //cout<<sum;
        minsum = sum;
        if (L == 1)
        {
        for (int j=0;j<N;j++)
            {
                long long sumt = sum;
                if (Nsum[j+1] > t)
                {
                      sumt -= (min(Nsum[j+1]-t,Nsum[j+1] - Nsum[j]))/2;
                }
                if (minsum > sumt)
                    minsum = sumt;
            }
        }    
        if (L == 2)
        {
        for (int i=0;i<(N-1);i++)
        {
            
            for (int j=i+1;j<N;j++)
            {
                long long sumt = sum;
                if (Nsum[i+1] > t)
                {
                      sumt -= (min(Nsum[i+1]-t,Nsum[i+1] - Nsum[i]))/2;
                }
                if (Nsum[j+1] > t)
                {
                      sumt -= (min(Nsum[j+1]-t,Nsum[j+1] - Nsum[j]))/2;
                }
                if (minsum > sumt)
                    minsum = sumt;
            }
        }    
        }                              
        cout<<"Case #"<<testid<<": "<<minsum<<endl;
    }
    return 0;
}            
        
