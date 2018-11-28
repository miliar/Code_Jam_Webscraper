#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main() {
    ifstream fin;
    ofstream fout;
    
    int test_case;
    fin.open("a.in");
    
    fout.open("output_a.txt");
    
    fin>>test_case;
    int tccnt=0;
    while (test_case!=tccnt)
    {
          tccnt++;
          //read
          int n; //no of buttons;
          int b[100], o[100], tnt[201];
          fin>>n;
          char ch;
          int b_cnt = 0;
          int o_cnt = 0;
          for (int i=0; i<n; i++)
          { 
              fin>>ch;
              if (ch=='O')
              {
                 tnt[i]=1;
                 fin>>o[o_cnt];
                 o_cnt++;
              }
              else if (ch=='B')
              {
                 tnt[i]=0;
                 fin>>b[b_cnt];
                 b_cnt++;
              }
          }  
          int total_time=0;
          int b_pos = 1;
          int o_pos = 1;
          int button_push =0;
          int x = 0;
          int y = 0;
          int time_for_b = int (fabs(b[x]-b_pos));
          int time_for_o = int (fabs(o[y]-o_pos));
          while ( button_push != n )
          {           
                if ( tnt[button_push] == 0 ) //b
                {
                     total_time +=(time_for_b+1);
                     b_pos = b[x];
                     x++;
                     button_push++;
                     time_for_o -= (time_for_b+1);
                     if (time_for_o <= 0) { time_for_o = 0; }
                     time_for_b = int (fabs(b[x]-b_pos));
                     
                }    
                else
                {
                     total_time +=(time_for_o+1);
                     o_pos = o[y];
                     y++;
                     button_push++;
                     time_for_b -= (time_for_o)+1;
                     if (time_for_b <= 0) { time_for_b = 0; }
                     time_for_o = int (fabs(o[y]-o_pos));
                }
          }
          fout<<"Case #"<<tccnt<<": "<<total_time<<endl;
    }

cout<<"Finished!\n";
fin.close();
fout.close();
return 0;
}
