#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char **argv)
{
    ifstream in(argv[1]);
    ofstream out("output.txt");
    int t;
    in>>t;
    for(int i = 1; i <= t; i++)
    {
        char board[102][102];
        double win[102]={0};
        double total[102]={0};
        double wp[102]={0};
        double owp[102]={0};
        double oowp[102]={0};
        int n;
        in>>n;
        for(int j = 0; j < n; j++)
        {
            for(int k = 0; k < n; k++)
            {
                char c;
                in>>c;
                board[j][k] = c;
                if(c == '1')
                    win[j]+=1;
                if(c == '1' || c == '0')
                    total[j]+=1;
            }
            wp[j] = win[j]/total[j];
        }
        for(int k = 0; k < n; k++)
        {
            double t = 0;int comp = 0;
            for(int j = 0; j < n; j++)
            {
                if(board[j][k] == '0')
                    t += win[j]/(total[j] -1);
                else if(board[j][k] == '1')
                    t += (win[j]-1)/(total[j]-1);
                if(board[j][k] == '0' || board[j][k] == '1')
                    comp++;
            }
            owp[k] = t/comp;
        }
        for(int j =0; j < n; j++)
        {
            double t = 0; int comp =0 ;
            for(int k = 0; k < n; k++)
            {
                if(board[j][k] == '0' || board[j][k] == '1')
                {
                    t += owp[k];
                    comp++;
                }
            }
            oowp[j] = t/comp;
        }
        out<<"Case #"<<i<<":"<<endl;
        for(int j = 0; j < n; j++)
        {
            cout<<j<<" "<<wp[j]<<" "<<owp[j]<<" "<<oowp[j]<<endl;
            out<<0.25*wp[j]+0.5*owp[j]+0.25*oowp[j]<<endl;
        }
    }

}
