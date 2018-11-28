
#include <iostream>

using namespace std;


int T; /* Max 40 */
int N; /* Max 100 */
int L; /* Max 10000 */
int H;
int Arr[100];

int i;
int j;
int Flag;

int main()
{
    cin>>T;
    
    for(int t=0; t<T; t++)
    {    
        Flag = 0;
        cin>>N>>L>>H;
        for(i=0;i<N;i++)
            cin>>Arr[i];
        
        for(j=L;j<=H;j++)
        {
            for(i=0;i<N;i++)
            {   
                if(Arr[i]%j == 0 || j%Arr[i]==0);
                else break;
            }
            
            if(i==N) 
            {
                Flag=1;
                break;
            }
        }
        
        if(t!=0) 
            cout<<endl;
        cout<<"Case #"<<t+1<<": ";
        if(Flag == 1 && j<=H)
            cout<<j;
        else cout<<"NO";
    }
    
    return 0;
}