#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

void first_cal(string str, vector<string> &words, vector<string>& ac);
void second_cal(ofstream &out, int n, int l, vector<string> &words, vector<string>& ac);

int main(){

    int L, D, N;
	vector<string> words;
	vector<string> ac;
	ofstream out("A_output.out");
	string tstr;

	ifstream in("A-large.in");		

	in>>L>>D>>N;
	

	for(int i=0; i<D;i++){
		in>>tstr;
		words.push_back(tstr);
	}

	for(int j=0; j<N;j++){
		in>>tstr;
		first_cal(tstr, words, ac);
		second_cal(out, j, L, words, ac);
	}

	return 0;
}

void first_cal(string str, vector<string> &words, vector<string>& ac){
	
	string nstr("");

	for(int i=0; i<str.length();i++){
		if(str.at(i)=='('){
			
			nstr="";	
			
			while(str.at(++i)!=')'){
				nstr+=str.at(i);
			}
			
			ac.push_back(nstr);

			nstr="";
	
			
		}
		else if(str.at(i)!='(' ){

				nstr=str.at(i);
				ac.push_back(nstr);
			
		}
	}


}

void second_cal(ofstream &out,int n, int l, vector<string> &words, vector<string>& ac){

    
	int num=0;
	int temp=0;

	for(int k=0; k<words.size(); k++){
		for(int i=0;i<l;i++){
			for(int j=0;j<ac[i].length();j++){
						
			
				if(ac[i].at(j)==words[k].at(i)){
					temp++;
					break;
				}

				
			}
		
		}
     
		if(temp>=l)
			num++;


		
		temp=0;
		
	}

	n++;
	out<<"Case #"<<n<<": "<<num<<endl;
	ac.clear();

}