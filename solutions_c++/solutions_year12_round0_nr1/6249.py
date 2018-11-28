// Speaking in Tongues.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <map>
#include <list>
#include <vector>
#include <fstream>

using namespace std;

string convertInt(int number)
{
	if (number == 0)
		return "0";
	string temp="";
	string returnvalue="";
	while (number>0)
	{
		temp+=number%10+48;
		number/=10;
	}
	for (int i=0;i<temp.length();i++)
		returnvalue+=temp[temp.length()-i-1];
	return returnvalue;
}

string Output(string output, int caseNum)
{
	string tmp = "Case #";
	tmp += convertInt(caseNum);
	tmp += ": ";
	tmp += output;

	return tmp;
}

string Convert(string inPut, map<char, char>* pMap)
{
	string out = "";
	string::iterator strIt;
	map<char, char>::iterator mapIt;

	for(strIt = inPut.begin(); strIt < inPut.end(); strIt++)
		out += pMap->find(*strIt)->second;

	return out;
}

void CreateInputs(vector<string>* pIn)
{
	ifstream ifs("A-small-attempt3.in");
	string temp;

	while(getline(ifs, temp))
		pIn->push_back(temp);
}

int main()
{
	map<char, char>* pMapping = new map<char, char>();
	
	pMapping->insert(pair<char, char>('y','a'));
	pMapping->insert(pair<char, char>('n','b'));
	pMapping->insert(pair<char, char>('f','c'));
	pMapping->insert(pair<char, char>('i','d'));
	pMapping->insert(pair<char, char>('c','e'));
	pMapping->insert(pair<char, char>('w','f'));
	pMapping->insert(pair<char, char>('l','g'));
	pMapping->insert(pair<char, char>('b','h'));
	pMapping->insert(pair<char, char>('k','i'));
	pMapping->insert(pair<char, char>('u','j'));
	pMapping->insert(pair<char, char>('o','k'));
	pMapping->insert(pair<char, char>('m','l'));
	pMapping->insert(pair<char, char>('x','m'));
	pMapping->insert(pair<char, char>('s','n'));
	pMapping->insert(pair<char, char>('e','o'));
	pMapping->insert(pair<char, char>('v','p'));
	pMapping->insert(pair<char, char>('z','q'));
	pMapping->insert(pair<char, char>('p','r'));
	pMapping->insert(pair<char, char>('d','s'));
	pMapping->insert(pair<char, char>('r','t'));
	pMapping->insert(pair<char, char>('j','u'));
	pMapping->insert(pair<char, char>('g','v'));
	pMapping->insert(pair<char, char>('t','w'));
	pMapping->insert(pair<char, char>('h','x'));
	pMapping->insert(pair<char, char>('a','y'));
	pMapping->insert(pair<char, char>('q','z'));
	pMapping->insert(pair<char, char>(' ',' '));

	vector<string>* pInput = new vector<string>();
	
	CreateInputs(pInput);
	
	//list<string>* pInput = new list<string>();
	int samples = atoi(pInput->at(0).c_str());

	fstream filestr;

	filestr.open ("out.txt", fstream::in | fstream::out | fstream::app);

	vector<string>::iterator it;
	int i = 1;
	it = pInput->begin();
	it++;
	for(it; it != pInput->end(); it++)
	{
		filestr << Output(Convert(*it, pMapping), i++) << endl;
	}	
	

	return 0;
}

/*

o = e	
u = j
r = p
l = m
a = y
n = s
g = l
a = y
e = c
i = k
s = d
m = x
p = v 
o = e
b = n
t = r
u = j
n = s
d = i
r = p
z = q
c = f
f = w
j = u
k = o
v = g
w = t
x = h
y = a

a b c d e f g h i j k l m n o p q r s t u v w x y z
y n f i c w l ? k u o m x s e v ? p d r j g t h a q


h = ?
q = ? 
? = b
? = z
*/