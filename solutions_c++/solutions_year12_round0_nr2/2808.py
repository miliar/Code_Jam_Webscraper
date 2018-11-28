#include<iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    
    int Z;
    cin >> Z;
    
    for(int z=1; z<=Z; z++)
    {
        int n;
        cin >> n;
        
        int s;
        cin >> s;
        
        int p;
        cin >> p;
        
        int result=0;
        
        for(int i=0; i<n; i++)
        {
            int t;
            cin >> t;
            
            if(t>=p*3-2)
                result++;
            
            else if(s && p>1 && (t==p*3-3 || t==p*3-4))
            {
                s--;
                result++;
            }   
        }
        
        cout << "Case #" << z << ": " << result << endl;
    
    }
    
return 0;
}
