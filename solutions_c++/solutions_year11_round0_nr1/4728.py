#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <stack>
#include <iomanip>
#include <list>
#include <string>
#include <sstream>
#include <cassert>
#include <deque>
#include <queue>
using namespace std;



struct Robot
{
	int cur_pos;
	int tar_pos;
};

struct Step
{
	char robot;
	int button;
};

typedef deque<Step> Steps;


void solve_a_case(ifstream &in, int &result)
{
	int num_of_button;
	in >> num_of_button;
	
	Steps steps(num_of_button);
	
	deque<int> Orange_queue;
	deque<int> Blue_queue;
	
	Robot Orange_robot, Blue_robot;
	
	
	
	for(int i=0; i<steps.size(); ++i)
	{
		Step m;
		in >> m.robot;
		in >> m.button;
		steps[i] = m;

		if(m.robot=='O')
			Orange_queue.push_back(m.button);
		else
			Blue_queue.push_back(m.button);

		//cout << "robot: " << steps[i].robot << " botton: " << steps[i].button << endl;
	}
	
	cout << "Orange_queue: ";
	for (int i=0; i< Orange_queue.size(); i++) 
	{
		cout << Orange_queue[i] << ",";
	}
	
	cout << endl << "Blue_queue: ";
	for (int i=0; i< Blue_queue.size(); i++) 
	{
		cout << Blue_queue[i] << ",";
	}
	cout << endl;
	
	
	Orange_robot.cur_pos = 1;
	Blue_robot.cur_pos = 1;
	
	
	bool isOrangePressButton = false;
	bool isBluePressButton = false;
	
	if(Orange_queue.size())
	{
		Orange_robot.tar_pos = Orange_queue.front();
		Orange_queue.pop_front();
	}
	
	if(Blue_queue.size())
	{
		Blue_robot.tar_pos = Blue_queue.front();
		Blue_queue.pop_front();
	}

	cout << "Case: " << endl;
	
	while (steps.size()) 
	{
		cout << "Time: " << result;
		
		if(steps[0].robot == 'O' && Orange_robot.tar_pos == Orange_robot.cur_pos)
		{
			
			
			steps.pop_front();
			
			cout << " Orange press " << Orange_robot.cur_pos;
			
			isOrangePressButton = true;
			
			if(Orange_queue.size())
			{
				Orange_robot.tar_pos = Orange_queue.front();
				Orange_queue.pop_front();
			}
			
		}	  
	    else if(steps[0].robot == 'B' && Blue_robot.tar_pos == Blue_robot.cur_pos)
		{
			steps.pop_front();
			
			cout << " Blue press " << Orange_robot.cur_pos;
			
			isBluePressButton = true;
			
			if(Blue_queue.size())
			{
				Blue_robot.tar_pos = Blue_queue.front();
				Blue_queue.pop_front();
			}
		}
		
				
		if(!isOrangePressButton)
		{
			
			if(Orange_robot.tar_pos != Orange_robot.cur_pos)
			{
				if(Orange_robot.cur_pos<Orange_robot.tar_pos) 
				   Orange_robot.cur_pos++;
				else
				   Orange_robot.cur_pos--;
				
				cout << " Orange->: " << Orange_robot.cur_pos << ";";
			}
			else 
			{
				cout << " Orange stay at " << Orange_robot.cur_pos << ";";
			}

			/*
			else 
			{
				if(Orange_queue.size())
					Orange_robot.tar_pos = Orange_queue.front();
				Orange_queue.pop_front();
			}
			 */
		}	
		
		if(!isBluePressButton)
		{
		   if(Blue_robot.tar_pos != Blue_robot.cur_pos)
		   {
			   if(Blue_robot.cur_pos<Blue_robot.tar_pos)
				   Blue_robot.cur_pos++;
			   
			   else
				  Blue_robot.cur_pos--;
			   
			   cout << " Blue->: " << Blue_robot.cur_pos << ";";
		   }
		   else 
		   {
			   cout << " Blue stay at " << Blue_robot.cur_pos << ";";
		   }

		/*	
		   else 
		   {
			   if(Blue_queue.size())
					Blue_robot.tar_pos = Blue_queue.front();
				Blue_queue.pop_front();
		   }
	   */
			
		}
		cout << endl;
		
		result++;
		
		isBluePressButton = isOrangePressButton = false;

			  
	}
	
	
	
}

void solve_all_cases(ifstream &in, ofstream &out)
{
	int case_num = 0;
	
	in >> case_num;
	for(int i=0; i<case_num; i++)
	{
		int r = 1;
		solve_a_case(in, r);
		

		out << "Case #" << i+1 << ": " << r-1 << endl;
	}
}

int main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	
	solve_all_cases(in, out);
	
	return 0;
}