// task1_robots.cpp : Defines the entry polong long for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>

#define MAX(X,Y) X>Y?X:Y
using namespace std;

long long max(long long i, long long j) {
	if (i > j) {
		return i;
	} else {
		return j;
	}
	return 0;
}
int _tmain(int argc, _TCHAR* argv[])
{
	fstream file_in("A-large.in", ios::in);
	fstream file_out("out_large.txt", ios::out);
	long long test_cases = 0;
	file_in >> test_cases;
	//vector<long long> blue_vec, orange_vec;
	long long buttons_numb;
	for (long long i = 0; i < test_cases; ++i) {
		file_in >> buttons_numb;
		long long step_numb = 0;
		long long orange_steps = 0;
		long long blue_steps = 0;
		long long orange_pos = 1;
		long long blue_pos = 1;
		char in_robot;
		long long in_button;
		bool orange_works = false;
		bool blue_works = false;
		long long steps_remained_orange = 0;
		long long steps_remained_blue = 0;
		long long orange_remains = 0;
		long long blue_remains = 0;
		long long orange_step_ended = 0;
		long long blue_step_ended = 0;
		bool orange_last = false;
		bool blue_last = false;
		for (long long j = 0; j < buttons_numb; ++j) {
			file_in >> in_robot;
			file_in >> in_button;
			if (in_robot == 'O') {
				orange_works = true;
				if (blue_last) {	
					orange_steps = max(abs(orange_pos - in_button) + 1 - orange_remains, 1) + blue_step_ended;
				} else {
					orange_steps = max(abs(orange_pos - in_button) + 1 - orange_remains, 1) + orange_step_ended;
				}
				if (1){//!blue_works) {
					blue_remains = orange_steps - blue_step_ended;//max(abs(orange_pos - in_button) + 1 - orange_remains + orange_step_ended - blue_step_ended, 0);
					orange_remains = 0;
				}
				orange_pos = in_button;
				orange_step_ended = orange_steps;
				orange_last = true;
				blue_last = false;
			} else {
				blue_works = true;
				if (orange_last) {	
					blue_steps = max(abs(blue_pos - in_button) + 1 - blue_remains, 1) + orange_step_ended;
				} else {
					blue_steps = max(abs(blue_pos - in_button) + 1 - blue_remains, 1) + blue_step_ended;
				}
				if (1){//!orange_works) {
					orange_remains = blue_steps - orange_step_ended;//max(abs(blue_pos - in_button) + 1 - blue_remains + blue_step_ended - orange_step_ended, 0);
					blue_remains = 0;
				}
				blue_pos = in_button;
				blue_step_ended = blue_steps;
				blue_last = true;
				orange_last = false;
			}
			if (blue_works & orange_works) {

			}

		}
		step_numb = MAX(blue_steps, orange_steps);
		//	if (in_robot == 'O') {
		//		orange_works = true;
		//		orange_steps += max(abs(orange_pos - in_button) + 1 - steps_remained_orange, 1);
		//		orange_pos = in_button;
		//		steps_remained_orange = 0;
		//	} else {
		//		blue_works = true;
		//		blue_steps += max(abs(blue_pos - in_button) + 1 - steps_remained_blue, 1);
		//		blue_pos = in_button;
		//		steps_remained_blue = 0;
		//	}
		//	if (blue_works && orange_works) {
		//		step_numb += max(orange_steps, blue_steps);
		//		if (blue_steps > orange_steps) {
		//			steps_remained_orange = blue_steps - orange_steps;
		//		} else {
		//			steps_remained_blue = orange_steps - blue_steps;
		//		}
		//		blue_works = false;
		//		orange_works = false;
		//	}
		//}
		//if (blue_works) {
		//	step_numb += blue_steps;
		//} else if (orange_works) {
		//	step_numb += orange_steps;
		//}
		file_out << "Case #" << i + 1 << ": " << step_numb << endl;
	}
	file_in.close();
	file_out.close();
	return 0;
}

