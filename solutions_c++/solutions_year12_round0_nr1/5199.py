#include <iostream>
#include <cmath>
#include <map>
#include <fstream>
#include <cstring>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
	//char ch1[] = {'a', 'b', 'c', 'd', 'e', 'f' ,'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
	char ch2[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	ifstream cin("C:/Users/Qasim/Downloads/A-small-attempt0.in");
	ofstream cout("C:/Users/Qasim/Downloads/b.txt", ios::out);
	string str; 
	getline(cin, str);
	stringstream ss(str);
	int N;
	ss>>N;
	for (int i = 0; i < N; i++)
	{
		getline(cin, str);
		for (int i = 0; i < str.size(); i++)
		{
			if (str[i] == ' ')
				str[i] = ' ';
			else
				str[i] = ch2[str[i] - 'a'];
		}
		cout<<"Case #"<<(i+1)<<": "<<str<<endl;
	}
	return 1;
}