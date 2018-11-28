#include <iostream>

using namespace std;

int C,D,N;
char Ds[36][4];
char Cs[36][3];
char Ns[101];
int i;
int j;
int k;
char Output[101];
int Top = -1;
int Flag = 0;

int FindChar(char Ch)
{
    for(j=0;j<=Top;j++)
        if(Output[j] == Ch) return 1;
    return 0;
}

void Display(char X[])
{
    for(int i=0;X[i]!='\0';i++)
    {
        cout<<X[i];
        if(X[i+1] != '\0') cout<<", ";
    }
}

int main (int argc, const char * argv[])
{
    int T;
    cin>>T; 
    
    for(int t=0;t<T;t++)
    {
        cin>>C;
        for(i=0;i<C;i++) cin>>Cs[i];
        cin>>D;
        for(i=0;i<D;i++) cin>>Ds[i];
        
        cin>>N;
        cin>>Ns;        
        
        if(C==0 && D==0)
        {
            strcpy(Output,Ns);
            Top = N-1;
        }
        
        else
        {
            Output[0] = Ns[0];
            Output[1] = Ns[1];
            Top = 1;
            
            for(i=2;i<N;i++)
            {
                if(C!=0) while(Top >= 1)
                {   
                    Flag = 0;
                    for(j=0;j<C;j++)
                        if((Cs[j][0] == Output[Top] && Cs[j][1] == Output[Top-1]) || (Cs[j][1] == Output[Top] && Cs[j][0] == Output[Top-1]))
                        {
                            Flag = 1;
                            Output[Top-1] = Cs[j][2];
                            Top--;
                        }
                    
                    if(Flag == 0) break;
                    
                }
                
                if(D!=0) for(k=0;k<D;k++)
                {
                    
                    if(FindChar(Ds[k][0]) == 1) 
                        if(FindChar(Ds[k][1]) == 1) 
                        {
                            Top = -1;
                            break;
                        }
                }
                    
                Output[++Top] = Ns[i];
            }
            
        }
        
        if(C!=0) while(Top >= 1)
        {   
            Flag = 0;
            for(j=0;j<C;j++)
                if((Cs[j][0] == Output[Top] && Cs[j][1] == Output[Top-1]) || (Cs[j][1] == Output[Top] && Cs[j][0] == Output[Top-1]))
                {
                    Flag = 1;
                    Output[Top-1] = Cs[j][2];
                    Top--;
                }
            
            if(Flag == 0 ) break;
            
        }
        
        if(D!=0) for(k=0;k<D;k++)
        {          
            if(FindChar(Ds[k][0]) == 1) 
                if(FindChar(Ds[k][1]) == 1) 
                {
                    Top = -1;
                    break;
                }
        }
        
        
        Output[Top+1]='\0';
        cout<<"Case #"<<t+1<<": [";
        Display(Output);
        cout<<"]\n";
        
    }

    return 0;  
    
}

