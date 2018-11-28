/*
 * Welcome.cpp
 *
 *  Created on: 2009-9-3
 *      Author: sailingwood
 */

#include <string>
#include <fstream>
#include <iostream>
using namespace std;

class Welcome
{
public:
	static string toMatch;
	int N;
	void run()
	{
		ifstream in("C-small-attempt0.in");
		ofstream out("C-small-attempt0.out");
		in>>N;
		std::getline(in, target);
		for (int i=0; i<N; i++)
		{
			std::getline(in, target);
//			cout<<target<<endl;
			int result = count(0, 0);
			char outline[100];
			std::sprintf(outline, "Case #%d: %04d\n", i+1, result);
			out<<outline;
		}
	}
private:
	string target;
	int count(int toMatchStart, int targetStart)
	{
		if (toMatchStart == toMatch.size())
			return 1;
		char matchChar = toMatch.c_str()[toMatchStart];
//		cout<<"#"<<toMatchStart<<" char: "<<matchChar<<endl;
		for (int i=targetStart; i<target.size(); i++)
		{
			if (target.c_str()[i] == matchChar)
			{
//				cout<<"In target string position "<<i<<" matched"<<endl;
				return (count(toMatchStart+1, i+1) + count(toMatchStart, i+1))%10000;
			}
		}
		return 0;
	}
};

string Welcome::toMatch = string("welcome to code jam");

int main(int argc, char** argv)
{
	Welcome w;
	w.run();
}
