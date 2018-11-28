#include <fstream>
#include <string>
#include <iostream>

using namespace std;

string output_value;
char translate[27] = "yhesocvxduiglbkrztnwjpfmaq";

void run()
{
	int i;
	int t = output_value.size();

	for(i=0;i<t;i++)
	{
		if(output_value[i] >= 'a' && output_value[i] <= 'z')
			output_value[i] = translate[output_value[i] - 'a'];
	}

}

void output(int num, ofstream* out)
{
	*out << "Case #" << num+1 << ": " << output_value << '\n';
}

int main()
{
	int T;
	ifstream in("A-small-attempt1.in");
	ofstream out("output.txt");
	in >> T;
	std::getline(in,output_value);
	for(int i=0;i<T;i++)
	{
		std::getline(in,output_value);
		run();
		output(i, &out);
	}
	in.close();
	out.close();
}