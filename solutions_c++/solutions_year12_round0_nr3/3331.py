#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace std;

#define SIZE 4

int main(void) {
	int testCases, A, B, answer, temp, k_num, a_num, b_num, tempSort, count, partialAnswer, tempInt ;
	int split[SIZE]; 
	int splitA[SIZE]; 
	int splitB[SIZE];
	bool check[1001] ={0};
	char tempChar;
	FILE *infile= fopen("input", "r+");
	fscanf(infile, "%d",&testCases);
	fscanf(infile, "%c", &tempChar);
	for(int i=1; i<=testCases; ++i) {
		answer = 0;
		for(int l=1; l<1002; ++l) {
			check[l] = false;
		}
		printf("Case #%d: ",i);
		fscanf(infile, "%d%d", &A, &B);
		fscanf(infile, "%c", &tempChar);
		for(int j=A; j<B; ++j) {
			//split j into digits.
		//	cout<<"new number: "<<j<<endl;
			temp = j;
			k_num=SIZE-1;
			for(; temp!=0; --k_num) {
				split[k_num] = temp%10;
				temp/=10;
			}
			++k_num;
			int n=0;
			for(; k_num<SIZE; ++k_num, ++n) {
				split[n] = split[k_num];
				splitA[n] = split[k_num];
			}
			k_num = n;
			for(int l=0; l<k_num; ++l) {
				tempInt = splitA[l];
				for(int m=k_num; m>1; --m) {
					splitA[(l+m)%k_num] = splitA[(l+m-1)%k_num];
				}
				splitA[(l+1)%k_num] = tempInt;
		
				if(splitA[0] == 0) {
					;
				} else {
					tempInt = 0;
					for(int z=0; z<k_num; ++z) {
						tempInt = splitA[z] + tempInt*10;
					}
				//	cout<<"tempInt is: "<<tempInt<<endl;
					if(tempInt<=B && tempInt>j) {
						++answer;
			//			cout<<">>answer Calulated"<<endl;
					}
				}
			}
		}
	printf("%d\n", answer);
	}
	return 0;
}

