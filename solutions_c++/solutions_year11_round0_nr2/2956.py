#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

#define lint long long
#define uint usigned long long

struct clearCombo
{
	char otherChar;
	int count;
};



class ClearComboList
{
	map<char, clearCombo> data;
public:
	void AddCombo(char c1, char c2)
	{
		clearCombo item;
		item.count=0;
		item.otherChar = c1;
		data[c2]=item;
		item.otherChar = c2;
		data[c1]=item;
	}
	
	bool CheckForClear(char c)
	{
		if(data.find(c) == data.end())
			return false;
		if(data[data[c].otherChar].count == 0)
		{
			data[c].count++;
			return false;
		}
		
		map<char, clearCombo>::iterator it = data.begin();
		while(it != data.end())
		{
			it->second.count=0;
			it++;
		}
		return true;
	}
	
	void Combined(char c)
	{
		if(data.find(c) != data.end() && data[c].count >0)
			data[c].count--;
	}
};

struct combineCombo
{
	char otherChar;
	char newChar;
};

class CombineComboList
{
	map<char, combineCombo> data;
public:
	void AddCombo(char c1, char c2, char result)
	{
		combineCombo item;
		item.newChar=result;
		item.otherChar = c1;
		data[c2]=item;
		item.otherChar = c2;
		data[c1]=item;
		
	}
	
	bool CheckCombine(char c1, char c2, char * result)
	{
		if(data.find(c1) == data.end())
			return false;
		
		if(data[c1].otherChar != c2)
			return false;
		   
		*result = data[c1].newChar;
		return true;
	}
	
};

int main (int argc, char * const argv[]) {
    
	ifstream inFile("../../input.txt");
	ofstream outFile("../../output.txt");
	int numCases;
	inFile >> numCases;
	for(int caseNum =1; caseNum <=numCases; caseNum++)
	{
		CombineComboList combiner;
		ClearComboList opposer;
		
		int numCombs;
		inFile >>  numCombs;
		for(int cntr =0; cntr< numCombs; cntr++)
		{
			char tmpCh1, tmpCh2, tmpCh3;
			inFile>>tmpCh1;
			inFile>>tmpCh2;
			inFile>>tmpCh3;
			combiner.AddCombo(tmpCh1, tmpCh2, tmpCh3);
		}
		
		inFile >>  numCombs;
		for(int cntr =0; cntr< numCombs; cntr++)
		{
			char tmpCh1, tmpCh2;
			inFile>>tmpCh1;
			inFile>>tmpCh2;
			opposer.AddCombo(tmpCh1, tmpCh2);
		}
		
		vector<char> result;
		int numElems;
		inFile >>  numElems;
		char lastChar='\0';
		for(int cntr =0; cntr< numElems; cntr++)
		{
			char newElem;
			inFile>>newElem;
			
			if(combiner.CheckCombine(newElem, lastChar, &newElem))
			{
				opposer.Combined(result[result.size()-1]);
				result[result.size()-1]=newElem;
				lastChar=newElem;
			}
			else if(opposer.CheckForClear(newElem))
			{
				result.clear();
				lastChar= '\0';
			}
			else
			{
				lastChar=newElem;
				result.push_back(newElem);
			}
			
		}
		
		
		int sz = result.size();
		cout<<"Case #"<<caseNum<<": [";
		outFile<<"Case #"<<caseNum<<": [";
		for(int cntr=0; cntr< sz-1; cntr++)
		{
			cout<<result[cntr]<<", ";
			outFile<<result[cntr]<<", ";
			
		}
		if(sz>0)
		{
			cout<<result[result.size()-1];
			outFile<<result[result.size()-1];
		}
		cout<<"]\n";
		outFile<<"]\n";
		
	}
	inFile.close();
	outFile.close();
	std::cout << "Done!\n";
    return 0;
}
