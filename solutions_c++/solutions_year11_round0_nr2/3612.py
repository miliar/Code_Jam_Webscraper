#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string opposeOp(bool opposeList[26][26], string spell, int lookTill)
{
	int size = spell.size();
	const char * cs = spell.c_str ();

	for(int i = 0;i<=lookTill;i++)
	{
		for(int j = i+1;j<=lookTill+1;j++)
		{
			int ascii1 = static_cast<int>(cs[i])-65;
			int ascii2 = static_cast<int>(cs[j])-65;

			if(opposeList[ascii1][ascii2] == true)
			{
				spell = spell.substr(j+1,size-(j+1));
				j=100000;
				i=100000;
			}
		}
		

	}
	return spell;
}

string invokeOp(string invokeList[26][26],string spell,bool opposeList[26][26])
{	
	int size = spell.size();
	for(int i = 0;i<size-1;i++)
	{
		const char * cs = spell.c_str ();
		
		int ascii1 = static_cast<int>(cs[i])-65;
		int ascii2 = static_cast<int>(cs[i+1])-65;

		if(invokeList[ascii1][ascii2] != "LOL")
		{
			spell = spell.substr(0,i) + invokeList[ascii1][ascii2] + spell.substr(i+2,size-i+2);
			size = spell.size();
			i = i-1;
		}
		else
		{
			string oldSpell = spell;
			spell = opposeOp(opposeList,spell,i);
			if(oldSpell != spell)
			{
				size = spell.size();
				i = -1;
			}
		}

	}
	return spell;
}


int main()
{
	int caseAmount;
	ifstream input;
	input.open("input.txt");
	ofstream output("output.txt");

	input>>caseAmount;
	int caseMet = 0;

	while(caseMet != caseAmount)
	{
		int numOfInvokes;
		input>>numOfInvokes;

		string invokeList[26][26];
		for(int i = 0; i<26; i++)
			for(int j= 0; j<26; j++)
				invokeList[i][j] = "LOL";

		for(int i = 0; i<numOfInvokes; i++)
		{
			string invoke;
			input>>invoke;
			const char * cs = invoke.c_str ();

			invokeList[static_cast<int>(cs[0])-65][static_cast<int>(cs[1])-65]=invoke.substr(2,1);
			invokeList[static_cast<int>(cs[1])-65][static_cast<int>(cs[0])-65]=invoke.substr(2,1);
		}

		int numOfOppose;
		input>>numOfOppose;

		bool opposeList[26][26];
		for(int i = 0; i<26; i++)
			for(int j= 0; j<26; j++)
				opposeList[i][j] = false;

		for(int i = 0; i<numOfOppose; i++)
		{
			string oppose;
			input>>oppose;
			const char * cs = oppose.c_str ();

			opposeList[static_cast<int>(cs[0])-65][static_cast<int>(cs[1])-65]=true;
			opposeList[static_cast<int>(cs[1])-65][static_cast<int>(cs[0])-65]=true;
		}

		int numOfSpellChar;
		input>>numOfSpellChar;
		string spell;
		input>>spell;

		// INIT DONE


		/*
		for(int i = 0; i<26; i++)
		{
			for(int j = 0; j<26; j++)
			{
				if(invokeList[i][j] != "LOL")
				{
					cout<<invokeList[i][j]<<endl;
				}
				if(opposeList[i][j] != false)
				{
					cout<<"GUM"<<endl;
				}
			}
		}

		cout<<spell<<endl;
		cout<<"-------------"<<endl;
		cout<<endl;
		*/
		spell = invokeOp(invokeList,spell,opposeList);

		output<<"Case #";
		output<<caseMet+1;
		output<<": [";
		const char * ch = spell.c_str();
		int spSize = spell.size();
		for(int k = 0; k<spSize; k++)
		{
			if(k == 0)
				output<<ch[k];
			else
			{
				output<<", ";
				output<<ch[k];
			}
		}
		output<<"]";
		output<<endl;

		// INCREMENT END REST

		caseMet++;
	}
	
	

	return 0;
}