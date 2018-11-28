//============================================================================
// Name        : eldavojohn
// Author      : 
// Version     :
// Copyright   : Whoever wants it gets it for whatever reason!
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

int main() {
	int case_count = 0, button_count = 0, button_index = 0, button_ind = 0,
			time = 0, b_state = 0, o_state = 0, b_ind = 0, o_ind = 0,
			b_loc = 1, o_loc = 1, case_ind = 0;
	char *tokens, *color;
	string rd_line;
	ifstream input_txt("A-large.in");
	ofstream output_txt("A-large.out");

	if (input_txt.is_open()) {

		// always assume at least one line with # of examples
		getline(input_txt, rd_line);
		case_count = atoi((char *) rd_line.c_str());

		// while the file is still good and the case count has not been maxxed
		while (input_txt.good() && case_count > case_ind) {
			button_count = 0, button_index = 0, button_ind = 0, time = 0, b_state
					= 0, o_state = 0, b_ind = 0, o_ind = 0, b_loc = 1, o_loc
					= 1;
			int color_seq[100] = { 0 }, index_seq[100] = { 0 };
			getline(input_txt, rd_line);
			// tokenize string
			tokens = strtok((char *) rd_line.c_str(), " ");
			button_count = atoi(tokens);
			tokens = strtok(NULL, " ");
			while (tokens != NULL) {
				// color
				color = tokens;
				tokens = strtok(NULL, " ");
				// position
				button_index = atoi(tokens);
				tokens = strtok(NULL, " ");

				// load into master arrays
				color_seq[button_ind] = *color;
				index_seq[button_ind] = button_index;
				button_ind++;
				if (*color == 'B') {
				}
			}
			// state key: -1 is finished, 0 is ready, 1 is pushing and 2 is moving
			while (b_state != -1 || o_state != -1) {

				// but what happens if they push it at the same time?
				while (color_seq[b_ind] != 'B' && b_state != -1) {
					if (b_ind < 100 && index_seq[b_ind] != 0) {
						b_ind++;
						// printf("Indexes are O:%i and B:%i\n", o_ind, b_ind);
						// printf("Seqvalues are O:%i and B:%i\n", index_seq[o_ind], index_seq[b_ind]);
						// printf("Locvalues are O:%i and B:%i\n", o_loc, b_loc);
					} else {
						// printf("done with b!");
						b_state = -1;
					}
				}
				while (color_seq[o_ind] != 'O' && o_state != -1) {
					if (o_ind < 100 && index_seq[o_ind] != 0) {
						o_ind++;
						// printf("Indexes are O:%i and B:%i\n", o_ind, b_ind);
						// printf("Seqvalues are O:%i and B:%i\n", index_seq[o_ind], index_seq[b_ind]);
						// printf("Locvalues are O:%i and B:%i\n", o_loc, b_loc);
					} else {
						// printf("done with o!");
						o_state = -1;
					}
				}
				// printf("Indexes are O:%i and B:%i\n", o_ind, b_ind);

				if (b_state != -1) {
					if (b_loc == index_seq[b_ind] && b_ind < o_ind) {
						// push the button, frank!
						// printf("pushing b! at time %i\n", time);
						b_state = 1;
						b_ind++;
						// printf("Indexes are O:%i and B:%i\n", o_ind, b_ind);
					} else if (b_loc == index_seq[b_ind] && b_ind > o_ind) {
						// need to wait for o to catch up so do nothing
					} else if (b_loc != index_seq[b_ind]) {
						b_state = 2;
						if (b_loc < index_seq[b_ind]) {
							b_loc++;
						} else {
							b_loc--;
						}
					}
				}
				if (o_state != -1) {
					if (o_loc == index_seq[o_ind] && o_ind < b_ind) {
						// push the button, frank!
						// printf("pushing o! at time %i\n", time);
						o_state = 1;
						o_ind++;
						// printf("Indexes are O:%i and B:%i\n", o_ind, b_ind);
					} else if (o_loc == index_seq[o_ind] && o_ind > b_ind) {
						// need to wait for o to catch up so do nothing
					} else if (o_loc != index_seq[o_ind]) {
						o_state = 2;
						if (o_loc < index_seq[o_ind]) {
							o_loc++;
						} else {
							o_loc--;
						}
					}
				}
				if (b_state != -1 || o_state != -1) {
					time++;
				}
			}

			case_ind++;
			printf("Case #%i: %i\n", case_ind, time);
			output_txt << "Case #" << case_ind << ": " << time << "\n";
		}
	}
	input_txt.close();
	output_txt.close();

	return 0;
}
