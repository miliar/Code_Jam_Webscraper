#include<iostream>
#include<fstream>
using namespace std;

class Invoker
{
	string str;
	char con[40][3];
	char opp[30][2];
	int con_size, opp_size;
	
public:
	Invoker()
	{
		reset();
	}
	
	void reset()
	{
		str = "";
		con_size = 0;
		opp_size = 0;
	}
	
	void setConbiner(char c1, char c2, char c3)
	{
		con[con_size][0] = c1;
		con[con_size][1] = c2;
		con[con_size][2] = c3;
		con_size++;
	}
	
	void setOpposer(char c1, char c2)
	{
		opp[opp_size][0] = c1;
		opp[opp_size][1] = c2;
		opp_size++;
	}
	
	void conbine()
	{
		if(str.length() < 2) return;
		
		char c1 = str[str.length() - 1], c2 = str[str.length() - 2];
		
		int i;
		
		for(i = 0; i < con_size; i++)
		{
			if((c1 == con[i][0] && c2 == con[i][1]) || (c1 == con[i][1] && c2 == con[i][0]))
			{
				str = str.substr(0, str.length() - 2) + con[i][2];
			}
		}
	}
	
	void oppose()
	{
		if(str.length() < 2) return;
		
		int i, j;
		
		for(i = 0; i < opp_size; i++)
		{
			if(str[str.length() - 1] == opp[i][0])
			{
				for(j = 0; j < str.length() - 1; j++)
				{
					if(str[j] == opp[i][1])
					{
						str = "";
						return;
					}
				}
			}

			if(str[str.length() - 1] == opp[i][1])
			{
				for(j = 0; j < str.length() - 1; j++)
				{
					if(str[j] == opp[i][0])
					{
						str = "";
						return;
					}
				}
			}
			
		}
				
	}
	
	/*void oppose()
	{
		if(str.length() < 2) return;
		
		int i, j, findLeft, findRight;
		bool zero;
		
		for(i = 0; i < opp_size; i++)
		{
			findLeft = findRight = -1;
			for(j = 0; j < str.length(); j++)
			{
				if(str[j] == opp[i][0])
				{
					findLeft = j;
					zero = true;
					break;
				}
				else if(str[j] == opp[i][1])
				{
					findLeft = j;
					zero = false;
					break;	
				}  
			}
			
			for(j++; j < str.length(); j++)
			{
				if(zero)
				{
					if(str[j] == opp[i][1])
					{
						findRight = j;
						break;
					}
				}
				else
				{
					if(str[j] == opp[i][0])
					{
						findRight = j;
						break;
					}
				}
			}
			
			if(findLeft > findRight)
			{
				i = findLeft;
				findLeft = findRight;
				findRight = i;
			}

			if(findLeft < 0 || findRight < 0) continue;

			str = str.substr(0, findLeft) + str.substr(findRight + 1, str.length() - findRight - 1);
		}
	}*/

	/*bool conbine(char& c1, char& c2)
	{
		int i;
		
		for(i = 0; i < con_size; i++)
		{
			if((c1 == con[i][0] && c2 == con[i][1]) || (c1 == con[i][1] && c2 == con[i][0]))
			{
				c1 = con[i][2];
				c2 = 0;
				return true;
			}
		}
		return false;
	}
	
	bool oppose(char& c1, char& c2, char& c3)
	{
		int i;
		
		for(i = 0; i < opp_size; i++)
		{
			if((c2 == opp[i][0] && c3 == opp[i][1]) || (c2 == con[i][1] && c3 == con[i][0]))
			{
				c2 = c3 = 0;
				return true;
			}
			
			if((c1 == opp[i][0] && c3 == opp[i][1]) || (c1 == con[i][1] && c3 == con[i][0]))
			{
				c1 = c2 = c3 = 0;
				return true;
			}
		}
		return false;
	}*/
	
	void put(char c)
	{
		if(c == 0) return;
		str += c;
	}
	
	string result()
	{
		string buf = "[";
		int i;
		for(i = 0; i < str.length(); i++)
		{
			buf += str[i];
			if(i != str.length() - 1) buf += ", ";
		}
		buf += "]";
		
		return buf;
	}
};

int main()
{
	ifstream fin("q3.in");
	ofstream fout("q3.out");
	
	int T; // cases
	int C; // conbiners
	int D; // opposers
	int N; // invokes
	Invoker inv;
	int i, j;
	char c1, c2, c3;
	
	fin >> T;
	
	for(i = 1; i <= T; i++)
	{
		inv.reset();
		
		fin >> C;
		
		for(j = 1; j <= C; j++)
		{
			fin >> c1 >> c2 >> c3;
			inv.setConbiner(c1, c2, c3);
		} 
		
		fin >> D;
		
		for(j = 1; j <= D; j++)
		{
			fin >> c1 >> c2;
			inv.setOpposer(c1, c2);
		}
		
		fin >> N;
		for(j = 1; j <= N; j++)
		{
			fin >> c1;
			inv.put(c1);
			
			inv.conbine();
			inv.oppose();
			/*inv.put(c1);
			c1 = c2;
			c2 = c3;
			fin >> c3;
			if(!inv.conbine(c2, c3)) inv.oppose(c1, c2, c3);*/
		}
		/*
		inv.put(c1);
		inv.put(c2);
		inv.put(c3);
		*/
		fout << "Case #" << i << ": ";
		
		fout<<inv.result();
		
		fout << endl;
	}
}