# include <iostream>
# include <vector>
# include <string>

using namespace std;

bool check (int A,int B)
{
    int mod;
    if ( A < B)
    {
       mod = B%A;
    }
    else
       mod = (A%B);
    //cout<<mod;
    if (mod == 0)
       return false;
    return true;                
}

int main ()
{
    int test;
    cin>>test;
    for (int testid = 1; testid <=test;testid++)
    {
        vector <int> freq;
        int N,L,H,ans;
        int temp;
        cin>>N>>L>>H;
        for (int i=0;i<N;i++)
        {
            cin>>temp;
            freq.push_back(temp);
        }
        bool flag;
        //cout<<L<<H<<endl;
        for (int i=L;i<=H;i++)
        {
            flag = true;
            for (int j=0;j<freq.size ();j++)
            {
                if (check(i,freq[j]))
                {
                      flag = false;
                }
            }
            if (flag == true)
            {
                 ans = i;
                 break;
            }
        }
        if (flag == true)
        {                     
            cout<<"Case #"<<testid<<": "<<ans<<endl;
        }
        else
        {
            cout<<"Case #"<<testid<<": NO"<<endl;
        }       
    }
    return 0;
}            
        
