#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <vector>
#include <stdlib.h>
using namespace std;

int get_steps_num(map<string, vector <int> > robots_tasks, vector<pair<string, int> > seq)
{
   //int length = (robots_tasks["O"] > robots_tasks["B"]) ? robots_tasks["B"].size() : robots_tasks["O"].size();
      
   int o_but_inx = 0;
   int b_but_inx = 0;
   int o_pos = 1;
   int b_pos = 1;
   int step_count = 0;
   
   for (int i=0; i < seq.size(); ++i)
   {
     if (seq[i].first == "O")
     {
        int steps = abs(seq[i].second - o_pos) + 1;
         
        //cout << "steps: " << steps << endl;

        step_count += steps;
        
        ++o_but_inx;
        o_pos = seq[i].second;

        if (b_but_inx >= robots_tasks["B"].size()) continue;


        int next_dist = abs(robots_tasks["B"][b_but_inx] - b_pos); 

        if (steps <next_dist)
        {
           b_pos += (robots_tasks["B"][b_but_inx] < b_pos)? - steps : steps;
        }
        else
        {
          b_pos = robots_tasks["B"][b_but_inx];
        } 
      }
      else
      {
        int steps = abs(seq[i].second - b_pos) + 1;
        step_count += steps;

        //cout << "steps: " << steps << endl;


        ++b_but_inx;
        b_pos = seq[i].second;

        if (o_but_inx >= robots_tasks["O"].size()) continue;

        int next_dist = abs(robots_tasks["O"][o_but_inx] - o_pos);

        if (steps <next_dist)
        {
           o_pos += (robots_tasks["O"][o_but_inx] < o_pos)? - steps : steps;
        }
        else
        {
          o_pos = robots_tasks["O"][o_but_inx];
        } 
      }

     }
   
     return step_count;

}



int main()
{

    int cases_num;
    
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    if (fin.is_open())
    {
      //cout << "file is open";
      fin >> cases_num;
      
      for (int i=0; i < cases_num; ++i)
      {
         int buttons_num;
         fin >> buttons_num;
         map<string, vector<int> > robots_tasks;
         vector<pair<string, int> > tasks;
         
          
         for (int x=0; x< buttons_num; ++x )
         {
            string robot;
            int button_id;

	    fin >> robot;
            fin >> button_id;
            robots_tasks[robot].push_back(button_id);
            tasks.push_back(pair<string, int>(robot, button_id));
         }
         fout << "Case #" << i+1 << ": "<< get_steps_num(robots_tasks, tasks)<< endl;
	 
          
      }
    }

   
    

    /*std::cin >> cases_num; 
    std::cout << "number of cases " << cases_num << std::endl;
    for (int i=0; i<cases_num; ++i)
    {

    }*/
}
