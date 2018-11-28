#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<fstream>

using namespace std;
int function(string test , vector<string> );
//void recursion(string str ,vector<string> parsed, int state , int &count , map<string,bool> flags);
int func2(vector< map<char,bool> >  , vector<string>  );
int main(){
	ifstream ifile("A-large.in");
	ofstream ofile("A-large.out");
	int l,d,n;
	//cin>>l>>d>>n;
	ifile>>l>>d>>n;
	vector<string> vec;
	
	while(d--){
		string s;
		//cin>>s;
		ifile>>s;
		vec.push_back(s);
	}
	int i = 1;
	cout<<"Writting start: ";
	while(n--){
		string test;
		//cin>>test;
		ifile>>test;
		//cout<<"Case #"<< i++ <<": "<<function(test , vec , flags)<<"\n";
		ofile<<"Case #"<< i++ <<": "<<function(test , vec )<<"\n";
	}
}

int function(string test , vector<string> vec ){
	
	vector<string> parsed;
	vector<map<char, bool> > vecMap;

	for(int i = 0 ; i < test.length(); i++){
		if(test[i] == '('){
			map<char , bool> temp;
			string s;
			while(test[i]!=')'){
				if(test[i] != '(' && test[i] != ')'){
					char ch = test[i];
					s+= ch;
					temp[ ch ] = true;
				}
				i++;
			}
			parsed.push_back(s);
			vecMap.push_back(temp);
		}
		else{
			map<char , bool> temp;
			string s;
			s+= test[i];
			temp[ test[i] ] = true;
			parsed.push_back(s);
			vecMap.push_back(temp);
		}
	}
	
	//recursion("" , parsed , 0 , count , flags);
	return func2( vecMap , vec );
	
}

/*void recursion(string str ,vector<string> parsed, int state , int &count , map<string,bool> flags){
	if(state >= parsed.size()){
		if( flags[ str ] ) count+=1;
		return;
	}
	for(int i = 0 ; i < parsed[state].length() ; i++){
		str += parsed[state][i];
		recursion(str , parsed , state+1 , count , flags);
		str.erase(str.length()-1,1);
	}
}*/

int func2(vector< map<char,bool> > vecMap , vector<string> words ){
	int count = 0;
	for(int i = 0 ; i < words.size() ; i++){
		int f = 1;
		for(int j = 0 ; j < words[i].length() ; j++){
			if( vecMap[j][ words[i][j] ] == false){
				f = 0;
				break;
			}
		}
		if(f) count+=1;
	}
	return count;
}