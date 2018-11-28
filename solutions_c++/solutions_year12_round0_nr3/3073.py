#include <stdio.h>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <iostream>
#include <math.h>
#include <sstream>
using namespace std;

string convertInt(long number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

long convertString(string st) 
{
	long result;
	stringstream(st) >> result;
	return result;
}

int main() {	
	int T = 0;
	scanf("%d\n",&T);
	for (int i=0; i<T; i++) {
		long A = 0;
		long B = 0;
		long temp[10];
		int pos = 0;

		scanf("%ld",&A);
		scanf("%ld\n",&B);

		long counter = 0;

		for (long j=A; j<=B; j++) {
			string tempValue = convertInt(j);
			if (tempValue.length() > 1) {
				pos = 0;
				for (int k=1; k<tempValue.length();k++) {
					string tempFlip = tempValue.substr(tempValue.length()-k,k) + tempValue.substr(0,tempValue.length()-k);
					if ((tempFlip[0] != '0') && (tempFlip[0] >= tempValue[0]) && tempFlip != tempValue) {
						long tempFlipValue = convertString(tempFlip);
						if ((tempFlipValue >= A) && (tempFlipValue <= B) && (tempFlipValue > j)) {
							bool nemu = false;
							for (int l=0; l<pos; l++) {
								if (temp[l] == tempFlipValue) {
									nemu = true;
								}
							}
							if (!nemu) {
								temp[pos] = tempFlipValue;
								pos++;
								counter++;
							}
						}
					}
				}
			}
		}

		//counter /= 2;

		printf("Case #%d: %ld",i+1,counter);
		//cout << strR;
		printf("\n");
	}
	//while (scanf("%d %d %d\n",&d1,&d2,&d3) != EOF) {
		//jawaban
		//printf("Case #%d: %d\n",d1,d2);
	//}
	//getch(); 
	return 0;
}