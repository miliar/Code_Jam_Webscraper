#include<iostream>
#include<cstdio>
using namespace std;

int abs(int a, int b)
{
    if(a>b) return (a-b);
    return (b-a);
}

main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout); 
    int t;
    int t_;
    cin>>t;
    t_ = t;
    while(t>0)
    {
        int i,n;
        char colour;
        int orange,blue;
        int current_o = 1,current_b = 1;
        int middle_moves = 0;
        int tot_moves = 0;
        bool last_move;
        
        cin>>n;
        
        cin>>colour;
        if(colour=='O')
        {
            cin>>orange;
            tot_moves = orange;
            middle_moves = orange;
            current_o = orange;
            last_move = 0;
        }
        if(colour=='B')
        {
            cin>>blue;
            tot_moves = blue;
            middle_moves = blue;
            current_b = blue;            
            last_move = 1;
        }
        
        for(i=1;i<n;++i)
        {
            //cout<<"dd"<<middle_moves<<"dd";
            cin>>colour;
            if(colour=='O')
            {
                cin>>orange;
                if(last_move==0)
                {
                    tot_moves += (abs(orange,current_o) + 1);
                    middle_moves += (abs(orange,current_o) + 1);
                    current_o = orange;
                }
                else
                {
                    if(abs(orange,current_o)<=middle_moves)
                    {
                        tot_moves += 1;
                        current_o = orange;
                        middle_moves = 1;
                        last_move = 0;
                    }
                    
                    else
                    {
                        tot_moves += ((abs(orange,current_o)-middle_moves) + 1);
                        middle_moves = ((abs(orange,current_o)-middle_moves) + 1);
                        current_o = orange;
                        last_move = 0;
                    }
                }
            }
            
            else
            {
                cin>>blue;
                if(last_move==1)
                {
                    tot_moves += (abs(blue,current_b) + 1);
                    middle_moves += (abs(blue,current_b) + 1);
                    current_b = blue;
                }
                else
                {
                    if(abs(blue,current_b)<=middle_moves)
                    {
                        tot_moves += 1;
                        current_b = blue;
                        middle_moves = 1;
                        last_move = 1;
                    }
                    
                    else
                    {
                        tot_moves += ((abs(blue,current_b)-middle_moves) + 1);
                        middle_moves = ((abs(blue,current_b)-middle_moves) + 1);
                        current_b = blue;
                        last_move = 1;
                    }
                }
            }
        }
        cout<<"Case #"<<t_-t+1<<": "<<tot_moves<<"\n";
        t--;
    }
}
                
        
