#include<iostream>
#include<fstream>
#include<string>

using namespace std;

char array[100];
char check[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(){
	ifstream input;
	ofstream output;
	input.open("A-small-attempt3.in");
	output.open("A-small-attempt3.out");
	int n;
	input>>n;
	int num = 0;
	char ch;
	input.get(ch);
	while (n--){
		int i=0;
		while (true){
			input.get(array[i]);
			if (array[i] == '\n') break;
			if (array[i]  != ' ')
				array[i] = check[array[i]-'a'];
			++i;
		}
		output<<"Case #"<<++num<<": ";
		for (int s=0;s<i;++s)
			output<<array[s];
		if (n != 0) output<<endl;
	}
	input.close();
	output.close();
	return 0;
}