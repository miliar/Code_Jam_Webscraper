#include<iostream>
using namespace std;

int main()
{
    int T;
    cin>>T;
    char b[4][5],s[]={'X','O'};
    for(int ti = 1; ti <= T; ++ti)
    {
        cin>>b[0]>>b[1]>>b[2]>>b[3];

        int won = -1;
        for(int k = 0; k < 2; ++k)
        {
            for(int i = 0; i < 4; ++i)
            {
                int j = 0;
                while(j < 4 && (b[i][j] == s[k] || b[i][j] == 'T')) ++j;

                if(j==4) 
                {
                    won = k;
                    break;
                }
            }
            if(won != -1) break;
            
            for(int j = 0; j < 4; ++j)
            {
                int i = 0;
                while(i < 4 && (b[i][j] == s[k] || b[i][j] == 'T')) ++i;
                
                if(i==4) 
                {
                    won = k;
                    break;
                }
            }
            if(won != -1) break;

            int i = 0;
            while(i < 4 && (b[i][i] == s[k] || b[i][i] == 'T')) {++i;}
            if(i == 4) 
            {
                won = k;
                break;
            }

            i = 0;
            while(i < 4 && (b[3-i][i] == s[k] || b[3-i][i] == 'T')) {++i;}
            if(i == 4)
            {
                won = k;
                break;
            }
        }
        
        cout<<"Case #"<<ti<<": ";
        if(won != -1) cout<<s[won]<<" won\n";
        else
        {
            bool draw = true;
            for(int i = 0; i < 4; ++i)
            {
                for(int j = 0; j < 4; ++j)
                {
                    if(b[i][j]=='.') 
                    {
                        draw = false;
                        i = 4;
                        break;
                    }
                }
            }
            if(draw) cout<<"Draw\n";
            else cout<<"Game has not completed\n";
        }
    }

    return 0;
}
