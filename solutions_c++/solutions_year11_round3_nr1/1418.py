
#include <iostream>

using namespace std;


int T; /* Max 50 */
int C;
int R;
int Count;
int Flag;

char Arr[50][50];
int i;
int j;

int main()
{
    cin>>T;
    for(int t=0; t<T; t++)
    {
        Count=0;
        Flag=1;
        
        cin>>R>>C;
        for(i=0;i<R;i++)
            for(j=0;j<C;j++)
                cin>>Arr[i][j];
        
        for(i=0;i<R;i++)
            for(j=0;j<C;j++)
                if(Arr[i][j]=='#')
                    Count++;
        
        if(Count%4 != 0)
            Flag = 0;
        
        else
        {
            for(i=0;i<R;i++)
                for(j=0;j<C;j++)
                {   if(Arr[i][j]=='#')
                    {
                        if(Arr[i+1][j]=='#' && Arr[i][j+1]=='#' && Arr[i+1][j+1]=='#')
                        {
                            Arr[i][j] = '/';
                            Arr[i+1][j] = '\\';                            
                            Arr[i][j+1] = '\\';
                            Arr[i+1][j+1] = '/';
                        }
                        
                        else
                            Flag=0;                            
                    }
                }
        }       
        
        cout<<"Case #"<<t+1<<":\n";
        if(Flag==0)
            cout<<"Impossible\n";
        else
            for(i=0;i<R;i++)
            {
                for(j=0;j<C;j++)
                    cout<<Arr[i][j];
                cout<<endl;
            }
    }
    
    return 0;
}