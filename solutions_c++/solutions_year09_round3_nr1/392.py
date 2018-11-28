#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <deque>
#include <map>

using namespace std;

FILE* in = fopen("A.in","r");
FILE* out = fopen("A.out","w");

int main(){
	int testnum = 0;
	
	fscanf(in,"%d", &testnum);

	for(int test = 1; test <= testnum; ++test){
		long long Answer = 0;
		
		char buff[100];
		fscanf(in,"%s\n", &buff);
		string n = buff;
		int alfa[256];
		for(int i=0;i< 256; ++i){
			alfa[i] = -1;
		}
		int base = 2;
		if(n.size() == 1){
			Answer = 1;
		}else if (n.size() >= 2){
			int c = 1;
			alfa[n[0]] = 1;
			while(alfa[n[c]] != -1 && c<n.size()){
				c++;
			}
			if(c<n.size())
			{
				alfa[n[c]] = 0;
				c++;
			}
			for(; c< n.size(); ++c){
				if(alfa[n[c]] == -1){
					alfa[n[c]] = base;
					base++;
				}
			}
			Answer = alfa[n[0]];
			for(int c = 1; c < n.size(); ++c){
				Answer = Answer*base + alfa[n[c]];
			}
		}
		fprintf(out,"Case #%d: %lld\n", test, Answer);
	}
	fprintf(out, "\n");
	return 0;
}