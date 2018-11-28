#include <stdio.h>
#include <string.h>
#include "stdlib.h"
#include "unistd.h"
#include "math.h"
#include <string>
#include <sys/types.h>
#include <vector>
#include <map>
#include <list>
#include <deque>
#include <set>
using namespace std;

char mat[26][26];
char neg[26][26];

vector<unsigned char> vec;

bool match(){
	int size = vec.size();
	if(size==1){
		return false;
	}
	char res = mat[vec[size-1]][vec[size-2]];
	if(res!='0'){
		vec.pop_back();
		vec.pop_back();
		vec.push_back(res);
		return true;
	} else {
		return false;
	}
}

bool clear(){
	int size = vec.size();
	if(size==1){
		return false;
	}
	for(int it=0;it<size-1;++it){
		if(neg[vec[it]][vec[size-1]]=='1'){
			vec.clear();
			return true;
		}
	}
	return false;
}

int main(int argc, char *argv[]) {
//input
	int T;
	vec.reserve(110);
	scanf("%d\n", &T);
	for (int i=0;i<T;++i)
	{
		memset(mat,'0',26*26);
		memset(neg,'0',26*26);
		vec.clear();
		int C;
		scanf("%d", &C);
		for(int ci=0;ci<C;++ci){
			char ch1;
			char ch2;
			char ch3;
			scanf(" %c%c%c", &ch1,&ch2,&ch3);
			mat[ch1-65][ch2-65]=ch3-65;
			mat[ch2-65][ch1-65]=ch3-65;
		}
		int D;
		scanf(" %d", &D);
		for(int di=0;di<D;++di){
			char ch1;
			char ch2;
			scanf(" %c%c", &ch1,&ch2);
			neg[ch1-65][ch2-65]='1';
			neg[ch2-65][ch1-65]='1';
		}
		int N;
		scanf(" %d ", &N);
		for(int ni=0;ni<N;++ni){
			char ch;
			scanf("%c", &ch);
			vec.push_back(ch-65);
			while(match()) {}
			clear();
		}
		printf("Case #%i: [", i+1);
		bool first=true;
		for(int vi=0;vi<vec.size();++vi){
			if(first){
				printf("%c", vec[vi]+65);
				first = false;
			} else {
				printf(", %c", vec[vi]+65);
			}
		}
		printf("]\n");
	}
}







