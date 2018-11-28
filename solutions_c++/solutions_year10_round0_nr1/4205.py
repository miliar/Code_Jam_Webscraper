#include <stack>
#include <utility> 
#include <vector>
#include <queue>
#include <math.h>
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <fstream>
#include <map>
using namespace std;


class Lights{
public:
	void onoff(){
	    ifstream input;
		input.open("A-small-attempt0.in",ios::in);
		ofstream output;
		output.open("A-small-attempt0.out",ios::out);
		
		int t;
		input>>t;
		int n,k;
		for (int i = 0; i < t; i++){
			input>>n>>k;
			bool arr[10];
			int j;
			for (j = 0; j < n; j++) arr[j] = 0;
			int ret;
			if(k > 0){
				for (j = 0; j < k; j++){
					int st = 0;
					while(arr[st] == 1){
						arr[st] = 0;
						st++;
					}
					arr[st] = !arr[st];
				}
				ret = 1;
				for(j = 0; j < n; j++){
					if (arr[j] != 1){
						ret = 0;
						break;
					}
				}
			}
			else ret = 0;
			output<<"Case #"<< i + 1<<": ";
			if(ret) output<<"ON";
			else output<<"OFF";
			output<<endl;

		}
		
		input.close();
		output.close();
	};
};


void main()
{
	Lights s;
	s.onoff();
}


/*
	output<<"Case #"<<i+1<<": ";
			for(k = 0; k < arr.size(); k++) output<<arr[k];
			output<<endl;
*/
