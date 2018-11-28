#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <list>
#include <map>
#include <set>
using namespace std;

unsigned int nTestCase, testCase;
int i, j, k, l;
char str[23];

void sortAsc(int a, int b){
	for(int i=a; i<b; ++i){
		for(j=a; j<b-(i-a); ++j){
			if(str[j] > str[j+1]){
				char c = str[j];
				str[j] = str[j+1];
				str[j+1] = c;
			}
		}
	}
}

int main(){
	cin >> nTestCase;
	for(testCase=0; testCase<nTestCase; ++testCase){
		scanf("%s", str);
		l = i = strlen(str) - 1;
		while((i>0) && str[i] <= str[i-1]){
			--i;
		}
		if(i>0){
			int min1 = i;
			for(j=i+1; j<=l; ++j){
				if((str[j] > str[i-1]) && (str[j] < str[min1]))
					min1 = j;
			}
			char c = str[min1];
			str[min1] = str[i-1];
			str[i-1] = c;
			sortAsc(i, l);
		} else {
			sortAsc(0, l);
			for(j=l+1; j>0; --j){
				str[j+1] = str[j];
			}
			str[1] = '0';
			j=0;
			while(str[j] == '0')
				++j;
			char c = str[j];
			str[j] = str[0];
			str[0] = c;
		}

		cout << "Case #" << testCase+1 << ": " << str << endl;
	}
	return 0;
}
