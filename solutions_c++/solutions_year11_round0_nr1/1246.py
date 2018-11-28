#include <iostream>

using namespace std;

int get_next_orange_move(int orange_pos, int orange_obj, bool is_orange_first);
int get_next_blue_move(int blue_pos, int blue_obj, bool is_blue_first);
int process(char colors[], int ids[], int button_count);
void get_next_buttons(char colors[], int ids[], int * orange_target, int * blue_target, bool * is_orange_first, int processed, int button_count);

int main(int argc, char * argv) {

	int linecount = 0;
	int nb_buttons = 0;
	cin >> linecount;

	for (int i = 0; i < linecount; i++) {
		cin >> nb_buttons;
		char colors [nb_buttons];
		int ids [nb_buttons];
		for (int j = 0; j < nb_buttons; j++) {
			cin >> colors[j];
			cin >> ids[j];
		}
		int nb_shots = process(colors, ids, nb_buttons);
		cout << "Case #" << i+1 << ": " << nb_shots << endl;
	}

	return 0;
}

int process(char colors[], int ids[], int button_count) {
	int shots = 0;
	
	int processed_buttons = 0;

	int orange_pos = 1;
	int blue_pos = 1;

	int orange_target = -1;
	int blue_target = -1;
	bool is_orange_first = true;

	while (processed_buttons < button_count) {

		get_next_buttons(colors, ids, &orange_target, &blue_target, &is_orange_first, processed_buttons,button_count);
		
		int orng_move = get_next_orange_move(orange_pos, orange_target, is_orange_first);
		if (orng_move == -1) {
			orange_pos--;
//			cout << "Orange back to " << orange_pos << endl;
		} else if (orng_move == +1) {
			orange_pos++;
//			cout << "Orange forward to " << orange_pos << endl;
		} else if (orng_move == 2) {
			processed_buttons++;
//			cout << "Orange pushes buttons " << orange_pos << endl;
		} else if (orng_move == 0) {
//			cout << "Orange stays on " << orange_pos << endl;
		}	

		int blue_move = get_next_blue_move(blue_pos, blue_target, !is_orange_first);
		if (blue_move == -1) {
			blue_pos--;
//			cout << "Blue back to " << blue_pos << endl;
		} else if (blue_move == +1) {
			blue_pos++;
//			cout << "Blue forward to " << blue_pos << endl;
		} else if (blue_move == 2) {
			processed_buttons++;
//			cout << "Blue pushes button " << blue_pos << endl;
		} else if (blue_move == 0) {
//			cout << "Blue stays on " << blue_pos << endl;
		}
		
		shots++;
//		cout << endl;
	}	
/*
	for (int k = 0; k < button_count; k++) {
		cout << colors[k] << "->" << ids[k] << endl;
	}
*/
	return shots;
}

/*
 Returns -1 for go_back, +1 for go_forward, 0 for do_nothing, and 2 to
 push_button */
int get_next_orange_move(int orange_pos,
				int orange_obj,
				bool is_orange_first) {
	if (orange_obj == -1) {
		return 0;
	} else if (orange_pos == orange_obj) {
		if (is_orange_first) {
			return 2;
		} else {
			return 0;
		}
	} else if (orange_pos > orange_obj) {
		return -1;
	} else if (orange_pos < orange_obj) {
		return +1;
	} else {
		return -2;
	}
}

int get_next_blue_move(int blue_pos, int blue_obj, bool is_blue_first) {
	return get_next_orange_move(blue_pos, blue_obj, is_blue_first);
}

void get_next_buttons (char colors[], int ids[], int * orange_target,
			int * blue_target, bool * is_orange_first, int processed, int size) {

	int blue_k = 101;
	int orange_k = 101;
	
	int k = processed;
	bool done = false;
	while (!done && k < size) {
		if (colors[k] == 'O') {
			*orange_target = ids[k];	
			orange_k = k;
			done = true;
		}
		k++;
	}	

	k = processed;
	done = false;
	while(!done && k < size) {
		if (colors[k] == 'B') {
			*blue_target = ids[k];
			blue_k = k;
			done = true;
		}
		k++;
	}

	*is_orange_first = (orange_k < blue_k);
}	
