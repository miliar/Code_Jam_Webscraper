#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

struct Node
{
public:
	double value;
	string name;
	Node* exact;
	Node* another;
	Node* parent;

	Node() { value = 0.0; name = ""; exact = NULL; another = NULL; parent = NULL; }
};

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fout.precision(7);
	int cases = 0;
	fin >> cases;
	for (int i = 0; i < cases; i++)
	{
		int lines = 0;
		fin >> lines;
		string temp;
		string line;
		fin.ignore();
		for (int j = 0; j < lines; j++)
		{
			getline(fin, temp);
			line += temp;
		}

		// build tree
		Node root = Node();
		Node* current = &root;
		double val;

		for (int j = 0; j < (int)line.size(); j++)
		{
			if (line[j] == '(')
			{
				if (current->exact == NULL)
				{
					Node* temp = new Node();
					temp->parent = current;
					current->exact = temp;
					current = temp;
				}
				else
				{
					Node* temp = new Node();
					temp->parent = current;
					current->another = temp;
					current = temp;
				}
			}
			else if (line[j] == ')')
			{
				current = current->parent;
			}
			else if (line[j] == '0' || line[j] == '1')
			{
				string number;
				for (; isdigit(line[j]) || line[j] == '.'; j++)
				{
					number += line[j];
				}
				j--;

				istringstream os(number);
				os >> val;
				current->value = val;
			}
			else if (isalpha(line[j]))
			{
				string name;
				for (; isalpha(line[j]); j++)
				{
					name += line[j];
				}
				j--;

				current->name = name;
			}
		}

		int animals = 0;
		fin >> animals;
		fout << "Case #" << i + 1 << ":" << endl;
		for (int j = 0; j < animals; j++)
		{
			fin >> temp;
			int count = 0;
			fin >> count;
			vector<string> features;
			for (int k = 0; k < count; k++)
			{
				fin >> temp;
				features.push_back(temp);
			}

			current = root.exact;
			double result = 1.0;
			while (current != NULL)
			{
				result *= current->value;
				bool has = false;
				for (int m = 0; m < (int)features.size(); m++)
				{
					if (features[m] == current->name)
					{
						has = true;
						break;
					}
				}
				
				if (has)
				{
					current = current->exact;
				}
				else
				{
					current = current->another;
				}
			}

			fout << fixed << result << endl;

		}
	}
	fin.close();
	fout.close();
	return 0;
}