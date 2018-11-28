#include<iostream>
#include<cstdlib>
using namespace std;

int main()
{
    int T;
    int N;
    
    cin>>T;
    
    for(int c=1;c<=T;c++)
    {
        cin>>N;
        
        int count=0;
        char R;
        int P;
        int O=1;
        int B=1;
        char lastmove='X';
        int last;
        int change;
        
        for(int i=0;i<N;i++)
        {
            cin>>R>>P;
            
            switch(R)
            {
                case 'O':
                    change=abs(P-O);
                    if(lastmove=='B')
                        change=change>last?change-last:0;
                    change++;
                    if(lastmove=='O')
                        last+=change;
                    else
                        last=change;
                    count+=change;
                    lastmove='O';
                    O=P;
                    break;
                case 'B':
                    change=abs(P-B);
                    if(lastmove=='O')
                        change=change>last?change-last:0;
                    change++;
                    if(lastmove=='B')
                        last+=change;
                    else
                        last=change;
                    count+=change;
                    lastmove='B';
                    B=P;
                    break;
            }
        }
        cout<<"Case #"<<c<<": "<<count<<endl;
    }
}
