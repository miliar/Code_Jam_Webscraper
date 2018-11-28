#include <fstream>
#include <iostream>
#include <string>
#include <set>
#include <ctype.h>
#include <sstream>
#include <stdlib.h>

using namespace std;

int NUMBER[10];

string calc_max(string in){
	
	int j;
	unsigned long tmp;
	char result[21];
	
	for(j=0;j<=10;j++)
			NUMBER[j] = 0;
		
	for(j=0;j<in.size();j++)
		switch(in.at(j)){
			case '1':
				NUMBER[1]++;
				break;
			case '2':
				NUMBER[2]++;
				break;
			case '3':
				NUMBER[3]++;
				break;
			case '4':
				NUMBER[4]++;
				break;
			case '5':
				NUMBER[5]++;
				break;
			case '6':
				NUMBER[6]++;
				break;
			case '7':
				NUMBER[7]++;
				break;
			case '8':
				NUMBER[8]++;
				break;
			case '9':
				NUMBER[9]++;
				break;
			case '0':
				NUMBER[0]++;
				break;
			default:
				break;
		}
		
	j = 1;
	while(1){
		if(NUMBER[j]>0){
			NUMBER[j]--;
			break;
		}
		j++;
	}
	
	tmp = j;
	tmp *= 10;
	for(j=0;j<10;j++)
		if(NUMBER[j] > 0){
			for(int k=0;k<NUMBER[j];k++){
				tmp *= 10;
				tmp += j;
			}
		}
	
	sprintf(result,"%ld",tmp);
	
	return string(result);
	
}

string calc(string in){
	
	int j;
	unsigned long tmp;
	char result[21];
	
	for(j=0;j<=10;j++)
			NUMBER[j] = 0;
		
	for(j=0;j<in.size();j++)
		switch(in.at(j)){
			case '1':
				NUMBER[1]++;
				break;
			case '2':
				NUMBER[2]++;
				break;
			case '3':
				NUMBER[3]++;
				break;
			case '4':
				NUMBER[4]++;
				break;
			case '5':
				NUMBER[5]++;
				break;
			case '6':
				NUMBER[6]++;
				break;
			case '7':
				NUMBER[7]++;
				break;
			case '8':
				NUMBER[8]++;
				break;
			case '9':
				NUMBER[9]++;
				break;
			case '0':
				NUMBER[0]++;
				break;
			default:
				break;
		}
	j=in.at(0) - '0' + 1;
	while(1){
		if(NUMBER[j]>0){
			NUMBER[j]--;
			break;
		}
		j++;
	}
	tmp = j;
	for(j=0;j<10;j++)
		if(NUMBER[j] > 0){
			for(int k=0;k<NUMBER[j];k++){
				tmp *= 10;
				tmp += j;
			}
		}
	
	sprintf(result,"%ld",tmp);
	
	return string(result);
	
}


int main(){
	
	int i,j,loop;
	string input;
	string s;
	string result;
	stringstream ss;
	unsigned long tmp;
	int count = 1;
	
	cin >> loop;
	
	
	//loop
	for(i=0;i<loop;i++){
		
		cin >> input;
		
		if(input.size() > 1){
		
			for(j=input.size()-1;j>0;j--){
				if(input.at(j) > input.at(j-1))
					break;
			}
			
			
			if(j>0){
				s = input.substr(j-1);
				result = input.substr(0,j-1) + calc(s);
			}
			else{
				result = calc_max(input);
			}
			
			ss.str("");
			ss.clear();
			ss << result;
			ss >> tmp;
		}
		else{	
			ss.str("");
			ss.clear();
			ss << input + '0';
			ss >> tmp;
		}
		
	
		cout << "Case #" << count++ << ": " << tmp << endl;
	}

	return 0;
}
