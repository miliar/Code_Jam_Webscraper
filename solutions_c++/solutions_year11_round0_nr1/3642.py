#include <string>
#include <new>
#include <deque>
#include <bitset>
#include <cstring>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

class Order {
	public:
		char Type;
		int Pos;
		Order(char TypeT, int PosT) {
			Type = TypeT;
			Pos = PosT;
		}
};


class Bot {
	public:
		int Pos;
		deque<Order> Tasks;
		bool Finish;
		bool Authorized;
		Bot() {
			Authorized = false;
			Finish = false;
			Pos = 1;
		}
		void AddOrder(Order Temp) {
			Tasks.push_back(Temp);
		}
		void RemoveOrder() {
				Tasks.pop_front();
		}
		Order ViewOrder() {
				Order Temp = Tasks[0];
				return Temp;
		}
		bool OrdersLeft() {
			if (Tasks.size() != 0) {
				return true;
			}
			return false;
		}
};


//Divides String By Spaces
deque<string> Divide(string str)
{
	deque<string> Data;
	//for each space found
	int Count = 0;

	int pos = 0;
	while (str.find(" ",pos)!=string::npos){
		int st = str.find(" ",pos);
		Data.push_back(str.substr(pos, (st)-pos)); //Attach chars left of current space
		Count++; //Set Input for Next
		pos = str.find(" ",pos)+1; //Jump past current space
	}
	Data.push_back(str.substr(pos, str.length()-pos)); //Attach chars right of last space
	return Data;
}


int main()
{
	//arr is allocated
	ifstream Input("input.in");
	string Line;
	getline(Input, Line);
	int NumCases = atoi(Line.c_str());
	deque<string> Lines;
	for (int i=0; i<NumCases; i++) {
		getline(Input,Line);
		Lines.push_back(Line);
	}
	deque<int> CaseAns;
	for (int i=0; i<NumCases; i++) {
		bool Finished = false;
		deque<string> Data = Divide(Lines[i]);
		Bot Orange;
		Bot Blue;
		deque<Order> GlobalOrders;
		int N = atoi(Data[0].c_str());
		int Pos = 1;
		for (int j=0; j<N; j++) {
			char R = Data[Pos].c_str()[0];
			int P = atoi(Data[Pos+1].c_str());
			Order Temp(R, P);
			if (R == 'O') {
				Orange.AddOrder(Temp);
			}
			else if (R == 'B') {
				Blue.AddOrder(Temp);
			}
			GlobalOrders.push_back(Temp);
			Pos+=2;
		}
		//Simulate
		int Time = 0;
		//Initial Authorization
		if (GlobalOrders[0].Type == 'B') {
			Blue.Authorized = true;
		}
		else if (GlobalOrders[0].Type == 'O') {
			Orange.Authorized = true;
		}
		while (Finished == false) {
			//CheckBlue
			bool SpecialCase = false;
			if (Blue.OrdersLeft()) {
				Order Temp = Blue.ViewOrder();
				if (Temp.Pos > Blue.Pos) {
					Blue.Pos++;
				}
				else if (Temp.Pos < Blue.Pos) {
					Blue.Pos--;
				}
				else if (Temp.Pos == Blue.Pos) {
					if (Blue.Authorized == true) {
						//Push Button
						Blue.RemoveOrder();
						GlobalOrders.pop_front();
						//Set Authorization
						Temp = GlobalOrders[0];
						if (Temp.Type == 'O' ) {
							Blue.Authorized = false;
							Orange.Authorized = true;
							SpecialCase = true;
						}
						if (!(Blue.OrdersLeft())) {
							Blue.Finish = true;
						}
					}
				}
			}
			else {
				Blue.Finish = true;
			}
			//CheckOrange
			if (Orange.OrdersLeft()) {
				Order Temp = Orange.ViewOrder();
				if (Temp.Pos > Orange.Pos) {
					Orange.Pos++;
				}
				else if (Temp.Pos < Orange.Pos) {
					Orange.Pos--;
				}
				else if (Temp.Pos == Orange.Pos) {
					if (SpecialCase == false) {
						if (Orange.Authorized == true) {
							//Push Button
							Orange.RemoveOrder();
							GlobalOrders.pop_front();
							//Set Authorization
							Temp = GlobalOrders[0];
							if (Temp.Type == 'B' ) {
								Blue.Authorized = true;
								Orange.Authorized = false;
							}
							if (!(Orange.OrdersLeft())) {
								Orange.Finish = true;
							}
						}
					}
					else if(SpecialCase == true) {
						SpecialCase = false;
					}
				}
			}
			else {
				Orange.Finish = true;
			}
			if (Blue.Finish && Orange.Finish) {
				Finished = true;
			}
			Time++;
		}
		CaseAns.push_back(Time);
		cout << "Finished Case #" << i+1 << ": " << endl;
	}
	cout << "Starting Output" << endl;
	ofstream Output("output.in");
	for (int i=0; i<NumCases; i++) {
		Output << "Case #" << i+1 << ": " << CaseAns[i] << endl;
	}
	return(0);
}
