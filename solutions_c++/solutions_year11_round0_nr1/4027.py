#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

#define UNDEFINED 0
#define ORANGE  1
#define BLUE    2

class Item {
	public:
	     Item (int clr , int NT) {
		    color = clr;
		    next_target = NT;
		}
	     void set(int clr , int NT) {
		    color = clr;
		    next_target = NT;
		}
		Item () {
		    color = UNDEFINED;
		    next_target = 1;
		}
		void set_next_target(int NT) {
			next_target = NT;
		}
		int  get_target() {
			return next_target;
		}
		void set_color (int clr) {
			color = color;
		}
		int  get_color () {
			return color;
		}
	private:
		int color;
		int next_target;
};


void FindTime(Item *all_items, int N, int case_num) {
	int orange_last_target = 1;
	int blue_last_target = 1;
	int ticks = 0;
	int orange_tick_credit = 0;
	int blue_tick_credit = 0;
	int delta = 0;
	for (int i = 0; i < N ; i++) {
		switch (all_items[i].get_color()) {
			case ORANGE:
				//cout << "[INFO] OLT " << orange_last_target << " OTC " << 
				//	orange_tick_credit << endl;
				if (all_items[i].get_target() >
				    (orange_last_target + orange_tick_credit)) {
				     delta = all_items[i].get_target() - 
					        orange_last_target - orange_tick_credit;

				    blue_tick_credit += delta;
				    ticks            += delta;

				} else if (all_items[i].get_target() < 
						(orange_last_target - orange_tick_credit)) {

				    delta = orange_last_target - all_items[i].get_target()
					       - orange_tick_credit;

				    blue_tick_credit += delta;
				    ticks            += delta;
				}
				orange_last_target = all_items[i].get_target();
				// push orange
				ticks++;
				blue_tick_credit++;
				orange_tick_credit = 0;

				//cout << " Ticks " << ticks << " ";
				//cout << " Orange last button " << orange_last_target << " Pushed ";
				//cout << " Blue Tick Credit " << blue_tick_credit << endl;

				break;
			case BLUE:
				//cout << "[INFO] BLT " << blue_last_target << " BTC " << 
				//	 blue_tick_credit << endl;
				if (all_items[i].get_target() 
						   > (blue_last_target + blue_tick_credit)) {

				    delta = all_items[i].get_target() - blue_last_target
					       - blue_tick_credit;

				    orange_tick_credit +=  delta;
				    ticks              +=  delta;

				} else if (all_items[i].get_target() 
						   < (blue_last_target - blue_tick_credit)) {
				    delta = blue_last_target - all_items[i].get_target()
					       - blue_tick_credit;
				    orange_tick_credit += delta;
				    ticks += delta;
				}
				blue_last_target = all_items[i].get_target();
				//push blue
				ticks++;
				orange_tick_credit++;
				blue_tick_credit = 0;

				//cout << " Ticks " << ticks << " ";
				//cout << " Blue last button " << blue_last_target << " Pushed ";
				//cout << " Orange Tick Credit " << orange_tick_credit << endl;
				break;
			default: 
				    break;
		}
	}
	cout << "Case #" << case_num <<": " <<ticks << endl;
}

int main() {
	int case_num = 1;
	char buffer[100];
	string str;
	bool first = 0;
	int N, total_cases;
	char COLOR;
	int BUTTON;


	ifstream read_file ("data");
	if (read_file.is_open()) {
	    while (getline(read_file, str)) {
			 if (!first) {
				 total_cases = atoi(str.c_str());
				 first = 1;
			 } else {
				 stringstream ss(str);
				 ss >> N;
	                Item *all_items = new Item[N];
				 for (int j = 0; j < N; j++) {
					 ss >> COLOR >> BUTTON;
					 if (COLOR == 'O') 
					  all_items[j].set(ORANGE, BUTTON);
					 else 
					  all_items[j].set(BLUE, BUTTON);
			      }
				 FindTime(all_items, N, case_num++);
				 delete [] all_items;
			 }
	    }
	    read_file.close();
	}
}
