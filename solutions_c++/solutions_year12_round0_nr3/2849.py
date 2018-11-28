#include<iostream>
using namespace std;

pair<int,int> r[10];

int main()
{
    ios_base::sync_with_stdio(0);
    
    int Z;
    cin >> Z;
    
    for(int z=1; z<=Z; z++)
    {
        int A;
        cin >> A;
        
        int B;
        cin >> B;
        
        int dig=0;
        int temp=A;
        
        while(temp)
        {
            dig++;
            temp/=10;
        }
        
        int pot=1;
        
        for(int i=1; i<dig; i++)
            pot*=10;
        
        int result=0;
        int res=0;
        
        for(int i=A; i<=B; i++)
        {
            int x=i;
            
            for(int j=1; j<dig; j++)
            {
                temp=x%10;
                x/=10;
                x+=temp*pot;
                
                if(x>i && x<=B)
                {
                    r[res].first=i;
                    r[res].second=x;
                    res++;
                }
            }
            
            if(res)
            {
                result++;
                
                for(int j=1; j<res; j++)
                    if(r[j]!=r[j-1])
                        result++;
                
                res=0;
            }
        }
                
        cout << "Case #" << z << ": " << result << endl;
    }
return 0;
}
