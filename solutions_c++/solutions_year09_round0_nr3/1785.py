#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

#define L_MAX 501

int check(const char* words, int wBegin, const char* paragraph, int pBegin){
	if(words[wBegin+1] == '\0'){
		int flag = 0;
		while(paragraph[pBegin] != '\0'){
			if( words[wBegin] == paragraph[pBegin])
				flag++;
			pBegin++;
		}
		return flag;
	}

	if(words[wBegin] != paragraph[pBegin]){
		while(paragraph[pBegin] != '\0'){
			if(words[wBegin] == paragraph[pBegin])
				break;
			pBegin++;
		}
	}
	if(paragraph[pBegin] == '\0')
		return 0;
	int pTmpBegin1 = pBegin;
	while( paragraph[pTmpBegin1] != '\0'){
		if(paragraph[pTmpBegin1] == words[wBegin+1])
			break;
		pTmpBegin1++;
	}
	//if(paragraph[pTmpBegin1+1] == '\0')
	//	return 0;

	int pTmpBegin2 = pBegin+1;
	while( paragraph[pTmpBegin2] != '\0'){
		if(paragraph[pTmpBegin2] == words[wBegin])
			break;
		pTmpBegin2++;
	}
	//if(paragraph[pTmpBegin2+1] == '\0')
	//	return 0;

	int num = check( words, wBegin+1, paragraph, pTmpBegin1)
				+ check( words, wBegin, paragraph, pTmpBegin2);
	if(num >= 10000)
		num = num %10000;
	return num;
}

int main(){
	char* words = "welcome to code jam";
	char* paragraph = new char[L_MAX];
	int n;
	ifstream fin("C-small-attempt0.in");
	ofstream fout("output.txt");
	
	fin>>n;
	fin.getline(paragraph, L_MAX);
	for(int i=1;i<=n;i++){
		fin.getline(paragraph, L_MAX);
		fout<<"Case #"<<i<<": ";
		fout<<setfill('0')<<setw(4)
			<<check(words, 0, paragraph, 0)<<endl;
	}
	return 0;
}