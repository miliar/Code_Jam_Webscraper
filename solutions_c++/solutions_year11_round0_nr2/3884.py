// Jai Mata Di
#include<string>
#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
class Magicka
{
	string sequence;
	string C;
	string D;

	void destroy()
	{
		for(int ptr = 0; ptr < sequence.length(); ptr++)
		{
			int z = D.find(sequence[ptr]);
			if( z != sequence.npos )
			{
				int y = C.find(sequence[ptr]);
				if (y != sequence.npos)
				{
					//string c2 = constructc2(ptr);
					//if(!isNeighbourInBefore(c2, ptr) && !isNeighbourInAfter(c2,ptr))
					if(ptr == 0 || formsCombo(sequence[ptr-1],sequence[ptr]) == '*')
					{
						goto okToDelete;
					}
					else if( ptr == sequence.length()-1 || formsCombo(sequence[ptr],sequence[ptr+1]) == '*')
					{
						goto okToDelete;
					}
				}
				else
				{
					okToDelete:
					char d1;
					string d2;
					d1 = sequence[ptr];
					d2 = constructd2(ptr);
					int x = sequence.find_first_of(d2);
						//string endc2 = constructc2(x);
						//if(!isNeighbourInBefore(endc2, x))
					int w = C.find(sequence[x]);
					if(w != sequence.npos)
					{
						if(formsCombo(sequence[w-1],sequence[w]) == '*')
						{
							goto okToDel;
						}
					}
					else
					{
						okToDel:
						sequence = sequence.substr(x+1);
						x = sequence.npos;
					}
				}
			}
		}
	}

	string constructd2(int ptr)
	{
		char d1 = sequence[ptr];
		string d2= "";
		string substr = D;
		int z = substr.find_first_of(d1);
		while(z != sequence.npos)
		{
			if(z%2 == 0)
			{
				d2+=D[z+1];
				substr= substr.substr(z+2);
				z = substr.find_first_of(d1);
			}
			else
			{
				d2+=D[z-1];
				substr= substr.substr(z+1);
				z = substr.find_first_of(d1);
			}
		}
		return d2;
	}
	
	void performSerialOperations()
	{
		int i=0;
		int y=0;
		while(i<sequence.length())
		{
			if(i==0)
			{
				i++;
			}
			else
			{
				char combo = formsCombo(sequence[i],sequence[i-1]);
				if(combo!='*')
				{
					string a = sequence.substr(0,i-1);
					string b = "";
					if(i<sequence.length()-1)
						b = sequence.substr(i+1);
					sequence = a + combo + b;
				}
				else
				{
					if(D.find(sequence[i]) != sequence.npos)
					{
						char d1= sequence[i];
						string d2= constructd2(i);
						string a = sequence.substr(0,i);
						int q = a.find_first_of(d2);
						if( q != sequence.npos)
						{
							sequence = sequence.substr(i+1);
							i = 0;
						}
						else
						{
							i++;
						}
					}
					else
					{
						i++;
					}
					/*
					int from = 0;
					int j = formsDestroy(i, );
					if(j != i)
					{
						i=j;
					}
					else
					{
						i++;
					}*/
				}
			}
		}
	}

	char formsCombo(char ch1,char ch2)
	{
		int z = C.find(ch1);
		if(z != sequence.npos)
		{
			if(z%3 == 0)
			{
				if(C[z+1] == ch2)
				{
					return C[z+2];
				}
			}
			else if(z%3 == 1)
			{
				if(C[z-1] == ch2)
				{
					return C[z+1];
				}
			}
		}
		return '*';
	}
	
	int formsDestroy(int i)
	{
		char d1= sequence[i];
		string d2= constructd2(i);
		string a = sequence.substr(0,i);
		int q = a.find_first_of(d2);
		if(q!=sequence.npos)
		{
			string a = sequence.substr(0,q);
			string b = sequence.substr(i+1);
			sequence = a + b;
			return q+1;
		}
		return i;
	}

public:
	Magicka(string str, string distroy,string combine)
	{
		sequence= str;
		C = combine;
		D = distroy;
	}
	
	string Run()
	{
		//destroy();
		performSerialOperations();
		return sequence;
	}
};
int main()
{
	try{

	// Prepare File Stream
	ifstream ip("ip.txt");
	ofstream op("op.txt");
	if(!ip.is_open() || !op.is_open())
	cout<<"Cannot Open File";
	
	int noOfTestCases=0;
	ip>>noOfTestCases;

	for(int i=0; i<noOfTestCases; i++)
	{
		int sizeOfC;
		int sizeOfD;
		int sizeOfS;
		string C="";
		string D="";
		string s="";

		ip>>sizeOfC;
		if(sizeOfC > 0)
		{
			ip>>C;
		}

		ip>>sizeOfD;
		if(sizeOfD > 0)
		{
			ip>>D;
		}

		ip>>sizeOfS;
		if(sizeOfS > 0)
		{
			ip>>s;
		}
		
		Magicka m = Magicka(s,D,C);
		string output = m.Run();
		op<< "Case #"<<i+1<<": [";
		if(output.length() > 0)
		{
			op<<output[0];
		}
		for(int ctr = 1 ; ctr<output.length(); ctr++)
		{
			op<<", "<<output[ctr];
		}
		op<<"]"<<endl;
	}

	//Closure
	char ch;
	cin>>ch;
	ip.close();
	op.close();
	}
	catch(exception e)
	{
		cout<<"Excp";	
	}
	
	return 0;
}

/*_____________________Code Dump____________________________

/*
class Magicka
{
	string sequence;
	string combination;
	string opposition;
	string outputSequence;
	void removeOppositions()
	{
		for(int i=0; i<sequence.length(); i++)
		{
			int z = opposition.find(sequence[i]) ;
			if( z != string.npos)  //present
			{
				int y = combination.find(sequence[i]);
				if(y != string.npos)
				{
					int oppPartner = -1;
					if( z%3 == 0)
					{
						oppPartner = opposition[z+1];
					}
					else if( z%3 ==1)
					{
						oppPartner = opposition[z-1];

					}
					int y = opposition.find(oppPartner);
					if( y != string.npos)  //present
					{

					}
					else
					{

					}
				}
				else 
				{
					//Delete
				}
			}
		}
	}
	void performSerialOperations()
	{

	}
public:
	Magicka(string comb,string opp,string seq)
	{
		sequence = seq;
		combination = comb;
		opposition = opp;
	};
	int Run()
	{
		removeOppositions();
		performSerialOperations();
	}
}; 
*/
/*

	bool isNeighbourInBefore(string c2,int ptr)
	{
		if(ptr>0)
		{
			if(c2.find(sequence[ptr-1]) != sequence.npos)
			{
				return true;
			}
		}
		return false;
	}
	bool isNeighbourInAfter(string c2,int ptr)
	{
		if(ptr<sequence.length() -1)
		{
			if(c2.find(sequence[ptr+1]) != sequence.npos)
			{
				return true;
			}
		}
		return false;
	}
	string constructc2(int ptr)
	{
		char c1 = sequence[ptr];
		string c2 ="";
		string substr = C;
		int z = C.find_first_of(c1);
		while(z != sequence.npos)
		{
			if(z%3 == 0)
			{
				c2 += C[z+1];
				substr= substr.substr(z+2);
				z = substr.find(c1);
			}
			else if(z%3 == 1)
			{
				c2+=C[z-1];
				substr= substr.substr(z+1);
				z = substr.find(c1);
			}
		}
		return c2;
	}
	*/
/*______________Code Dump End____________________________*/
