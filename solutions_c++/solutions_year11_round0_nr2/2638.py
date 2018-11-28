#include <vector>
#include <iostream>
#include <string>

using namespace std;

typedef unsigned int uint;
typedef unsigned long long ull;

struct lovers
{
	char p1, p2, baby;
	lovers(char mom, char dad, char babby) : p1(mom), p2(dad), baby(babby) {}
	lovers() : p1(0), p2(0), baby(0) {}
};

struct haters
{
	char bad, good;
	haters() : bad(0), good(0) {}
	haters(char b, char g) : bad(b), good(g) {}
};

char combines(vector<lovers> &react, char a, char b)
{
	for(uint i=0; i<react.size(); ++i)
	{
		lovers l = react.at(i);
		if((l.p1==a && l.p2==b) || (l.p2==a && l.p1==b) ) return l.baby;
	}
	return 0;
}

bool hasoppose(vector<haters> &react, vector<char> ab, char b)
{
	for(uint c = 0; c<ab.size(); ++c)
	{
		char a = ab.at(c);
		for(uint i=0; i<react.size(); ++i)
		{
			haters l = react.at(i);
			if((l.bad==a && l.good==b) || (l.good==a && l.bad==b) ) return true;
		}
	}
	return false;
}


int main()
{
	uint numTest;
	cin >> numTest;
	for(uint test=0; test<numTest; ++test)
	{
		//combinations
		int numComb;
		cin>>numComb;
		vector<lovers> combinators(numComb);
		for(int c=0; c<numComb; ++c)
		{
			string temp;
			cin >> temp;
			combinators.at(c) = lovers(temp[0], temp[1], temp[2]);
		}
		
		//oppositions
		int numOpp;
		cin>>numOpp;
		vector<haters> opposers(numOpp);
		for(int o=0; o<numOpp; ++o)
		{
			string temp;
			cin >> temp;
			opposers.at(o) = haters(temp[0], temp[1]);
		}
		
		//elements
		int numElem;
		cin >> numElem;
		string getem;
		cin >> getem;
		vector<char> elems;
		for(int e=0; e<numElem; ++e)
		{
			char curr = getem[e];
			
			//empty list means just add the char
			if(elems.size()==0) {
				elems.push_back(curr);
				continue;
			}
			
			//have at least one char
			char res = combines(combinators, elems.back(), curr);
			if(res != 0) elems.back() = res;
			else if(hasoppose(opposers, elems, curr)) elems.clear();
			else elems.push_back(curr);
		}
		
		cout<<"Case #"<<test+1<<": [";
		if(!elems.empty()) {
			for(uint p=0; p<elems.size()-1; ++p) { cout<<elems.at(p)<<", "; }
			cout<<elems.back();
		}
		cout<<"]"<<endl;
	}
}
