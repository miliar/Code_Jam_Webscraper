#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <algorithm>

#define ARRAY_SIZE 22
#define MIN_RESET 10
#define INPUT_FILE "B-large.in"

using namespace std;

int main(){

	ifstream in(INPUT_FILE);
	ofstream out("g.out");
	
	int k;
	string number ="";
	
	in>>k;
	
	for(int i=0; i<k; i++){
	
		in>>number;
		int digits[ARRAY_SIZE] = {0};
		int currentDigit = 0;
		int size = number.size();
		bool moved = false;
		
		// Separate digits
		for(int h=0; h<size; h++){
			digits[h] = number[h] -'0';
		}
		
		if(size>1){
			currentDigit = number.size()-2;
		}
		
		int rMin =MIN_RESET, rMinIndex = -1;
		
		while(currentDigit != -1){
			// Find min number that is larger than currentEntry
			rMin = MIN_RESET;
			rMinIndex = -1;
			
			for(int j=currentDigit; j<number.size(); j++){
				if(digits[j] > digits[currentDigit] && digits[j] < rMin){
				    rMin = digits[j];
					rMinIndex = j;
				}
			}
			
			if(rMin > digits[currentDigit] && rMin != MIN_RESET){
			    digits[rMinIndex] = digits[currentDigit];
				digits[currentDigit] = rMin;
				// Sort after current index
				sort(digits+currentDigit+1, digits+number.size());
				moved = true;
				break;
			}
			
			currentDigit--;
			
		}
		
		if(!moved){
			//sort the whole list and add 0 in second place
			sort(digits,&digits[number.size()]);
			int temp = 0;
			size++;
			if(size > 2){
				for(int r=number.size()-1; r>=1; r--){
					digits[r+1] = digits[r];
				}
			}
			
			digits[1] = 0;
			
		}
		
		// Check for leading zeros
		if(digits[0] == 0){
			for(int w=1; w<size; w++){
				if(digits[w] != 0){
					digits[0] = digits[w];
					digits[w] = 0;
					break;
				}
			}
		}
		
		out<<"Case #"<<i+1<<": ";
		for(int z=0; z<size; z++){
			out<<digits[z];	
		}
		out<<endl;
	}

}