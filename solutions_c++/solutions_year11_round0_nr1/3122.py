//#include <stdlib>
#include <iostream>
#include <map>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    freopen("A.in" , "r" , stdin);
	freopen("A-out.out" , "w" , stdout);
    
    int T;   
    cin>>T;

     for(int caseID = 1 ; caseID <= T ; caseID ++){
		int numActions;
		char robot;
		int pos_O = 1, pos_B = 1;
		int act_pos;
		char last_robot = ' ';
		int cur_robot_cost=0;
		int all_cost =0;

		cin >> numActions;

		for (int i=0; i< numActions; i++)
		{
			cin >> robot;
			cin >> act_pos;
			if(robot == last_robot){
				if(robot == 'O'){
					int gap = (act_pos > pos_O)? (act_pos - pos_O):(pos_O - act_pos);
					all_cost += gap + 1;
					cur_robot_cost += gap + 1;
					pos_O = act_pos;
					//last_robot = 'O';
				}else{
					int gap = (act_pos > pos_B)? (act_pos - pos_B):(pos_B - act_pos);
					all_cost += gap + 1;
					cur_robot_cost += gap + 1;
					pos_B = act_pos;
				}
			}else{
				int last_robot_cost = cur_robot_cost;
				cur_robot_cost = 0; 
				if(robot == 'O'){
					int gap = (act_pos > pos_O)? (act_pos - pos_O):(pos_O - act_pos);
					if (last_robot_cost > gap){
						gap = 0;
					}else{
						gap -= last_robot_cost;
					}
				
					cur_robot_cost += gap + 1;
					all_cost += gap + 1;

					pos_O = act_pos;
				//	last_robot='O';
				}else{
					int gap = (act_pos > pos_B)? (act_pos - pos_B):(pos_B - act_pos);
					if (last_robot_cost > gap){
						gap = 0;
					}else{
						gap -= last_robot_cost;
					}
					
					cur_robot_cost += gap + 1;
					all_cost += gap + 1;
					
					pos_B = act_pos;
				//	last_robot='B';
				}
			}

			last_robot = robot;
		}

        cout<<"Case #"<<caseID<<": "<<all_cost<<"\n";             

     }
     

   // system("PAUSE");
    return 0;
}
