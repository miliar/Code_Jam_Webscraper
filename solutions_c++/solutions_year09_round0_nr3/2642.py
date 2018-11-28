#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

char target[19] = {'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m'};
string inputStr;
int countResult;
void checkString(int pt,int chIdx){
	if(chIdx == 19){
		countResult++;
		if(countResult == 10000) countResult = 0;
		return ;
	}
	vector<int> idx;
	for(int i = pt;i < (int)inputStr.size() ; i++){
		if(target[chIdx] == inputStr.at(i)) idx.push_back(i);
	}
	if(idx.size() == 0) return ;
	for(int i = 0 ; i < (int)idx.size() ; i++){
		checkString(idx[i],chIdx+1);
	}
}

int main(){

	FILE *fin = fopen("C-small-attempt0.in","r");
	FILE *fout = fopen("C-small-attempt0.out","w");
	
	
	int tc;
	fscanf(fin,"%d",&tc);

	char getCh[500];
	fgets(getCh,500,fin);
	for(int caseCnt = 1; caseCnt <= (int)tc ; caseCnt++){
		countResult = 0;
		memset(getCh,0,sizeof(getCh));	
		fgets(getCh,500,fin);
		inputStr = getCh;

		checkString(0,0);
		
		fprintf(fout,"Case #%d: %04d\n",caseCnt,countResult);
	}

	fclose(fin);
	fclose(fout);
	return 0;
}