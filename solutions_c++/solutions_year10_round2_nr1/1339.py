#include <iostream>
#include <stdio.h>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <sstream>

using namespace std;
vector< set<string> > dirlevels;
set<string> dirs;

/*
struct node	{
	vector<string> dirs;
	set<string> check;
	vector<node> child;
};

node root;

void printRoot()	{

	cout << "root " << root.dirs.size() << endl;
	
	for (int i = 0; i < root.dirs.size(); i++)
		cout << root.dirs[i] << " ";
	cout << endl;
}

int insertToTree(string line, node * blah)	{

	cout << line;
	
	stringstream input (line);
	string first;
	input >> first;
	bool last = input.eof();

	cout << " " << first << endl;

	if (first.length() == 0)
		return 0;

	int total = 0;

	if (blah.check.count(first) == 0)	{
		blah->dirs.push_back(first);
		blah->check.insert(first);
		node stuff;
		blah->child.push_back(stuff);
		total += 1;
		string shitshit;

 		int blahblahshit = 0;

		first.clear();
		input >> first;
		while (!input.eof())	{
// 			blahblahshit++;
			shitshit += first;
			shitshit += " ";
			input >> first;
		}
		if (!last)
			shitshit += first;

 		cout << shitshit << " "<<  blahblahshit << endl;
		
		total += insertToTree (shitshit, (node &) blah->child[blah.dirs.size() - 1]);
	} else	{
		string shitshit;

		first.clear();
		input >> first;
// 		int blahblahshit = 0;
		while (!input.eof())	{
// 			blahblahshit++;
			shitshit += first;
			shitshit += " ";
			input >> first;
		}
		
		if (!last)
			shitshit += first;

// 		cout << shitshit << " " << blahblahshit << endl;
		
		for (int i = 0; i < blah.dirs.size(); i++)	{
			if (blah.dirs[i].compare(first) == 0)	{
				insertToTree (shitshit,(node &) blah->child[i]);
				break;
			}
		}
	}

	return total;
}

int main()	{
	int testnum;
	cin >> testnum;
	
	for (int i = 0; i < testnum; i++)	{
		
		int a,b;
		cin >> a >> b;

		for (int j = 0; j < a; j++)	{
			
			string line;
			cin >> line;
			for (int k = 0; k < line.length(); k++)	{
				if (line[k] == '/')
					line[k] = '\n';
			}

insertToTree(line, (node &) root);
			printRoot();
		}


		int total = 0;
		for (int j = 0; j < b; j++)	{

			string line;
			cin >> line;

			for (int k = 0; k < line.length(); k++)	{
				if (line[k] == '/')
					line[k] = ' ';
			}

total += insertToTree(line, (node &) root);
			printRoot();
		}

		cout << "Case #" << (i+1) << ": " << total << endl;
	}

}
*/


int main()	{

	int testnum;
	cin >> testnum;

	for (int i = 0; i < testnum; i++)	{

		int a,b;
		cin >> a >> b;

		for (int j = 0; j < a; j++)	{

			string line;
			cin >> line;
			for (int k = 0; k < line.length(); k++)	{
				if (line[k] == '/')
					line[k] = ' ';
			}

			stringstream blah (line);

			int index = 0;
			string blahblahshit;
			while (!blah.eof())	{
				string tempblah;
				blah >> tempblah;
				blahblahshit += tempblah;

				dirs.insert(blahblahshit);

				/*
				if (dirlevels.size() == index)	{
					set<string> derp;
					dirlevels.push_back(derp);
				}

// 				cout << tempblah << " " << index << endl;
				dirlevels[index++].insert(tempblah);*/
			}
		}

		int total = 0;

		for (int j = 0; j < b; j++)	{

			string line;
			cin >> line;
			
			for (int k = 0; k < line.length(); k++)	{
				if (line[k] == '/')
					line[k] = ' ';
			}

// 			cout << line << endl;
			stringstream blah (line);

			int index = 0;
			int counter = -1;
			string blahblahshit;
			while (!blah.eof())	{
				string tempblah;
				blah >> tempblah;
				blahblahshit += tempblah;

				if (dirs.count(blahblahshit) == 0)	{
					dirs.insert(blahblahshit);
					total++;
				}

/*
				if (dirlevels.size() == index)	{
					set<string> derp;
					dirlevels.push_back(derp);
				}

// 				cout << tempblah << endl;
				
				if (dirlevels[index].count(tempblah) == 0)	{
// 					cout << tempblah << " " << index << endl;

					if (counter == -1)
						counter = index;
					
					dirlevels[index].insert(tempblah);
				}
				
				index++;
				*/
			}

// 			cout << counter << " " << index << endl;
// 			if (counter != -1)
// 				total += index - counter;
		}



// 		for (int k = 0; k < dirlevels.size(); k++)
// 			dirlevels[k].clear();
// 		dirlevels.clear();

		dirs.clear();
		cout << "Case #" << (i+1) << ": " << total << endl;
	}
}
