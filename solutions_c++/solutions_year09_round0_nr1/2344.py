#include <vector>
#include <stdio.h>
#include <string>

using namespace std;

#define vs vector<string>
int main(){
	int testnum = 0;
	FILE* in = fopen("A.in","r");
	FILE* out = fopen("A.out","w");
	int Answer, L, D;
	fscanf(in, "%d %d %d\n", &L, &D, &testnum);
	int i;
	vs dic;
	for(i=0; i<D; ++i){
		char c[100];
		
		fgets(c,100,in);
		string s(c);
		dic.push_back(s);
	}
	vs word;
	for(int test = 1; test<=testnum; test++){
		Answer = 0;
		word.clear();
		int braket=0;
		for(i=0; i<L; ++i){
			string curchar = "";
			do{
			char c = fgetc(in);
			if(c == '('){
				braket++;
			}else if(c == ')'){
				braket--;
			}else {curchar += c;}
			}while(braket>0);	
			word.push_back(curchar);
		}
		fscanf(in, "\n");
		for(int i = 0, len = dic.size(); i < len; ++i){
			bool f = true;

			for(int ch = 0; ch< L; ++ch){
				if(word[ch].find(dic[i][ch]) == string::npos ){
					f = false;
				}
			}
			if(f)Answer++;
		}
		
		fprintf(out, "Case #%d: %d\n", test, Answer);
	}
	return 0;
}