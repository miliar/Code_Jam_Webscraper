#include <iostream>
#include <fstream>

using namespace std;

const int lenG (102);

char G[lenG+2];

//if someone reads this and think: "this stupid guy did not realize tha he need just to create an array of [26][1]", my answer is: My dear coding friend, I did just this because it was more bug-free than creating a smaller array.So fuck you!!
char table[26][2] = {{'a','y'}, {'b','h'}, {'c','e'}, {'d','s'}, {'e','o'}, {'f','c'}, {'g','v'}, {'h','x'}, {'i','d'}, {'j','u'}, {'k','i'}, {'l','g'}, {'m','l'}, {'n','b'}, {'o','k'}, {'p','r'}, {'q','z'}, {'r','t'}, {'s','n'}, {'t','w'}, {'u','j'}, {'v','p'}, {'w','f'}, {'x','m'}, {'y', 'a'}, {'z', 'q'}};



int main(){
	int T;
	ifstream fin;
	fin.open("A-small-attempt0.in");
	ofstream fout;
	fout.open("result.txt");
	
	
	fin >> T;
	fin.getline(G, lenG);
	for(int c=1;c<=T;c++){
		fin.getline(G, lenG);
		fout << "Case #" << c << ": ";
		for(int i=0;(G[i]>='a'&&G[i]<='z')||G[i]==' ';i++){
			if(G[i]==' ')
				fout << ' ';
			else
				fout << table[G[i]-'a'][1];
		}
		fout << endl;
	}
	
	fout.close();
	fin.close();
	return 0;
}


