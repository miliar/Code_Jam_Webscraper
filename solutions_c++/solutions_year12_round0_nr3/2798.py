#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<cstdlib>

using namespace std;

int main(){
	int numCases=0, A=0, B=0, num=0, converted=0;
	int arr[7];
	string s, s2, sub1, sub2, con, conBack;
	char letter;
	bool repeat = false;
	ifstream inFile;
	ofstream outFile;
	inFile.open("input.in");
	outFile.open("output.out");
	if(!inFile){
		cerr << "Unable to DIE";
	}
	inFile >> numCases;
	for(int i=0; i<numCases; i++){
		num=0;
		inFile >> A;
		inFile >> B;
		for(int n=A; n<B; n++){
			stringstream out;
			out << n;
			s = out.str();
			for(int q=0; q<7; q++){
				arr[q]=0;
			}
			for(int l=0; l<s.length(); l++){
				repeat = false;
				sub1 = s.substr(0,l+1);
				sub2 = s.substr(l+1, s.length()-l);
				con = sub2 + sub1;
				converted = atoi(con.c_str());
				stringstream out2;
				out2 << converted;
				conBack = out2.str();
				for(int w=0; w<7; w++){
					if(converted == arr[w]){
						repeat = true;
					}
				}
				if(converted > n && converted <= B && con.compare(conBack) == 0 && !repeat){
					//cout << s << " < " << con << "\n";
					//outFile << s << " < " << con << "\n";
					arr[l] = converted;
					num++;
				}
			}
		}
		//cout << "Case #" << (i+1) << ": " << num << "\n";
		outFile << "Case #" << (i+1) << ": " << num << "\n";
	}
				
/*		string s;
		stringstream out;
		stringstream out2;
		inFile >> A;
		inFile >> B;
		out << A;
		s = out.str();
		cout << "A is " << s.length() << " digits long.\n";
		out2 << B;
		s = out2.str();
		cout << "B is " << s.length() << " digits long.\n";
	}*/

	inFile.close();
	outFile.close();
	return 1;
}
