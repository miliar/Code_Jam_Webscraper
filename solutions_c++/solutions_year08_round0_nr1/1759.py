#include <cstdlib>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	FILE *in  = fopen("A-small-attempt1.in","r");
	FILE *out = fopen("A-small-attempt1.out","w");
	int tests;
	fscanf(in,"%d",&tests);
	for(int t = 0; t<tests; t++){
		int ret = 0;
		map<string,int> numEng;
		vector<int> cantAp(1001,0);
		int S;
		fscanf(in,"%d",&S);
		vector<string> se;
		fscanf(in,"\n");
		for(int i = 0; i<S; i++){
			int j = 0;
			string name="";
			char ast[1000];
			while(1){		
				char tmp;
				fscanf(in,"%c",&tmp);
				if(tmp == '\n') break;
				name += tmp;
			}
			se.push_back(name);
			numEng[name] = i;
		}

		int Q;
		vector<int> qs;
		fscanf(in,"%d",&Q);
		vector<string> queries;
		fscanf(in,"\n");
		for(int i = 0; i<Q; i++){
			string querie="";
			int j = 0;
			char tmp;
			while(fscanf(in,"%c",&tmp) != EOF){
				if(tmp == '\n') break;
				querie += tmp;
			}
			queries.push_back(querie);
			qs.push_back(numEng[querie]);
		}
		
		//el que mas abajo aparece, o el q no aparece
		vector<bool> aparecio(S+2,false);
		int todos = 1;
		if(qs.size() > 0) aparecio[qs[0]] = true;
		for(int i = 1; i<Q; i++){
			if(!aparecio[qs[i]]){
				aparecio[qs[i]] = true;
				todos++;
			}
			if(todos == S){
				ret++;
				for(int j = 0; j<S; j++) aparecio[j] = false;
				aparecio[qs[i]] = true;
				todos = 1;
			}
		}
		fprintf(out,"Case #%d: %d\n",t+1,ret);
		fscanf(in,"\n");
	}
    return EXIT_SUCCESS;
}
