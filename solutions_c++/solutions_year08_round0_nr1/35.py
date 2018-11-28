#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

map<string,int> pos;

char tmp[120];

int main(){
	int i,casos,c,s,q;
	
	fgets(tmp,120,stdin);
	sscanf(tmp,"%d",&casos);
	for (c=1;c<=casos;c++){
		pos.clear();
		fgets(tmp,120,stdin);
		sscanf(tmp,"%d",&s);
		for (i=0;i<s;i++){
			fgets(tmp,120,stdin);
			pos[(string)tmp]=i;
		}
		set<int> tengo;
		int rta=0;
		fgets(tmp,120,stdin);
		sscanf(tmp,"%d",&q);
		for (i=0;i<q;i++){
			fgets(tmp,120,stdin);
			tengo.insert(pos[(string)tmp]);
			if ((int)tengo.size()==s){
				tengo.clear();
				tengo.insert(pos[(string)tmp]);
				rta++;
			}
		}
		printf("Case #%d: %d\n",c,rta);
	}
	
	return 0;
}
