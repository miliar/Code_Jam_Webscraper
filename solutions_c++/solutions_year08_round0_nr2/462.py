//============================================================================
// Name        : alien_numbers.cpp
// Author      : muramasa
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <vector>
#include <numeric>
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <boost/lexical_cast.hpp>
using namespace std;
using boost::lexical_cast;
int main() {
	ifstream ifs("B-small.in");
	ofstream ofs("B-small.out", std::ios::out | std::ios::trunc);
	string buf;
	getline(ifs, buf);
	int cases = lexical_cast<int> (buf);
	cout << "cases : " << cases << endl;
	for (int j = 0; j < cases; j++) {
		int turn_time;
		ifs >> turn_time;
		int a_timetables, b_timetables;
		ifs >> a_timetables >> b_timetables;
		cout << "timetable : " << a_timetables << " " << b_timetables
				<< " delaytime : " << turn_time << endl;
		vector<int> a_start_times, a_end_times;
		vector<int> b_start_times, b_end_times;
		vector<int> a_waitting_train(b_timetables, 1);
		vector<int> b_waitting_train(a_timetables, 1);
		for (int i = 0; i < a_timetables; i++) {
			string start_time, end_time;
			ifs >> start_time >> end_time;
			int start_time_m = lexical_cast<int> (start_time.substr(0, 2)) * 60
					+ lexical_cast<int> (start_time.substr(3, 2));
			a_start_times.push_back(start_time_m);
			int end_time_m = lexical_cast<int> (end_time.substr(0, 2)) * 60
					+ lexical_cast<int> (end_time.substr(3, 2)) + turn_time;
			a_end_times.push_back(end_time_m);
			cout << "a"<<i <<":" <<start_time_m << " " << end_time_m << endl;
		}
		for (int i = 0; i < b_timetables; i++) {
			string start_time, end_time;
			ifs >> start_time >> end_time;
			int start_time_m = lexical_cast<int> (start_time.substr(0, 2)) * 60
					+ lexical_cast<int> (start_time.substr(3, 2));
			int end_time_m = lexical_cast<int> (end_time.substr(0, 2)) * 60
					+ lexical_cast<int> (end_time.substr(3, 2)) + turn_time;
			b_start_times.push_back(start_time_m);
			b_end_times.push_back(end_time_m);
			cout << "b" << i <<":"<< start_time_m << " " << end_time_m << endl;
		}
		int diff_time;
		int table_b_num = -1;
		int trans_a_count = 0;
		//Ａ駅で電車を使い回せる数を数える
		for (int i = 0; i < a_start_times.size(); ++i) {
			cout << "local a" << i << " : " ;
			diff_time = -1;
			for (int k = 0; k < b_end_times.size(); ++k) {
				int local_diff_time = a_start_times[i] - b_end_times[k];
				if (local_diff_time >= 0 && a_waitting_train[k] == 1) {

					if (diff_time >= 0) {
						if (diff_time >= local_diff_time) {
							cout << " b" << k;
							cout << "d." << local_diff_time ;
							cout << "wait_train:"<<table_b_num<<"->";
							a_waitting_train[table_b_num] = 1;
							diff_time = local_diff_time;
							table_b_num = k;
							a_waitting_train[table_b_num] = 0;
							cout << table_b_num<<" ";
						}
					} else {
						cout << " b" << k;
						cout << "c." << local_diff_time ;
						trans_a_count++;
						diff_time = local_diff_time;
						table_b_num = k;
						a_waitting_train[table_b_num] = 0;
						cout << "wait_train:"<<table_b_num;
					}
				}
			}
			cout << endl;
			cout << "trans_a_count : " << trans_a_count << endl;
		}
		int a_train_n = a_timetables - trans_a_count;

		int table_a_num = -1;
		int trans_b_count = 0;
		//Ａ駅で電車を使い回せる数を数える
		for (int i = 0; i < b_start_times.size(); ++i) {
			cout << "local b"<<i<<" : " ;
			diff_time = -1;
			for (int k = 0; k < a_end_times.size(); ++k) {
				int local_diff_time = b_start_times[i] - a_end_times[k];
				if (local_diff_time >= 0 && b_waitting_train[k] == 1) {
					if (diff_time >= 0) {
						if (diff_time >= local_diff_time) {
							cout << " a" << k;
							cout << "d." << local_diff_time ;
							cout << "wait_train:"<<table_a_num<<"->";
							b_waitting_train[table_a_num] = 1;
							diff_time = local_diff_time;
							table_a_num = k;
							b_waitting_train[table_a_num] = 0;
							cout << "wait_train:"<<table_a_num;
						}
					} else {
						cout << " a" << k;
						cout << "c." << local_diff_time ;
						trans_b_count++;
						diff_time = local_diff_time;
						table_a_num = k;
						b_waitting_train[table_a_num] = 0;
						cout << "wait_train:"<<table_a_num;
					}
				}
			}
			cout<<endl;
			cout << "trans_b_count : " << trans_b_count << endl;
		}
		int b_train_n = b_timetables - trans_b_count;
		cout << "Case #" << j+1 << ": " <<a_train_n  <<" " << b_train_n<<endl;
		ofs << "Case #" << j+1 << ": " <<a_train_n  <<" " << b_train_n<<endl;
	}
	return 0;
}
