#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <stdio.h>
#include <math.h>
using namespace std;


int main(){
	int n;	
	cin >> n;	
	getchar();
	char c;
	for(int i = 0; i < n; i++){
		c = getchar();
		vector <int> last;
		while(((int)c - (int)'0' >= 0)&&((int)c - (int)'0' < 10)){
			last.push_back((int)c - (int)'0');
			c = getchar();
		}
		for (int z = 0; z <= (last.size() - 1) / 2; z++)
			swap(last[z], last[last.size() - 1 - z]);
		bool sorted = true;
		for(int j = 0; j < last.size() - 1; j++){
			if (last[j] > last[j + 1]){
				int min = last[j];
				int minposit = j;
				for(int k = 0; k < j; k++)
					if((last[k] > last[j + 1]) && (last[k] < min)){
						min = last[k];
						minposit = k;
					}
				swap(last[j + 1], last[minposit]);
				for(int k = 0; k < j; k++)
					for(int l = 0; l < j; l++)
						if(last[l] < last[l + 1])
							swap(last[l], last[l + 1]);
				cout << "Case #" << i + 1 << ": ";
				for(int k = last.size() - 1; k >= 0; k--)
					cout << last[k];
				cout << endl;
				sorted = false;
				break;
			}
		}
		if(sorted){
				cout << "Case #" << i + 1 << ": ";
				
				for (int m = 0; m < last.size(); m++)
					if (last[m] > 0){
					cout << last[m] << "0";
					for(int k = 0; k < m; k++)
						cout << "0";					
					for(int k = m + 1; k < last.size(); k++)
						cout << last[k];
					cout << endl;
					break;
				}
				
							
		}
		

	}
}