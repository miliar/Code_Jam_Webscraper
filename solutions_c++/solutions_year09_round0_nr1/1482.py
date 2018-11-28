#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <list>
#include <map>
#include <set>
using namespace std;

unsigned int WordSize, DictSize, PatSize;
typedef int Mask[15];

Mask wordMasks[5000];
Mask regMask;
int n;
int alphabet[] = {1, 2, 4, 8, 0x10, 0x20, 0x40, 0x80, 
					0x100, 0x200, 0x400, 0x800, 
					0x1000, 0x2000, 0x4000, 0x8000, 
					0x10000, 0x20000, 0x40000, 0x80000, 
					0x100000, 0x200000, 0x400000, 0x800000, 
					0x1000000, 0x2000000 };

void prepareWordMask(string word, Mask *mask1){
	int i;
	int *iter = (int *) mask1;
	for(i=0; i<WordSize; ++i){
		*iter = alphabet[word[i]-'a'];
		++iter;
	}
}

void prepareRegMask(string word, Mask *mask1){
	int i, j;
	int *iter = (int *) mask1;
	for(i=0, j=0; i<WordSize; ++i, ++j){//j is index of regex input char
		if(word[j] != '('){
			*iter = alphabet[word[j]-'a'];
		}else{
			*iter = 0;
			++j;
			while(word[j] != ')'){
				*iter |= alphabet[word[j]-'a'];
				++j;
			}
			//++j;//for ')'
		}
		++iter;
	}
}

int count(Mask reg, Mask *word){
	int i, j, count1=0;
	int *riter, *witer;
	riter = (int*)reg;
	for(i=0; i<DictSize; ++i){
		witer = (int*)word[i];
		bool flag=true;
		for(j=0; (j<WordSize) && flag; ++j){
			if(!(riter[j] & witer[j]))
				flag = false;
		}
		if(flag)
			++count1;
	}
	return count1;
}

int main(){
	int i, j;
	cin >> WordSize;
	cin >> DictSize;
	cin >> PatSize;

	string word;
	for(i=0; i<DictSize; ++i){
		cin >> word;
		prepareWordMask(word, wordMasks+i);
	}
	for(i=0; i<PatSize; ++i){
		cin >> word;
		prepareRegMask(word, &regMask);
		n = 0;
		n = count(regMask, wordMasks);
		cout << "Case #" << i+1 << ": " << n << endl;
	}
	return 0;
}
