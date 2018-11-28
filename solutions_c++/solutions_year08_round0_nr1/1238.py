
#include<iostream>
#include<fstream>
#include<string>
#include<map>
#include<memory>
using namespace std;

int n, s, q, runlength[100];
string searchEngine[100], query[1000];
map<string, int> table;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

int Run(int start);

int main()
{
	int i = 0, j, k, ans;
	char tempS[101];
	
	fin>>n;
	while(i < n)
	{
		i++;

		fin>>s; fin.get();
		for(j = 0; j < s; ++ j){
			k = 0;
			while((tempS[k] = (char)fin.get()) != '\n') k ++;
			tempS[k] = '\0';
			searchEngine[j] = tempS;
			table[searchEngine[j]] = j;
		}
	/*	for(j = 0; j < s; ++ j)
			cout<<searchEngine[j]<<endl;*/

		fin>>q; fin.get();
		for(j = 0; j < q; ++ j){
			k = 0;
			tempS[k] = (char)fin.get();
			while(tempS[k] != '\n' && !fin.eof()){
				k ++;
				tempS[k] = (char)fin.get();
			}
			tempS[k] = '\0';
			query[j] = tempS;
		}
/*		for(j = 0; j < q; ++ j)
			cout<<query[j]<<endl;*/

		memset(runlength, 0, s*sizeof(int));
		ans  = 0; k = Run(0);
		while(k < q) {
			memset(runlength, 0, s*sizeof(int));
			k = Run(k);
			ans ++;
		}
		fout<<"Case #"<<i<<": "<<ans<<endl;	
	}
	return 0;
}

int Run(int start)
{
	int num = s, index;
	for(int i = start; i < q; ++ i){
		index = table[query[i]];
		if(runlength[index] == 0){
			runlength[index] = i+1;
			num --;
			if(num == 0) return i;
		}
	}
	return q;
}
