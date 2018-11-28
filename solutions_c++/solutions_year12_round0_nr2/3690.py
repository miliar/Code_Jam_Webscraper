#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

void Prob1() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int T,t,i;
	char str[128];

	fin >> T;
	fin.getline(str,128);
	t=1;

	while(T--) {
		fin.getline(str,128);
		
		fout << "Case #" << t++ << ": ";
		for(i=0;i<strlen(str);i++) {
				 if(str[i]=='y') fout << "a";
			else if(str[i]=='n') fout << "b";
			else if(str[i]=='f') fout << "c";
			else if(str[i]=='i') fout << "d";
			else if(str[i]=='c') fout << "e";
			else if(str[i]=='w') fout << "f";
			else if(str[i]=='l') fout << "g";
			else if(str[i]=='b') fout << "h";
			else if(str[i]=='k') fout << "i";
			else if(str[i]=='u') fout << "j";
			else if(str[i]=='o') fout << "k";
			else if(str[i]=='m') fout << "l";
			else if(str[i]=='x') fout << "m";
			else if(str[i]=='s') fout << "n";
			else if(str[i]=='e') fout << "o";
			else if(str[i]=='v') fout << "p";
			else if(str[i]=='z') fout << "q";
			else if(str[i]=='p') fout << "r";
			else if(str[i]=='d') fout << "s";
			else if(str[i]=='r') fout << "t";
			else if(str[i]=='j') fout << "u";
			else if(str[i]=='g') fout << "v";
			else if(str[i]=='t') fout << "w";
			else if(str[i]=='h') fout << "x";
			else if(str[i]=='a') fout << "y";
			else if(str[i]=='q') fout << "z";
			else fout << str[i];
		}
		
		if(T) fout << endl;
	}


	fin.close();
	fout.close();
}

void Prob2() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int T,t=1;
	int N, S, P, tmp, R, p;
	vector<int> point;

	fin >> T;
	while(T--) {
		R=0;
		point.clear();
		fin >> N >> S >> P;
		for(int i=0;i<N;i++) {
			fin >> tmp;
			point.push_back(tmp);
		}

		sort(point.begin(),point.end());
		
		for(int i=N-1;i>=0;i--) {
			p = point.at(i)/3;
			switch(point.at(i)%3) {
			case 0:
				if(p>=P) R++;
				else if(p && p<10 && p==P-1 && S) { R++; S--; }
				break;
			case 1:
				if(p+1>=P) R++;
				break;
			case 2:
				if(p+1>=P) R++;
				else if(p && p<10 && p+1==P-1 && S) { R++; S--; }
				break;
			}
		}
		
		fout << "Case #" << t++ << ": " << R;
		if(T) fout << endl;
	}

	fin.close();
	fout.close();
}


int main()
{
	//Prob1();
	Prob2();
	system("pause");
	return 0;
}