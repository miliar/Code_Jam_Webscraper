#include<iostream>
#include<fstream>
#include<map>
#include<string>
using namespace std;

int main(){

	ifstream fin("B-large.in", ios::in);
	ofstream fout("b.out",ios::out);

	map<char,map<char, bool>> combinable, oppose;
	map<char,map<char, char>> comresult;

	int T;
	fin>>T;
	int i;
	for (i=0;i<T;i++){
		combinable.clear();
		oppose.clear();
		comresult.clear();
		int C;
		fin>>C;
		int j;
		char ch1,ch2,r;
		for (j=0;j<C;j++){
			fin>>ch1>>ch2>>r;
			combinable[ch1][ch2] = true;
			combinable[ch2][ch1] = true;
			comresult[ch1][ch2] = r;
			comresult[ch2][ch1] = r;
		}
		int D;
		fin>>D;
		for (j=0;j<D;j++){
			fin>>ch1>>ch2;
			oppose[ch1][ch2] = true;
			oppose[ch2][ch1] = true;
		}
		string s="";
		int N, k;
		char ch;
		fin>>N;
		for (k=0;k<N;k++){
			fin>>ch;
			s.push_back(ch);

			int L;
			L = s.length();
			if (L<2)
				continue;
			//test for combine
			if (combinable[s[L-2]][s[L-1]]){
				s[L-2]= comresult[s[L-2]][s[L-1]];
				s.erase(L-1,1);
				continue;
			}
			//test for oppose
			for (j=L-2;j>=0;j--){
				if (oppose[s[L-1]][s[j]]){
					//s.erase(j,L-j);
					s.clear();
					break;
				}
			}
		}
		fout<<"Case #"<<i+1<<": [";
		int L = s.length();
		for (j=0;j<L;j++){
			fout<<s[j];
			if (j<L-1)
				fout<<", ";
		}
		fout<<"]"<<endl;
	}

	fout.close();

	return 0;
}
