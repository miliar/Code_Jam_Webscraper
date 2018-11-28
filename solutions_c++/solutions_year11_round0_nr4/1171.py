#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

struct Num {
	int v;
	int pos;
};

using namespace std;

bool NumCompare(const Num& a, const Num& b)
{
	return a.v < b.v;
}

int process_sort(vector<Num>& numList) {
	sort(numList.begin(),numList.end(), NumCompare);	
	int ans = 0;	
	for(int i = 0; i < numList.size(); i++){		
		if(numList[i].pos != i)			
			ans++;	
	}

	return ans;
}


int main(int argc, char* argv[])
{
	FILE* ifile = fopen("D-small-attempt0.in", "r");
	if(ifile == NULL) {
		printf("open file error!");
		return -1;
	}
	FILE* out = fopen("out", "w");

	int recordNo;
	fscanf(ifile, "%d", &recordNo);
	printf("Record: %d\n", recordNo);

	int i = 1;
	int num;
	int tmp;
	vector<Num> numList;
	Num tmpNum;

	while(i <= recordNo) {
		numList.clear();
		fscanf(ifile, "%d", &num);
		int j = 0;
		while( j < num) {
			fscanf(ifile, "%d", &tmp);
			tmpNum.pos = j;
			tmpNum.v = tmp;
			numList.push_back(tmpNum);

			j++;
		}

		float times = process_sort(numList);
		fprintf(out, "Case #%d: %.6f\n", i, times);

		i++;
	}
	return 0;
}

