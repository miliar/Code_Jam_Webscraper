/*
# Text File
# AUTHOR:   gautam
# FILE:     /home/gautam/try/codejam/prog1.cpp
# CREATED:  17:04:57 16/07/2008
# MODIFIED: 17:04:57 16/07/2008
*/
#include <stdio.h>
#include <unistd.h>

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <list>

using namespace std;

#define MAX_N 2
#define MAX_S 3
#define MAX_SIZE 100

int convertvalue(string str){
#ifdef TRACE1
	cout<<str<<endl;
#endif
	int hrs, mins;
	sscanf(str.c_str(), "%d:%d", &hrs, &mins);
#ifdef TRACE1
	cout<<"Hours = "<<hrs<<"Mins = "<<mins<<endl;
#endif
	int num=hrs*60+mins;
#ifdef TRACE
	cout<<num<<endl;
#endif
	return num;
}


int main(int argc, char *argv[]){
	unsigned int num=0;
	char a;
	
	string t_num;
	getline(cin, t_num);
	istringstream ss1(t_num);
	ss1>>num;
#ifdef TRACE
	cout<<"number of cases: "<<num<<endl;
#endif

	for(int t_case=0;t_case<num;t_case++){
		
		int turnaround_time;
		string t_num_turn;
		getline(cin, t_num_turn);
		istringstream ss2(t_num_turn);
		ss2>>turnaround_time;
#ifdef TRACE
		cout<<"Turnaround time = "<<turnaround_time<<endl;
#endif
		
		int na, nb;
		string t_num_ab;
		getline(cin, t_num_ab);
		istringstream ss3(t_num_ab);
		ss3>>na;
		ss3>>nb;

#ifdef TRACE
		cout<<"NA = "<<na<<"NB = "<<nb<<endl;
#endif

		list<int> trains_at_A;
		list<int> trains_at_Ar;
		list<int> trains_at_B;
		list<int> trains_at_Br;

		for(int i=0;i<na;i++){
			string d_times;
			getline(cin, d_times);
			istringstream myss(d_times);
			string timeA, timeB;
			myss>>timeA;
			myss>>timeB;
			int ntimeA=convertvalue(timeA);
			int ntimeB=convertvalue(timeB);
			trains_at_A.push_back(ntimeA);
			trains_at_Br.push_back(ntimeB+turnaround_time);
		}




		for(int i=0;i<nb;i++){
			string d_times;
			getline(cin, d_times);
			istringstream myss(d_times);
			string timeA, timeB;
			myss>>timeB;
			myss>>timeA;
			int ntimeA=convertvalue(timeA);
			int ntimeB=convertvalue(timeB);
			trains_at_Ar.push_back(ntimeA+turnaround_time);
			trains_at_B.push_back(ntimeB);
		}

		trains_at_A.sort();
		trains_at_B.sort();
		trains_at_Ar.sort();
		trains_at_Br.sort();

		int trains_starting_A=na;
		for(list<int>::iterator itero=trains_at_A.begin();itero!=trains_at_A.end();itero++){
			for(list<int>::iterator iter=trains_at_Ar.begin();iter!=trains_at_Ar.end();iter++){
#ifdef TRACE
				cout << "iter = "<<(int)(*iter)<<endl;
#endif
				if(trains_at_Ar.size()){
					//if(trains_at_A[i]>=(int)(*iter)){
					if((int)*itero>=(int)(*iter)){
#ifdef TRACE
						cout<<"Deleted" <<endl;
#endif
						trains_starting_A-=1;
						trains_at_Ar.erase(iter);
						break;
					}
				}
			}
		}
		int trains_starting_B=nb;
		for(list<int>::iterator itero=trains_at_B.begin();itero!=trains_at_B.end();itero++){
			for(list<int>::iterator iter=trains_at_Br.begin();iter!=trains_at_Br.end();iter++){
				if(trains_at_Br.size()){
					//if(trains_at_B[i]>=(int)(*iter)){
					if((int)*itero>=(int)(*iter)){
						trains_starting_B-=1;
						trains_at_Br.erase(iter);
						break;
					}
				}
			}
		}


		cout<< "Case #"<<t_case+1<<": "<<trains_starting_A<<" "<<trains_starting_B<<endl;
	}
	return 0;
}
