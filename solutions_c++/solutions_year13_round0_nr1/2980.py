#include <iostream>
#include <fstream>
#include <string>
//#include <cmath>
//#include <vector>
//#include <algorithm>
//#include <cassert>
using namespace std;
int N;
        int C,I,P;
int main() {
    std::ifstream fin ("A-large.in");
    std::ofstream fout("tictac.out");
    string s[4],blank;
    fin>>N;
    for(int i=0;i<N;i++)
    {
        fout<<"Case #"<<(i+1)<<": ";
        fin>>s[0]>>s[1]>>s[2]>>s[3];
        //cout<<"\n\n";
       // for(int i=0;i<4;i++) cout<<s[i]<<"\n";
        int result=4;
        bool tie=true;
        for(int i=0;i<4;i++)
        {
            int sofar=0;
            bool T=false;
            for(int j=0;j<4;j++)
            {
                switch(s[i][j])
                {
                case 'O':
                    sofar+=1;
                    break;
                case 'T':
                    T=true;
                    break;
                case '.':
                    tie=false;
                    break;
                default://X
                    sofar-=1;
                    break;
                }
            }
                if(sofar==-4 || (T && sofar==-3)) result=1;
                if(sofar==4 || (T && sofar==3)) result=2;
                //cout<<"Row"<<i<<": "<<result<<"\n";
        }
        for(int i=0;i<4;i++)
        {
            int sofar=0;
            bool T=false;
            for(int j=0;j<4;j++)
            {
                switch(s[j][i])
                {
                case 'O':
                    sofar+=1;
                    break;
                case 'T':
                    T=true;
                    break;
                case '.':
                    break;
                default://X
                    sofar-=1;
                    break;
                }
            }
                if(sofar==-4 || (T && sofar==-3)) result=1;
                if(sofar==4 || (T && sofar==3)) result=2;
               // cout<<"Col"<<i<<": "<<result<<"\n";
        }
        {
            int sofar=0;
            bool T=false;
        for(int i=0;i<4;i++)
            {
            int j=i;
                switch(s[j][i])
                {
                case 'O':
                    sofar+=1;
                    break;
                case 'T':
                    T=true;
                    break;
                case '.':
                    break;
                default://X
                    sofar-=1;
                    break;
                }
            }
                if(sofar==-4 || (T && sofar==-3)) result=1;
                if(sofar==4 || (T && sofar==3)) result=2;
                //cout<<"Diag: "<<result<<"\n";
        }
        
        {
            int sofar=0;
            bool T=false;
            for(int i=0;i<4;i++)
            {
            int j=3-i;
                switch(s[j][i])
                {
                case 'O':
                    sofar+=1;
                    break;
                case 'T':
                    T=true;
                    break;
                case '.':
                    break;
                default://X
                    sofar-=1;
                    break;
                }
            }
                if(sofar==-4 || (T && sofar==-3)) result=1;
                if(sofar==4 || (T && sofar==3)) result=2;
                //cout<<"Diagback: "<<sofar<<"\n";
        }
        if(tie && result==4) result=3;
        switch(result){
        case 1:
            fout<<"X won";
            break;
        case 2:
            fout<<"O won";
            break;
        case 3:
            fout<<"Draw";
            break;
        case 4:
            fout<<"Game has not completed";
            break;
        }
        fout<<"\n";
        
    }
    
    return 0;
}
