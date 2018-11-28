#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <fstream>

using namespace std;
class player{
public:
	int current_state;
	int current_time;
	player(){
		current_state =1;
		current_time = 0;
	}
};
int test;
char ch;
int place;
int main(){
	ifstream cin("input.in");
	ofstream cout("output.txt");
	cin>>test;
	for (int i=0;i<test;i++){
		player O,B;
		int size;
		cin>>size;
		for (int j=0;j<size;j++){
			cin>>ch;
			cin>>place;

			if (ch == 'O'){
				int time = abs(O.current_state - place);
				O.current_time = max(O.current_time + time, B.current_time)+1;
				O.current_state = place;
			}
			else{
				int time = abs(B.current_state - place);
				B.current_time = max(B.current_time + time, O.current_time)+1;
				B.current_state = place;
			}
		}
		cout<<"Case #"<<i+1<<": "<< max(O.current_time,B.current_time)<<endl;
	}
}