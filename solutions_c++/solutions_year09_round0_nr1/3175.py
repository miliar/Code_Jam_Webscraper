#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;


struct tokens{

	char *ret;
	
};
struct words{

	char ret1[11];
	
};
int counter;

void process(int L, string word, int cases, vector<string> rr){

	tokens tp;
	int fund;
	int ctr = 0;
    
   for(int i=0; i < L; i++){
   
		fund = rr[i].find(word[i]);
		if (fund!=string::npos) ctr++;

	}

    if (ctr == L) counter += 1;
	return ;
	
}
void Tokenize(const string& str,
                      vector<string>& tokens,
                      const string& delimiters = "( ) ")
{
    // Skip delimiters at beginning.
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
	
	if (!lastPos){
	
		string temp ="";
		//cout << "stp -- > " << str.length() << endl;
		for(int i=0; i < str.length(); i++){
		
			temp += str[i];
			tokens.push_back(temp);
			
		}
	}
	else
	{
    // Find first "non-delimiter".
		string::size_type pos     = str.find_first_of(delimiters, lastPos);

		while (string::npos != pos || string::npos != lastPos)
		{
			// Found a token, add it to the vector.
			tokens.push_back(str.substr(lastPos, pos - lastPos));
			// Skip delimiters.  Note the "not_of"
			lastPos = str.find_first_not_of(delimiters, pos);
			// Find next "non-delimiter"
			pos = str.find_first_of(delimiters, lastPos);
		}
		
	}
}

int main(){

    
	vector<tokens> rr;
	 vector<words> word;
	 vector<string> norm;
     char str[] = "(ab)b(bc)d(ca)";
	 char pattern[500];
	 int L, D, N;
	 scanf("%d %d %d", &L, &D, &N);
	 for(int i=0; i < D; i++){
	 
		words ww;
		string temp;
		cin >> temp;
		//scanf("%s", &ww.ret1);
		
		//word.push_back(ww);
		norm.push_back(temp);
	}
	vector<string> ttp;
	vector<string> bb;
	string bb1[L];
	for(int cases = 0; cases < N; cases++){
	
		//scanf("%s", &pattern);
		//string dead = "";
		string dead;
		char temp;
		
		//while(cin >> temp)) dead += temp;
		cin >> dead;
		
		//stringstream ss1(dead);
		
		vector<string> tab;
		int m = 0;
		int mmm = 0;
		while( m != dead.size() )
		{
			//m++;
			string str1 = "";
			string str2 = "";
			if(dead[mmm] == '('){
			
				//mmm++;
				while( dead[mmm++] != ')'){
						
						
						str1 += dead[mmm];
						//m++;
						
				}
				
				tab.push_back(str1);
				str1 = "";
				m = mmm;
				
			}
			
			else if( dead[mmm] != '('){
			
				str2 += dead[mmm++];
				tab.push_back(str2);
				str2 = "";
				m = mmm;
			}
			
			if(mmm == dead.size() ) break;
			//m = mmm;
			
		}
		//cout << "tab-size " << tab.size() << endl;
		
		//for(int b=0; b < tab.size(); b++)
		{
			//cout << tab[b] << endl;
		}
		
		//cout << "dead --> " << dead << endl;
		counter = 0;
	 
		
		char delims[] = "( ) ";
		char *result = NULL;
	    
		tokens rp;
		result = strtok( pattern, delims );
		int ctr = 0;
		while( result != NULL ) {
			//printf( "result is \"%s\"\n", result );
			result = strtok( NULL, delims );
		 
		    rp.ret = result;
			//string str = result;
			//static_cast<std::string>(result);
			rr.push_back(rp);
			
			
		
		}
	
		//vector<string> tell;
        //string stp("(ab)(bc)(ca)");
		
		//Tokenize(dead, tell);
		
		//Tokenize(dead, tell);
		//cout << " blah " << endl;
        //cout << " ---> " << tell.size() << endl;
		//cout << L << " " << D << " " << N << endl;
		for(int p=0; p < D; p++){
		
				process(L, norm[p], cases, tab);
			
		}
		//cout << " is it here " << endl;
		cout << "Case #" << cases+1 << ": "<< counter << endl;
		
		//tell.clear();
		
	}
	
	
	 
	 
	 return 0;
	 
}
