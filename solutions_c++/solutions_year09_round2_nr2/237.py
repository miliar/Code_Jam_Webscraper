#include <stdio.h>
#include <assert.h>
#include <string>
#include <algorithm>

using namespace std;

char s[10000];

int main(){
	int nTC;
	scanf("%d",&nTC);
	for (int TC=1; TC<=nTC; TC++){
		scanf("%s",s);
		string x = s;

		bool desc = true;
		for (int i=0; i+1<x.size(); i++)
			if (x[i] < x[i+1]) desc = false;
		
		if (desc){
			sort(x.begin(),x.end());
			int minIdx = 0;
			for (int i=1; i<x.size(); i++)
				if (x[minIdx]=='0' || (x[i]!='0' && x[i] < x[minIdx]))
					minIdx = i;
			assert(x[minIdx]!=0);
			x = x.substr(minIdx,1) + "0" + x.substr(0,minIdx) + x.substr(minIdx+1);
		} else {
			next_permutation(x.begin(),x.end());
		}
		printf("Case #%d: %s\n",TC,x.c_str());
	}
}
