
#include<iostream>
#include <fstream>
using namespace std;

static int const MAX_NUM_OF_BOTS = 100;
static int const MAX_NUM_OF_TEST =100;
//Used to store bot information for each test case

int Orange_Bots[MAX_NUM_OF_TEST][MAX_NUM_OF_BOTS][2];
int Blue_Bots[MAX_NUM_OF_TEST][MAX_NUM_OF_BOTS][2];

int main()
{
      int number_of_test = 0;
      int sequence_length = 0;
      int button_pos =0;
      char bot_color = '#';
      
      ifstream inputFile;
       inputFile.open("A-large.in");
      
       if (inputFile.is_open())
       {
             inputFile >> number_of_test;
            // cout << "number of test read is:" << number_of_test <<endl;
       }
       
       ofstream outputFile;
       outputFile.open("Large_A_output.txt");
            
       for(int i=1; i<=number_of_test; i++)
       {
            // cout << "current test case = " << i <<endl;
             int orange_bot_cnt = 0;
             int blue_bot_cnt = 0;
             int total_to_push = 0;
             
             inputFile >>sequence_length;
          //   cout << "current sequence length =" <<  sequence_length <<endl;
          //   cin.get();

             for(int j=0; j< sequence_length; j++)
             {
                   inputFile >> bot_color >> button_pos;
                   
                   if(bot_color=='O')
                   {
                         Orange_Bots[i][orange_bot_cnt][0] = button_pos;
                         Orange_Bots[i][orange_bot_cnt][1] = total_to_push;  
                         orange_bot_cnt++;
                          total_to_push++;  
                   }
                        
                   if(bot_color=='B')
                   {
                         Blue_Bots[i][blue_bot_cnt][0] = button_pos;  
                         Blue_Bots[i][blue_bot_cnt][1] = total_to_push;
                         blue_bot_cnt ++;
                         total_to_push++;
                   } 
             }//EndFillCurrentSequence
             
             //Process current test case
             int orange_pos=1;
            int blue_pos=1;
            int orange_curpos=0;
            int blue_curpos=0;
            int pushed=0;
            int cur_test_total_time=0;  //earliest finish time

            //Simulate the move of bots
            while(pushed !=total_to_push)
            {
                  int targetTotal;
                  int steps; //steps to move
                  if (orange_curpos<orange_bot_cnt
                    && Orange_Bots[i][orange_curpos][1]==pushed)
                  {
                        targetTotal = Orange_Bots[i][orange_curpos][0];
                        orange_curpos++ ;
                        steps=abs(targetTotal-orange_pos)+1;
                        cur_test_total_time+=steps;
                        pushed++;
                        orange_pos = targetTotal;
                        for(int k =0;  k<steps; k++)
                        {
                              if(blue_pos < Blue_Bots[i][blue_curpos][0])
                                    blue_pos++;
                              if(blue_pos == Blue_Bots[i][blue_curpos][0])
                                    break;
                              if(blue_pos > Blue_Bots[i][blue_curpos][0])
                                    blue_pos--;
                        }
                  }//EndForProcessOrange
                  
                  if(blue_curpos<blue_bot_cnt &&Blue_Bots[i][blue_curpos][1]==pushed)
                  {
                        targetTotal = Blue_Bots[i][blue_curpos][0];
                        blue_curpos++ ;
                        steps=abs(targetTotal-blue_pos)+1;
                        cur_test_total_time +=steps;
                        blue_pos = targetTotal;
                        pushed++;
                        for(int k=0; k<steps; k++)
                        {
                              if(orange_pos<Orange_Bots[i][orange_curpos][0])
                                    orange_pos++;
                              if(orange_pos==Orange_Bots[i][orange_curpos][0])
                                    break;
                              if(orange_pos>Orange_Bots[i][orange_curpos][0])
                                    orange_pos--;
                        }
                  }//EndProcessBlue
            }

            //cout<< "Case #"<< i << ": "  << totalTime<<endl;
            outputFile<< "Case #"<< i << ": "  << cur_test_total_time<<endl;
            
      }//EndOfTotalNumOfTests
       
       outputFile.flush();
      outputFile.close();
      cin.get();
      return 0;
}
