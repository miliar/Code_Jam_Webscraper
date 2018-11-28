

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string inp_file = "C-small-attempt1.in";
string out_file = "C-small.out";

int compute( int** & counter, const string &s, int s_cor, const int & s_len, int search_cor, const string & search_for,const int & search_len)
{
	

	
	if( search_cor >= search_len)
	{
			counter[s_cor-1][search_cor-1] = 1; 
			return counter[s_cor-1][search_cor-1] ;
	}
	


	if(s_cor >= s_len)
	{
		counter[s_cor-1][search_cor-1]=0;
		return 0;
	}



	if(counter[s_cor][search_cor] == -1)
	{
			int count_total = 0;
			for(int i = s_len-1; i>= s_cor; i--)
			{
				if(s.at(i) == search_for.at(search_cor))
				{
				
					count_total +=	 compute(counter,s,i+1,s_len,search_cor+1,search_for,search_len);
				//	count_total %= 10000;
					counter[i][search_cor] = count_total;
				}
	
			}
			return count_total;
	}
	else
		return counter[s_cor][search_cor];
		
}

int main()
{
	ifstream input;
	input.open(inp_file.c_str());
	ofstream output;
	output.open(out_file.c_str());



	int num_of_cases;
	string s;

	input>>num_of_cases;

	getline(input,s);
	int s_len ;
	int** counter;
	string search_for = "welcome to code jam";
	int se_len = search_for.length();
	int cntt = 0;
	for(int n=1; n<= num_of_cases; n++)
	{
		getline(input,s);
		s_len = s.length();
		 counter = new int*[s_len];
		for(int c = 0 ; c<s_len; c++)
		{
			counter[c] = new int[se_len];
			for(int a = 0; a<se_len; a++)
				counter[c][a] = -1;
		}
		cntt = compute(counter,s,0,s_len,0,search_for,se_len);

		if(cntt<10)
			output<<"Case #"<<n<<": 000"<<cntt<<endl;
		else if(cntt<100)
			output<<"Case #"<<n<<": 00"<<cntt<<endl;
		else if(cntt<1000)
			output<<"Case #"<<n<<": 0"<<cntt<<endl;
		else
			output<<"Case #"<<n<<": "<<cntt<<endl;
	  
		for(int c2 = 0 ; c2<s_len; c2++)
		{
		 delete[]	counter[c2];
		}
		delete[]  counter;



	}
	input.close();
	output.close();

	return 0;
}