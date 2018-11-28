#include <iostream>
#include <set>
#include <fstream>
#include <vector>

using namespace std;



struct letter{

	char let;
	vector<letter> kids;
	
	letter(char l){
		let = l;
	}

	letter* add(char c){
		for(int i=0; i<kids.size(); i++){
			if(kids[i].let == c){	
				return &kids[i];
			}
		}
		kids.push_back(letter(c));
		return &kids[kids.size()-1];
	}
	
	letter* findl(char c){
		for(int i=0; i<kids.size(); i++){
			if(kids[i].let == c){
				return &kids[i];
			}
		}
		return NULL;
	}
	
		
};




int find(string s, letter* cur_level){
//	cout << s << "\n";
	if(s.length() == 0)
		return 1;
	if(s[0] != '('){
		letter* next = cur_level->findl(s[0]);
		if(next != NULL){
			if(s.length() == 1){
				return 1;
			}
	//		cout << "kalder find \n";
			return find(s.substr(1, s.length()-1), next);
		}
//		cout << "Fandt ikke" << s[0] << "\n";
		return 0;
	}
	size_t end = s.find(')');
	string options = s.substr(1,end-1);
//	cout << "Options : " << options << "\n";
	int result = 0;
	for(int i=0; i<options.length(); i++){
		letter* next = cur_level->findl(options[i]);
		if( next != NULL){
//			cout << "kalder find \n";
			result += find(s.substr(end+1, s.length()-end-1), next);
		}
//		cout << "Fandt ikke" << options[i] << "\n";
	}
	return result;
}



int main(int argc, char argv[]){

	
	ifstream input("input.txt");
	int L;
	int D;
	int N;
	input >> L >> D >> N;
//	cout << "L :" << L << "\n";
	string buf;
	getline(input, buf);
	letter uberletter('Ø');
	letter* current = &uberletter;
	for(int i=0; i<D; i++){
		getline(input, buf);
		for(int i=0; i<L; i++){
			current = current->add(buf[i]);
		}
		current = &uberletter;
	}
	uberletter.add('a');
	ofstream output("output.txt");
	for(int i=0; i<N; i++){
		getline(input, buf);
//		cout << buf << "\n";
		int result = find(buf, &uberletter);
		output << "Case #" << i+1 << ": " << result << "\n";
	}
	return 0;



}
