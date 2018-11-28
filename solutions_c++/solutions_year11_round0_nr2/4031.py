//Written by Ron Snijders

#include <iostream>

using namespace std;

int main()
{
    freopen("B-small-attempt1.in", "rt", stdin);
    freopen("MagickaOut.txt", "wt", stdout);
    
    string combine[36][3];
    string opposed[28][2];
    string invoke[100];
    string output[100];
    
    int T;
    cin >> T;
    
    for(int i = 0; i < T; i++)
    {
        int C;
        int D;
        int N;
        
        cin >> C;
        getchar();
                
        for(int ii = 0; ii < C; ii++)
        {
            combine[ii][0] = getchar();
            combine[ii][1] = getchar();
            combine[ii][2] = getchar();
            getchar();
        }
        
        cin >> D;
        getchar();
        
        for(int ii = 0; ii < D; ii++)
        {
            opposed[ii][0] = getchar();
            opposed[ii][1] = getchar();
            getchar();
        }
        
        cin >> N;
        getchar();
        
        for(int ii = 0; ii < N; ii++)
        {
            invoke[ii] = getchar();
        }
        getchar();
        
        int index = 0;
        
        for(int ii = 0; ii < N; ii++)
        {
            output[index] = invoke[ii];
            
            if(index != 0)
            {
                for(int iii = 0; iii < C; iii++)
                {
                    if((output[index-1] == combine[iii][0] && output[index] == combine[iii][1]) || (output[index-1] == combine[iii][1] && output[index] == combine[iii][0]))
                    {
                        output[index-1] = combine[iii][2];
                        index--;
                    }
                    
                }
                
                for(int iii = 0; iii < index; iii++)
                {
                    for(int iiii = 0; iiii < D; iiii++)
                    {
                        if((output[index] == opposed[iiii][0] && output[iii] == opposed[iiii][1]) || (output[index] == opposed[iiii][1] && output[iii] == opposed[iiii][0]))
                        {
                            index = -1;
                        }
                    }
                    
                }
            }
            index++;
        }
        
        cout << "Case #" << i + 1 << ": [";
        
        for(int ii = 0; ii < index; ii++)
        {
            cout << output[ii];
            
            if(ii != index - 1)
            {
                cout << ", ";
            }
        }
        
        
        cout << "]" << endl;
                       
    }
}
