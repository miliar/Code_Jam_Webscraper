#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <cmath>

using namespace std;

int countBase(string obj)
{
	int num[10];
	for (int i = 0; i < 10; i++)
		num[i] = 0;
	int al[26];
	for (int i = 0; i < 26; i++)
		al[i] = 0;
	int count = 0;
	for (int i = 0; i < obj.size(); i++) {
		if (obj[i] >= 48 && obj[i] <= 57) {
			if (num[obj[i] - 48] == 0) {
				num[obj[i] - 48] = 1;
				count++;
			}
		}
		if (obj[i] >= 97 && obj[i] <= 122) {
			if (al[obj[i] - 97] == 0) {
				al[obj[i] - 97] = 1;
				count++;
			}
		}
	}
	return count;
}


int main()
{
	ifstream in;
	in.open("A-small-attempt2.in");
    ofstream out;
	out.open("result.txt");
    
	string temp;
	getline(in, temp);

	int cases = atoi(temp.c_str());

	for (int count = 0; count < cases; count++) {
		int index[36] = { 1, 0, 2, 3, 4, 5, 6, 7 ,8 ,9 ,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35};
		string obj;
		getline(in, obj);
		long double base = countBase(obj);
		if (base == 1)
			base = 2;
		//cout << base << endl;
		
		long long result = 0;
		int exist[36];
		for (int i = 0; i < 36; i++)
			exist[i] = -1;
		int j = 0;
		for (int i = 0; i < obj.size(); i++) {
			long double mySize = obj.size() - 1 - i;
			int aaa;
            if (obj[i] >= 48 && obj[i] <= 57) 
				aaa = obj[i] - 48;
			else
				aaa = obj[i] - 97 + 10;
			if (exist[aaa] == -1) {
				exist[aaa] = index[j];
			    result += index[j] * pow(base, mySize);
				j++;
			}
			else
				result += exist[aaa] * pow(base, mySize);
		}

		out << "Case #" << count + 1 << ": " << result << endl;
			 
	}
	in.close();
	out.close();
	return 0;
}
