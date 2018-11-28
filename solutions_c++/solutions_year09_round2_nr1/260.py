#include <iostream>  
#include <string>  
#include <vector>  
#include <set>  
#include <map>  
#include <algorithm>  
#include <math.h>  
#include <sstream>  
#include <ctype.h>  
#include <queue>  
#include <stack>  
#include <fstream>
#include <iomanip>
using namespace std;  

template<class Item>  
void display(vector<Item> v)  
{  
  for(int i=0; i<v.size(); i++)  
    cout << v[i] << ' ';  
  cout << '\n';  
}   

struct tree
{

	string node;
	double prob;
	
	int left, right;
};

vector<tree> trees;
vector<string> words;
int curIndex;

int buildTree( string prev="ABC")
{
int n = trees.size();
tree temp;
trees.push_back(temp);
stringstream s1;
//cout << words[curIndex] << ' ' << words[curIndex+1] << endl;
s1 << words[curIndex++] << " ";
s1 << words[curIndex++];
s1 >> trees[n].prob;
s1 >> trees[n].node;
cout << trees[n].prob << ' ' << trees[n].node << endl;
if(trees[n].node==")")
{
	trees[n].left = trees[n].right = -1;
	trees[n].node = "AAA";
	return 1;
}

curIndex++;

trees[n].left = trees.size();
buildTree();

curIndex++;

trees[n].right = trees.size();
buildTree();

curIndex++;

return 1;
}






int main()
{

int  N, L, A;

fstream In("a-large.in", ios::in);
fstream Out("a-large.out", ios::out);
In >> N;
vector<string> text;

for(int h=0; h<N; h++)
{
	Out << "Case #" << h+1 << ": " <<endl;
	cout << "CASE " << h+1 << endl;
	In >> L;
	cout << L << endl;
	trees.resize(0);
	char stemp[100];
	string temp;
	text = vector<string>(L, "");
	In.getline(stemp,90);
	for(int i=0; i<L; i++)
	{	In.getline(stemp, 90);
		//cout << stemp << endl;
		string temp2(stemp);
		for(int j=0; j<temp2.size() && temp2[j] != '\n'; j++)
			if(temp2[j] == '(' || temp2[j] == ')')
			{	text[i] += " ";
				text[i] +=temp2[j];
				text[i] += " " ;
			}
			else text[i] += temp2[j];

	}

	stringstream In2;
		
	for(int i=0; i<L; i++) In2 << text[i] << " ";
	words.resize(0);
	while(!In2.eof() )
	{
		In2 >> temp;
		words.push_back(temp);
	}
	curIndex = 1;
	buildTree();

	for(int i=0; i<trees.size(); i++)
	{;
	//	cout << "Node " << i << ": " << trees[i].prob << endl
	//		<< trees[i].node << endl << trees[i].left << ' ' << trees[i].right << endl;

	}

	In >> A;

	for(int m=0; m<A; m++)
	{
		double prob = 1;
		set<string> prop;
		string s;
		In >> s;
		int a;
		In >> a;

		for(int i=0; i<a; i++)
		{	In >> s;
			prop.insert(s);
		}

		int cur = 0;
		while(cur != -1)
		{
			prob *= trees[cur].prob;
			if(prop.find(trees[cur].node)!=prop.end() )
				cur = trees[cur].left;
			else cur = trees[cur].right;
		}
		Out << setprecision(8) << fixed << prob << endl;
	}
			

}

In.close();

Out.close();

return 0;

}
