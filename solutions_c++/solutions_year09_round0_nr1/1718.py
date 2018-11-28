/**************************************************
*        Code Jam - Qualification Round 2009 
*				Alien Language
**************************************************/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define L_MAX 16
#define D_MAX 5000
#define N_MAX 500

int check(const char* word, const char* signal){
	int wlen = strlen(word);
	int slen = strlen(signal);
	int i=0;
	int j=0;
	int max = 0;		//最大匹配数，不匹配的起始位置
	while(i < wlen && j < slen){
		bool flag = false;
		if( signal[j] == '(' ){
			while(signal[j] != ')' ){
				if(word[i] == signal[j]){
					flag = true;			
				}
				j++;
			}
		}else{
			if( word[i] == signal[j] )
				flag = true;
		}
		if(flag){
			i++;
			j++;			//here signal[j] should be ')' or current char
			max++;			//max指向下个匹配位次
		}
		else
			return max;
	}
	return -1;			//完全匹配
}

int solve(const string signal, const vector<string>& dictionary){
	int sum = 0;
	int nflag = 0;
	vector<string>::const_iterator iter = dictionary.begin();
	while(iter != dictionary.end() ){
		nflag = check(iter->c_str(), signal.c_str());
		if(nflag == -1){
			sum++;
			iter++;
		}
		else{
			string c = iter->substr(0, nflag+1);
			while(iter != dictionary.end() && c == iter->substr(0, nflag+1) )
				++iter;
		}
	}
	return sum;
}
	
int main(){
	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	int L, D, N;
	vector<string> dictionary;

	fin>>L>>D>>N;
	for(int i=0;i<D;i++){
		string temp;
		fin>>temp;
		dictionary.push_back(temp);
	}
	stable_sort(dictionary.begin(), dictionary.end());

	for(int i=0;i<N;i++){
		string temp;
		fin>>temp;
		fout<<"Case #"<<i+1<<": ";
		fout<<solve(temp, dictionary)<<endl;
	}

	//for(int i=0;i<N;i++){
	//	string temp;
	//	cin>>temp;
	//	check(temp, dictionary);
	//}
	//for(vector<string>::iterator iter = dictionary.begin();
	//	iter != dictionary.end(); ++iter)
	//	cout<<*iter<<endl;
	return 0;
}