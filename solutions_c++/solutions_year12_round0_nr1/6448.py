#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main() {
	
	char arr[26];
	int n, m;
	
	
	arr['e'-97] = 'o';
	arr['q'-97] = 'z';
	arr['y'-97] = 'a';arr['z'-97] = 'q';
	ifstream fin("input.txt");
	
	string s1, s2;
	while (getline(fin,s1))
	{    
 		getline(fin,s2);
 		//cout << s1 << endl << s2 << endl;
		n = s1.length(); 
		for (int i = 0; i < n; i++) {
		    if (s1[i] == ' ') continue;
			arr[s1[i]-97] = s2[i];
		}
	}		    	 
	ifstream fin1("A-small-attempt1.in");
	ofstream fout("output.out");
	fin1 >> m;
	getline(fin1,s1);
	for (int j = 0; j < m; j++)
	{
	 	getline(fin1,s1); 
	 	//cout << s1 << endl;
 	    n = s1.length();
 	    for (int i = 0; i < n; i++) {
			if (s1[i] == ' ') continue;
			s1[i] = arr[s1[i]-97];
		}
		fout << "Case #" << j+1 << ": " << s1 << endl;
	}
	
	system("pause");
	
	return 0;
}	
	
