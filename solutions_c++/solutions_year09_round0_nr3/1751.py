//============================================================================
// Name        : welcome.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>

using namespace std;

char data[500];
char find_this[20] = "welcome to code jam";
int len;
int a;
void find_data(int current_index,int data_index)
{
	if(data_index > len) return;
	if(current_index==19)
	{
		++a;
	}
	for(int i = data_index; i < len ; ++i){
		if(find_this[current_index]==data[i])
		{
			find_data(current_index+1,i+1);
		}
	}

}

int main() {
	int n;

	ifstream fcin;
	ofstream fcout;

	fcout.open("C.out");
//	fcin.open("C-small.in");
	fcin.open("C-small-attempt0.in");

	fcin >> n;
	fcin.getline(data,0);
	for(int i = 0 ; i < n ; ++i)
	{
		fcin.getline(data,500);
		len = strlen(data);
		a = 0;
		find_data(0,0);
		cout << "Case #" << i+1 << ": ";
		fcout << "Case #" << i+1 << ": ";
		int k = 1000;
		while(k > 1){
			cout << a/k;
			fcout << a/k;
			a = a%k;
			k = k / 10;
		}
		cout << a << endl;
		fcout << a << endl;
	}
	return 0;
}
