#include<iostream>
#include<cstdlib>
using namespace std;

int main()
{
    int T;
    cin>>T;
    
    for(int num = 1; num <= T; num++) {
        int N;
        char R; int P;
        int time = 0;
        cin>>N;
        
        int pos_O = 1, pos_B = 1;
        char lastmove = ' ';
        int last_time;
        int change_time;
        
        for(int i = 0; i < N; i++) {
            cin>>R>>P;
            
            switch(R) {
                case 'O':
                    change_time = abs(P-pos_O);
                    if(lastmove == 'B')
                        if(change_time > last_time)
                            change_time = change_time - last_time;
                        else
                            change_time = 0;
                    change_time++;
                    if(lastmove == 'O')
                        last_time += change_time;
                    else
                        last_time = change_time;
                    time += change_time;
                    lastmove = 'O';
                    pos_O = P;
                    break;
                    
                case 'B':
                    change_time = abs(P-pos_B);
                    if(lastmove == 'O')
                        if(change_time > last_time)
                            change_time = change_time - last_time;
                        else
                            change_time = 0;
                    change_time++;
                    if(lastmove == 'B')
                        last_time += change_time;
                    else
                        last_time = change_time;
                    time += change_time;
                    lastmove = 'B';
                    pos_B = P;
                    break;
            }
        }
        cout<<"Case #"<<num<<": "<<time<<endl;
    }
    return 0;
}
