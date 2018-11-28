#include<string>
#include<iostream>
#include<fstream>

using namespace std;

int main(void)
{
	ifstream input_data;
	input_data.open("A-small-attempt4.in");

	ofstream output_data;
	output_data.open("output.txt");
	
	int T;
	int length;
	char current;
	string G;
	string table = "yhesocvxduiglbkrztnwjpfmaq";
	input_data >> T;

	getline(input_data,G);

	for(int i=0; i < T; i++) {

		getline(input_data, G);
		length = G.length();
		output_data << "Case #" << i+1 << ": ";

		for(int j=0; j < length; j++) {
			current = G[j];

			if(current == ' ') {
				output_data << " ";
			}
			else {
				output_data << table[current - 'a'];
			}
		}

		if(i != T-1) {
			output_data << endl;
		}
	}
}

