// test.cpp : Defines the entry point for the console application.
//


#include <iostream>
#include <string>
#include <fstream>

using namespace std;





int main()
{	

	ifstream infile("f:\\jx\\A-small-attempt0", ios::in);
	ofstream outfile("f:\\jx\\a", ios::out);


	int l,d, n;
	string str[5000];
	infile >> l >> d >> n;
	for(int i=0; i<d; i++)
	{
		infile >> str[i];
	}
	bool bit[15][26];
	
	for(int nn = 1; nn <= n; nn++)
	{
		string in;
		infile >> in;
		for(int i=0; i<15; i++) for(int j=0; j<26; j++) bit[i][j] = 0;

		bool stop = false;
 
	



		int p = 0;
		for(int i=0; i<in.length (); i++)
		{
			if(in[i]=='(') 
				stop = true;
			else if(in[i]==')')
			{
				p++;
				stop = false;
			}
			else 
			{
				bit[p][in[i]-'a'] = true;
				if(!stop)
					p++;
			}
		}
     string t;
	//	for(int i=0; i<15; i++){ for(int j=0; j<26; j++) cout <<bit[i][j]<< " "; cout << endl;} getline(cin, t);

		int sum = 0;
		for(int i=0; i<d; i++)
		{
			int j;
			for(j=0; j<str[i].length(); j++)
			{
				if(!bit[j][str[i][j]-'a']) break;
			}
			if(j == l) sum++;
		}

		outfile << "Case #" << nn << ": " << sum << endl;
	}


	return 0;
}

