
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <math.h>
#include <vector>

using namespace std;

bool twoIntersect(int y1, int y11, int y2, int y21)
{
	if (y1 < y2 && y11>y21)
		return true;
	if (y1 > y2 && y11 < y21)
		return true;
	return false;
}

int main()
{
	ifstream input("A-large.in");
	ofstream output("largeAA.out");
	string line;

	int numInputs;
	input >> numInputs;

	for (int i=0; i<numInputs; i++)
	{
		//Parse a test case
		int n;
		input >> n;
		int num = 0;

		int (*wires)[2] = new int[n][2];
		for (int j=0; j<n; j++)
			input >> wires[j][0] >> wires[j][1];
		for (int j=0; j<n; j++)
			for (int k=0; k<n; k++)
				if (twoIntersect(wires[j][0],wires[j][1],wires[k][0],wires[k][1]))
					num++;


			//Write output line
		output << "Case #" << i+1 << ": " << num/2 << endl;

	}

	input.close();
	output.close();

	cout << "done\n";

	int a;
	cin >> a;
	return 0;
}
//
//#include <iostream>
//#include <fstream>
//#include <sstream>
//#include <string>
//#include <math.h>
//#include "tree.hh"
//
//using namespace std;
//
//tree<string> *folds;
//
//void parseLine(string parent, string line);
//int countLine(string line);
//
//int mai1n()
//{
//	ifstream input("small1A.in");
//	ofstream output("small1A.out");
//	string line;
//
//
//	int numInputs;
//	input >> numInputs;
//
//	for (int i=0; i<numInputs; i++)
//	{
//		folds = new tree<string>("ROOT");
//		//Parse a test case
//		int N,M;
//		input >> N >> M;
//
//		//Parse the first N lines:
//		for (int j=0; j<N; j++)
//		{
//			line = "";
//			while (line == "")
//				getline(input,line);
//			parseLine("ROOT", line);
//		}
//
//		int count = 0;
//		//Parse the M lines:
//		for (int j=0; j<M; j++)
//		{
//			line = "";
//			while (line == "")
//				getline(input,line);
//			count += countLine(line);
//		}
//
//		//Write output line
//		output << "Case #" << i+1 << ": " << count << endl;
//
//	}
//
//	input.close();
//	output.close();
//
//	cout << "done\n";
//
//	int a;
//	cin >> a;
//	return 0;
//}
//
//
//void parseLine(string parent, string line)
//{
//	//string curr;
//	//string rest;
//	//sscanf(line.c_str(),"/%[^/]%s",curr,rest);
//	//
//	//Find the parent folder
//	string temp = line;
//	tree_node_<string>* c = folds->head;
//	while (temp != "/" && temp!="")
//	{
//		string current;
//		sscanf(temp.c_str(),"/%[^/]%s",current,temp);
//		bool found = false;
//		for (tree_node_<string>* t=c->first_child; t<c->last_child; t++)
//			if (t->data == current)
//			{
//				c = t;
//				found = true;
//				break;
//			}
//		if (!found)
//			folds->append_child(c,current);
//		
//	}
//
//	//parseLine(parent.append(curr),rest);
//
//	
//}
//
//int countLine(string line)
//{
//	int count = 0;
//	//string curr;
//	//string rest;
//	//sscanf(line.c_str(),"/%[^/]%s",curr,rest);
//	//
//	//Find the parent folder
//	string temp = line;
//	tree<string>::iterator c = folds->begin();
//	while (temp != "/" && temp!="")
//	{
//		string current;
//		sscanf(temp.c_str(),"/%[^/]%s",current,temp);
//		bool found = false;
//		tree<string>::iterator t=c;
//		while (t!=c->end())
//			if (t->data == current)
//			{
//				c = t;
//				found = true;
//				break;
//			}
//			else
//				t++;
//		if (!found)
//		{
//			folds->append_child(c,current);
//			count++;
//		}
//		
//	}
//	return count;
//
//	//parseLine(parent.append(curr),rest);
//
//	
//}
//
