//============================================================================
// Name        : codejam_2012_2.cpp
// Author      : festony
// Version     :
// Copyright   : blooooz
// Description : Hello World in C++, Ansi-style
//============================================================================


#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <deque>
#include <set>
#include <algorithm>
using namespace std;

typedef long long LL;

struct reach {
	LL base;
	LL length;
	LL reach_point;
	LL max_reach_point;
};

vector<reach> path;

LL get_reach_point(reach new_vine) {
	int s = path.size();
	LL new_reach_point = new_vine.base;
	LL temp;
	for(int i=s-1; i>=0; i--) {
		if(path[i].max_reach_point < new_vine.base) {
			break;
		}
		if(path[i].reach_point < new_vine.base) {
			continue;
		}
		temp = new_vine.base - path[i].base;
		temp = temp > new_vine.length ? new_vine.length:temp;
		if(new_vine.base + temp > new_reach_point) {
			new_reach_point = new_vine.base + temp;
		}
	}
	return new_reach_point;
}

//bool ledge_reachable(LL D) {
//	int s = path.size();
//	reach last = path[s-1];
//	LL last_distance = D - last.base;
//	for(int i=s-1; i>=0; i++) {
//		if(path[i].base < new_vine.base - new_vine.length) {
//			break;
//		}
//		new_reach_point = new_vine.base + (new_vine.base - path[i].base);
//	}
//}

static string process(int case_num, fstream & in) {
	clock_t t1=clock();
	char buf[10240];
	string temp_str = "";
	string result = "";

	cout << "case " << case_num << endl;
	LL N, D;
	path.clear();
	bool reachable = true;
	reach temp;
	in >> N;
	LL max_reach_point = 0;
	int last_reach = -1;
	for(LL i=0; i<N; i++) {
		in >> temp.base;
		in >> temp.length;
		if(i>0) {
			if(temp.base > max_reach_point) {
				continue;
			}
		}
		if(reachable) {
//			if(i==0 && temp.length > temp.base) {
//				temp.reach_point = temp.base * 2;
//			} else {
//				temp.reach_point = get_reach_point(temp);
//			}
			if(i==0) {
				temp.reach_point = temp.base * 2;
			} else {
				temp.reach_point = get_reach_point(temp);
				cout << temp.base << " " << temp.reach_point << endl;
			}
			if(temp.reach_point > max_reach_point) {
				max_reach_point = temp.reach_point;
			}
			temp.max_reach_point = max_reach_point;
			last_reach ++;
			path.push_back(temp);
		}
	}
	in >> D;
	if (reachable) {
		temp = path[last_reach];
		if (temp.reach_point == temp.base) {
			temp.reach_point = temp.base + temp.length;
		}
		if (temp.reach_point > max_reach_point) {
			max_reach_point = temp.reach_point;
		}
	}
	if(max_reach_point < D) {
		reachable = false;
	} else {
		reachable = true;
	}
	if(reachable) {
		temp_str = "YES";
	} else {
		temp_str = "NO";
	}


	sprintf(buf, "Case #%d: %s\n", case_num + 1, temp_str.c_str());
	clock_t t2=clock();
	cout<<"Iteration " << case_num + 1 << " took " << t2-t1 << " mini seconds" << endl;
	result.append(buf);
	return result;
}

int main() {
	int caseNum = 0;
	fstream in("F:\\Users\\festony\\Downloads\\codejam\\2012_2\\A-small-attempt3.in");
	fstream out("F:\\Users\\festony\\Downloads\\codejam\\2012_2\\testout7.txt", ios_base::out | ios_base::trunc);

	in >> caseNum;
	in.ignore(256, '\n');
	char buf[10240];

	string result = "";

	for(int i=0; i<caseNum; i++) {
		result.append(process(i, in));
	}
	cout << result;
	out << result;
	in.close();
	out.close();

}

