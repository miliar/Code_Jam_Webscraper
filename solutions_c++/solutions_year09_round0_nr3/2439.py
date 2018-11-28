#include <iostream>
#include <string>
#include <iomanip>
#include <fstream>

using namespace std;

int counter;

string Truncate(string str){
	string::iterator it;
	string copy = str;
	for (it = copy.begin(); it < copy.end(); it++){
		char ch = *it;
		switch (ch){
		   case 'w': break;
		   case 'e': break;
		   case 'l': break;
		   case 'c': break;
		   case 'o': break;
		   case 'm': break;
		   case 't': break;
		   case 'd': break;
		   case 'j': break;
		   case 'a': break;
		   case ' ': break;
		   default : copy.erase(it);
		}
	}
	return copy;
}

void Count(string phrase, string src){
	
	if (phrase == "") {
		counter = (++counter)%10000; 
		return;
	}
	if (src.length() < phrase.length()) { return; }
	if (src.length() == 0) { return; }
 	
	int lastfound = -1;
	char firstch = phrase[0];
    
	while (true){
		lastfound = src.find(firstch, lastfound + 1);
		if (lastfound != -1){
			if (lastfound != src.length()-1){			
				if (phrase.length() > 1){
					Count(phrase.substr(1), src.substr(lastfound + 1));
				} else {
					Count("", src.substr(lastfound + 1));
				} 
		   } else {
				if (phrase.length() > 1){
					return;
				} else if (phrase.length() == 1){
					Count("","");
				}
		   }
		} else {
           break;
		}
	}
}

int Solve(string article){
	//string str = Truncate(article);
    counter = 0;
    Count("welcome to code jam", article); 

	return counter;
}

int main(){

	int N;
	
	ifstream file;
	ofstream outfile;
	outfile.open("C-small.out");
	file.open("../C-small-attempt0.in");

	file >> N;

	if (N == 0) return 0;
	string buffer;
    getline(file, buffer);

	int m = 1;
	while (m <= N){		
		string article;
		getline(file, article);
        cout << article << endl;
		outfile << "Case #" << m << ": "; 
		outfile << setfill('0');
		outfile << setw(4) << Solve(article) << endl;
		m++;
	}

	file.close();
	outfile.close();

    string heyhey;
	cin >> heyhey;
	return 0;
}