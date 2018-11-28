#include <vector>
#include <stdio.h>
#include <string>
#include <algorithm>

using namespace std;

#define v(c) vector<c>

int main(){
	int testnum = 0;
	FILE* in = fopen("B.in","r");
	FILE* out = fopen("B.out","w");
	fscanf(in, "%d\n", &testnum);
	v(char) vc;

	for(int test = 1; test<=testnum; test++){
		vc.clear();
		char c;
		do{
			c = fgetc(in);
			if(c!='\n'  && c!= EOF){
				vc.push_back(c);
			}
		}while(c != '\n' && c!= EOF);
		bool next = next_permutation(vc.begin(),vc.end());
		if(!next){
			int n = 0;
			while(vc[0]=='0'){
				vc.erase(vc.begin());
				n++;
			}
			for(int k=0; k<=n;++k){
				vc.insert(vc.begin()+1,'0');
			}
		}
		fprintf(out, "Case #%d: ", test);
		for(int i = 0, len = vc.size(); i<len; ++i){
			fprintf(out, "%c", vc[i]);
		}
		fprintf(out, "\n");
	}
	return 0;
}