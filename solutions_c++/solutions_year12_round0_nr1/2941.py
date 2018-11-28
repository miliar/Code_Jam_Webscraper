#include <iostream>
#include <string>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;


void translate(const string &input, string &output)
{
	string language_key = "ynficwlbkuomxsevzpdrjgthaq";
	int position;

	output.clear();
	for(int iter = 0; iter < input.size();iter++)
	{
		if(input[iter] == ' ')
			output.push_back(input[iter]);
		else
		{
			position = language_key.find(input[iter]);
			output.push_back('a' + position);
		}
	}
}

int main()
{
	int T; // Total number of inputs
	vector<string> inputList;
	vector<string> outputList;
	string current,result;

	int iter;

	cin>>T;
	cin.ignore();
	for(iter=0;iter<T;iter++)
	{
		//cin.getline(current);
		getline(cin, current);
		inputList.push_back(current);
	}

	for(iter=0;iter<T;iter++)
	{
		current = inputList[iter];
		translate(current, result);
		outputList.push_back(result);
	}



	for(iter=0;iter<T;iter++)
	{
		cout<<"Case #"<<(iter+1)<<": "<<outputList.at(iter)<<endl;
	}

	return 0;
}

