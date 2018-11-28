#include<iostream>
#include<vector>
#include<fstream>
using namespace std;

int main()
{
    
    fstream input;
    string s;
    cin>>s;
    
    input.open(s.c_str(),ios::in);
    int T;
    input>>T;
    
    
    fstream output;
    output.open("output.txt",ios::out);
    
    for(int testcase=0;testcase<T;testcase++)
    {
            int n;
            input>>n;
            vector <int> A(n);
            vector <int> B(n);
            for(int i=0;i<n;i++)
            input>>A[i]>>B[i];
            
            int ans=0;
            for(int i=0;i<n;i++)
            {
                    for(int j=i+1;j<n;j++)
                    {
                            if(A[i]>A[j]&&B[i]<B[j])
                                                    ans++;
                            else if(A[i]<A[j]&&B[i]>B[j])
                                 ans++;
                                         
                            
                            
                    }        
                    
                    
            }        
            
            output<<"Case #"<<testcase+1<<": "<<ans<<endl;

            
            
            
    }
   
   
   
   
   
    input.close();
    output.close();
    system("pause");
    return 0;
    
        
    
    
    
}
