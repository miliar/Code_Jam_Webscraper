//      bots.cpp
//      
//      Copyright 2011 Antonio <antonio@antonio-laptop>
//      
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//      
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//      
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.


#include <iostream>
#include <fstream>
#include <string.h>
#include <cstdlib>

using namespace std;
//Describe the bot class
class bot{
	private:
		int button_now;
		int button_future;
	public:
	bot();//Constructor
	~bot();//Destructor
	void reset();
	void button_expected(int button_new);//Set a new button destination
	bool next_step(bool priority);//Return true if finished
};
//Implementation for bot class

bot::bot()//Constructor
{
	button_now = 1;//+1 in index
	button_future = -1;
}

bot::~bot()//bot destructor
{
}
void bot::reset()
{
		button_now = 1;
	
}

void bot::button_expected(int button_new)
{
		button_future= button_new;
}
bool bot::next_step(bool priority)
{
	switch(priority)
	{
		case true:
			if(button_now == button_future)
				return true;
			else if (button_now > button_future)
				button_now--;
			else
				button_now++;
			break;//Just in case
		default:
			if(button_now > button_future)
				button_now--;
			else if(button_now < button_future)
				button_now++;
			break;
	}
	return false;
}

//Logic
int main(int argc, char** argv)
{
	char cycles_char[4] = {0};
	int cycles = 0;
	char operations_char[4];
	int operations= 0;
	
	//char bot_one_id_char[2] = {0};
	//char bot_two_id_char[2] = {0};
	
	//char button_bot_one_char[3] = {0};
	//char button_bot_one_char[4] = {0};
	//char button_bot_two_char[4] = {0};
	
	int button_bot_one = 0;
	int button_bot_two = 0;
	
	//int priority = -1;
	
	char line[1000] = {0};
	int step_counter = 0;
	//Instantiate every bot
	bot * orange = new bot();
	bot * blue = new bot();
	//Start to execute the sequence
	string filename = argv[1];
	//Open the filename
	ifstream file_inst (filename.c_str());
	ofstream file_output;
	file_output.open("bot.out",ios::out);
	file_inst >> cycles_char;
	cycles = atoi(cycles_char);
	for(int i = 0 ; i < cycles ; i++)
	{
		file_inst >> operations_char;
		operations = atoi(operations_char);
		if(operations == 0)
			continue;
		bool orange_first = false;
		file_inst.getline(line,1000);
		char * line_orange = line;
		char * line_blue = line;
		//file_inst >> bot_one_id_char;
		//file_inst >> button_bot_one_char;
		//Look for the first orange
		char * orange_actual = strchr(line_orange,'O');
		line_orange = orange_actual;
		line_orange += 2;
		char * blue_actual = strchr(line_blue,'B');			
		line_blue = blue_actual;
		line_blue += 2;
		if((orange_actual < blue_actual && orange_actual != NULL) || (orange_actual != NULL && blue_actual == NULL))
		{
				//Orange is the one with priority
				orange_first = true;
				orange_actual += 2;//Point to the number
				//cout << "The value of orange actual is" << *orange_actual << endl;
			    button_bot_one = atoi(orange_actual);
			    orange->button_expected(button_bot_one);
				if(blue_actual != NULL)
				{
						blue_actual += 2;
						button_bot_two = atoi(blue_actual);
						blue->button_expected(button_bot_two);
				}
				else
					button_bot_two = -1;
		}
		else if ((blue_actual < orange_actual && blue_actual != NULL) || (blue_actual != NULL && orange_actual == NULL))
		{
			orange_first = false;
			blue_actual += 2;
			button_bot_one = atoi(blue_actual);
			//cout << "The value of blue botton" << button_bot_one << endl;
			blue->button_expected(button_bot_one);
			if(orange_actual != NULL)
			{
					orange_actual += 2;
					button_bot_two = atoi(orange_actual);
					orange->button_expected(button_bot_two);
			}
			else
				button_bot_two = -1;
				
		}
		bool pushed_button = false;
		//Should get the rest of the line
		//cout<<"The value of orange_first is "<<orange_first << endl;
		for(int j=0 ;j < operations; j++)
		{
			while(pushed_button == false)
			{
				if(orange_first == true)
				{
					if(button_bot_two != -1)
						pushed_button = blue->next_step(false);	
					pushed_button = orange->next_step(true);
					//cout<<"The value of pushed button is in orange "<<pushed_button<<endl;
					step_counter++;
				}
				else
				{
					if(button_bot_two != -1)
						pushed_button = orange->next_step(false);
					pushed_button = blue->next_step(true);
					//cout<<"The value of pushed button blue is in blue "<<pushed_button<<endl;
					step_counter++;	
				}
			}
			//cout<<"The value of step counter is "<<step_counter<<endl;
				//When finished, a robot has pushed a button	
			if(j < operations)
			{
			//Fetch next operation for robot that has finished
			//file_inst >> bot_one_id_char;
			//file_inst >> button_bot_one_char;	
			if(orange_first == true)
				{
					//Look for the next O instruction
					orange_actual = strchr(line_orange,'O');
					line_orange = orange_actual;
					line_orange +=2;
					if(orange_actual != NULL)
					{
							if((orange_actual < blue_actual) || (orange_actual != NULL && blue_actual == NULL))//Orange still the prioriry
							{
									orange_actual +=2;
									button_bot_one = atoi(orange_actual);
									orange->button_expected(button_bot_one);
								    cout << "Button_bot_one is " <<button_bot_one <<  endl;
							}
							else
							{
									orange_actual +=2;
									button_bot_one = atoi(orange_actual);
									orange->button_expected(button_bot_one);
									orange_first = false;
							}
					}
					else
					{
						orange_first = false;
						button_bot_two = -1;
					}
				}
			else
				{
					blue_actual = strchr(line_blue,'B');
					line_blue = blue_actual;
					line_blue +=2;
					if(blue_actual != NULL)
					{
							if((orange_actual > blue_actual) || (orange_actual == NULL && blue_actual != NULL))//Blue still the prioriry
							{
									blue_actual +=2;
									button_bot_one = atoi(blue_actual);
									blue->button_expected(button_bot_one);
							}
							else
							{
									blue_actual +=2;
									button_bot_one = atoi(blue_actual);
									blue->button_expected(button_bot_one);
									orange_first = true;
							}
					}
					else
					{
						orange_first = true;	
						button_bot_two = -1;
					}
				}
			}
			pushed_button = false;
		}
		//Print the number of steps			
		cout<<"The number of steps are "<<step_counter << endl;
		int p = i + 1;
		file_output<<"Case #"<<p<<": "<<step_counter << endl;
		step_counter = 0;
		//Reset the bots, put them in 1 again
		blue->reset();
		orange->reset();
	}
	file_inst.close();
	file_output.close();
	return 0;
}
