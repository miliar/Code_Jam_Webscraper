#include<iostream>
#include<fstream>
using namespace::std;

int main()
{
 ifstream ifs ( "A-large.in" , ifstream::in );
 ofstream ofs ( "out.txt", ofstream::out);
 int N = 0;
 ifs >> N;
 for(int i=0;i<N;i++)
 {
         int M = 0;
         ifs >> M;
         char curr_state;
         int totaltime = 0;
         int O = 1;
         int B = 1;
         int timeinstate = 0;
         for(int j=0;j<M;j++)
         {
            char state;
            int pos;
            ifs >> state >> pos;
            if(state==curr_state)
                {
                    if(state=='O')
                    {
                        int diff = pos - O;
                        if(diff<0)diff = -diff;
                        int move = diff+1;
                        totaltime += move;
                        timeinstate += move;
                        O = pos;
                    }
                    if(state=='B')
                    {
                        int diff = pos - B;
                        if(diff<0)diff = -diff;
                        int move = diff+1;
                        totaltime += move;
                        timeinstate += move;
                        B = pos;
                    }
                }
            else
            {
                if(state=='O')
                    {
                        int diff = pos - O;
                        if(diff<0)diff = -diff;
                        int move = diff-timeinstate;
                        if(move<0)move = 0;
                        move++;
                        totaltime += move;
                        timeinstate = move;
                        O = pos;
                    }
                    if(state=='B')
                    {
                        int diff = pos - B;
                        if(diff<0)diff = -diff;
                        int move = diff-timeinstate;
                        if(move<0)move = 0;
                        move++;
                        totaltime += move;
                        timeinstate = move;
                        B = pos;
                    }
                    curr_state = state;
            }
         }        
         ofs << "Case #" << i+1 << ": " << totaltime<<endl;
 }    
}
