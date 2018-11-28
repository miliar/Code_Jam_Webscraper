#include<iostream>
#include<string>
#include<vector>
using namespace std;
int main()
{
     long long runs;
     cin>>runs;
     for(long long i=0;i<runs;i++)
        {
                long long p, k,l;
                cin>>p>>k>>l;
                vector <long long> freq(l,0);
                //vector <vector<long long> > pad(k);
                //vector <long long> temp;
                
                for(long long j=0;j<freq.size();j++)
                        cin>>freq[j];
                sort(freq.begin(),freq.end());
                reverse(freq.begin(),freq.end());
                vector <long long> symbol(l,1);
                long long ans=0;
                for(long long m=0;m<symbol.size();m++)
                {
                        ans=ans+freq[m]*(m/k+1);
                        
                }
                   
                
                
                
                
                
                
                
                /////////////////////////////////////////////////////////
                cout<<"Case #"<<(i+1)<<": ";
                cout<<ans;
                   
                   
                
                   
                if(i!=(k-1))
                            cout<<endl;
        }
     getchar();
     return 0;
}
