#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>

using namespace std;

set<string>  dict;
int l,d,n;

string  pos;
vector<string> word;

string getword(int *idx){
	string str;
	str.resize(l);
	for(int i = 0 ; i < l ; i ++){
		str[i] = word[i][*(idx+i)];
	}
	return str;
}
void increaseIdx(int *idx, int bit, vector<int> &cnt)
{
	if(bit >=l)  return;
	if(*(idx+bit) < cnt[bit]-1){
		*(idx+bit) = *(idx+bit) + 1 ;
	}else{
		*(idx+bit) = 0 ; 
		increaseIdx(idx,++bit,cnt);
	}
}
int eval2(vector<string> & _word){
	int cases = 0 ;
	//cout << "begin word: 0: " << _word[0] << " 1:" << _word[1] << endl ;
	for(set<string>::iterator i=dict.begin() ; i != dict.end() ; i ++){
		string s= *i ; 
		bool got = false;
		for(int j = 0 ; j < l ; j ++){
			string c=s.substr(j,1);
			//cout << "dict:" << s << "--- string c: " << c << endl; 
			if( _word[j].find(c) == string::npos ){
				break;
			}
			if(j == l -1){
				got = true ;
			}
		}
		if(got)  { cases ++ ;  //cout << "\tgot one:" << s << "word[0]:" << _word[0]<<  endl; 
	             }
	}
	return cases; 
}
int eval(vector<string> & _word){
	char w[255];
	vector<int>  cnt;
	int i ; 
	for(i = 0 ; i < _word.size() ; i ++){
		cnt.push_back(_word[i].size());
	}
	unsigned long totalcnt = 1; 
        for( i = 0 ; i < cnt.size() ; i ++){
		totalcnt *= cnt[i];
	}
		
	int *idx = new int[l];
	memset(idx,0,sizeof(int)*l);
	string st;
        int	cases = 0 ;
	for( i = 0 ; i < totalcnt ; i ++){
		st = getword(idx);
		if(dict.find(st) != dict.end()) {
			cases ++ ; 
		}
		increaseIdx(idx,0, cnt);
	}
	delete [] idx;
	return cases;
}

int main(int argc, char** argv)
{
	FILE * fp;
	fp = fopen(argv[1],"r");
	if(fp == NULL) {
		cout << "Can not open the file\n";
	}
	
	char line[2048];
	fgets(line,2048,fp);
	sscanf(line,"%d %d %d", &l,&d,&n);
	//cout << d << endl ;
        for(int i = 0 ; i < d; i ++){
		fgets(line,2048,fp);
		dict.insert(string(line).substr(0,l));	 
		//cout << "add dict: " << string(line).substr(0,l) << endl ; 
	}
	
	int stat=0;
	for(int i = 0 ; i < n ; i ++){
		fgets(line,2048,fp);  //cout << "\nword :" << line << endl;
		int  t = 0 ;
		int widx=0;
		stat = 0 ; 
		while(widx < l){
			
			if(stat == 0 && line[t] != ')' && line[t] != '('  && line[t] != '\n'){
				pos.push_back(line[t]);
				widx ++;
				word.push_back(pos);
				pos.clear();
			}else if(stat == 1){
				if(line[t] != '(' && line[t] != ')'){
					pos.push_back(line[t]);
				}
			}

			if(line[t] == '('){
				stat = 1 ;	
			}else if(line[t] == ')'){
				stat = 0 ; 
				if(pos.size() > 0 ){
					word.push_back(pos);
					pos.clear();
					widx ++ ; 
				}
			}
			t ++ ;
		}
		pos.clear();
		int cases = eval2(word);
		cout << "Case #"<< i + 1<< ": " << cases << "\n";
		word.clear();
	}
	fclose(fp);
}
