#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string> 
#include <vector>
#include<map>


using namespace std;

#define OUTPUT_FILE "output.txt"
#define ESCAPE_CHAR " "
#define OUTPUT_START "Case #"



vector<string> get_all_string(string input,string escape)
{
   vector<string> lines;
   int pos=0;
  
   while(1)
   {
          int next_pos = input.find(escape,pos);
          if (next_pos==string::npos)
          {
                   lines.push_back( input.substr(pos,input.size()-pos) );
                   break;
          }
          else
          {
              lines.push_back( input.substr(pos,next_pos-pos) );
              pos = next_pos+1;
          }
   }
   return lines;
}

void get_all_input(vector<string>& input , string filename)
{
   ifstream  myfile; 
   myfile.open (filename.c_str());
   
    string line;
    
   getline(myfile, line);
   input.push_back(line);//number of test cases
   int no_of_cases = atoi(input[0].c_str());
   
   for(int i=0;i<no_of_cases;i++)
   {
     getline(myfile, line);
     input.push_back(line);//some input
   
     getline(myfile, line);
     input.push_back(line);//number of inputs

     int no_of_input = atoi(line.c_str());//get all inputs in one string
     int j=0;
     line="";
     while(j<no_of_input)
     { 
       string input_line;
       getline(myfile, input_line);
       line = line + input_line;
       vector<string> all = get_all_string(input_line,ESCAPE_CHAR);
        j = j+all.size();
     }
     input.push_back(line);                             
   }
   
   return;  
}



void write_to_file(vector<string> output)
{
     ofstream  myfile; 
     myfile.open (OUTPUT_FILE);
   
     for(int i=0;i<output.size() ;i++)
    {
             myfile<<OUTPUT_START<<i+1<<": "<<output[i]<<endl;
    }
     
}

vector<string> problem(vector<string> input)
{
   
    vector<string> out;
    int test_cases = atoi(input[0].c_str());
    int count =0;
    while(count<test_cases)
    {
    count++;
    vector<string> all = get_all_string(input[count]," ");
    int cur_o = 1;
    int cur_b = 1;
    int cur_index = 1;
    int last_move_by = -1;
    int last_move_steps = 0; 
    int sum =0;
    while(cur_index < all.size() )
    {
    if(all[cur_index].compare("O") == 0)
    {
             int temp = abs(atoi(all[cur_index+1].c_str()) - cur_o);
             cur_o = atoi(all[cur_index+1].c_str());
             cout<<"currentO"<<cur_o<<endl;
             cout<<"O temp "<<temp<<endl;
             if(last_move_by ==0){
                  if(last_move_steps > temp){
                      sum = sum+1;
                      last_move_steps=1;
                      cout<<"O incremented sum by 1"<<endl;
                  }
                   else{
                      sum +=(temp - last_move_steps)+1;
                      cout<<"switch O incremented sum by "<<(temp - last_move_steps)+1<<endl;
                      last_move_steps = (temp - last_move_steps)+1;
                   }
          }
          else{
               last_move_steps += temp+1;
               sum +=  temp+1;
               cout<<"O incremented sum by "<<temp+1<<endl;
          }
      last_move_by = 1;
    }
    else{
             int temp =  abs(atoi(all[cur_index+1].c_str()) - cur_b);
             cur_b = atoi(all[cur_index+1].c_str());
             cout<<"currentB"<<cur_b<<endl;
             cout<<"B temp "<<temp<<endl;
             if(last_move_by ==1){
             if(last_move_steps > temp){
                    sum = sum+1;
                    last_move_steps=1;
                    cout<<"switch B incremented sum by 1"<<endl;
             }
             else{
                  sum +=(temp - last_move_steps)+1;
                  cout<<"B incremented sum by "<<(temp - last_move_steps)+1<<endl;
                last_move_steps = (temp - last_move_steps)+1;        
             }
      }
      else{
          last_move_steps += temp+1;
          sum +=  temp+1;
          cout<<"B incremented sum by "<<temp+1<<endl;
      }
      last_move_by = 0;
    }
    cur_index +=2;
}
char sumChar[20]; 
itoa(sum,sumChar,10);
out.push_back(sumChar);
}
    return out;
}

int main(int argc, char *argv[])
{
   int no_of_lines;
   vector<string> input;
   get_all_input(input , argv[1]);
   vector<string> out = problem(input);
   write_to_file(out);
   system("PAUSE");
   return EXIT_SUCCESS;
}
