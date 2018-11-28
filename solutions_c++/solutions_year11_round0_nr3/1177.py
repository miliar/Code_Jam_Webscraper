#include <stdio.h>
#include <vector>
#include <iostream>

using namespace std;
bool hashSolution = false;
int maxValue = 0;

int cal_XOR(vector<int>& candy)
{
	int start = 0; int end = candy.size();
	int ret = 0;
	//start++;
	for(; start < end; start++)
		ret = ret ^ candy[start];

	return ret;
}

void cal_candy(vector<int>& candy) {
	if(cal_XOR(candy) != 0)
		return;

	int minpos = 0; int min = candy[0];
	for(int i = 1; i < candy.size(); i++) {
		if(candy[i] < min) {
			min = candy[i];
			minpos = i;
		}
	}

	hashSolution = true;
	maxValue = 0;
	for(int i = 0; i < candy.size(); i++) {
		if( i != minpos)
			maxValue += candy[i];
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* ifile = fopen("C-small-attempt0.in", "r");
	if(ifile == NULL) {
		printf("open file error!");
		return -1;
	}
	FILE* out = fopen("out", "w");

	int recordNo;
	fscanf(ifile, "%d", &recordNo);
	printf("Record: %d\n", recordNo);

	int i = 1;
	vector<int> candy;
	int candyNo; 
	int value;
	while(i <= recordNo) {
		candy.clear();
		fscanf(ifile, "%d", &candyNo);
		int j = 0;
		while(j < candyNo) {
			fscanf(ifile, "%d", &value);
			candy.push_back(value);
			j++;
		}

		cal_candy(candy);
		
		if(hashSolution) {
			cout<<maxValue<<endl;
			fprintf(out, "Case #%d: %d\n", i, maxValue);
		}else {
			cout<<"NO"<<endl;
			fprintf(out, "Case #%d: NO\n", i);
		}
		hashSolution = false;
		maxValue = 0;
		i++;
	}
	return 0;
}

