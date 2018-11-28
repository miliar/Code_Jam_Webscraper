#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<cmath>
#include<map>

using namespace std;

char reverseReplacement[] = 
{
	// abcd
	'y',
	'n',
	'f',
	'i',

	//efgh
	'c',
	'w',
	'l',
	'b',
	
	//ijkl
	'k',
	'u',
	'o',
	'm',
	
	//mnop
	'x',
	's',
	'e',
	'v',
	
	//qrst
	'3',
	'p',
	'd',
	'r',
	
	//uvwx
	'j',
	'3',
	't',
	'h',
	
	//yz
	'a',
	'q',
};

char replacement[] = 
{
	// abcd
	'y',
	'h',
	'e',
	's',
	
	//efgh
	'o',
	'c',
	'v',
	'x',
	
	//ijkl
	'd',
	'u',
	'i',
	'g',
	
	//mnop
	'l',
	'b',
	'k',
	'r',
	
	//qrst
	'z',
	't',
	'n',
	'w',
	
	//uvwx
	'j',
	'p',
	'f',
	'm',
	
	//yz
	'a',
	'q',
};


int process_testcaseA(string s)
{
	int rv = 0;
	istringstream iss(s);
	int a,b;
	iss >> a >> b;
	int numdigits = 0;
	int multiplier = 1;
	int x = a;
	map<string, int>found;
	
	for(int i = 0; i < s.length(); i++)
	{
		if(' ' != s[i])
			s[i] = replacement[s[i]-'a'];
	}
	
	cout << s << endl;
	
	return rv;
}

int process_testcaseB(string inpp)
{
	int rv = 0;
	istringstream iss(inpp);
	int n, s, p;
	iss >> n >> s >> p;

	vector<int> scores;

	int usedSurprises = 0;
	for(int i = 0; i < n; i++)
	{
		int j;
		iss >> j;
		scores.push_back(j);
		int rem = j % 3;
		int possibleSurprise = 0;
		if( (j < 29) && (j > 1) )
		{
			possibleSurprise = 1;
		}
		int currentmax = j/3+((rem)?1:0); // this is the unsurprising max
		if(currentmax >= p)
		{
			rv++;
		}
		else
		{
			if(( possibleSurprise) && (s>0))
			{
				
				currentmax = j/3;
				switch (rem) {
					case 0:
					case 1:
						currentmax += 1;
						break;
					case 2:
						currentmax += 2;
						
					default:
						break;
				}
				if(currentmax >= p)
				{
					rv++;
					s--;
				}
			}
		}
			
	}

	return rv;
}


int main(int argc, const char *argv[])
{
	int tc = 0;
	ifstream is;
	if(argc == 1)
		is.open("inp.txt");
	else
		is.open(argv[1]);
	
	
	// find total number of testcases
	string s;
	getline(is,s); 
	istringstream iss(s);
	iss >> tc;
	//printf("num tc == %d\n", tc);
	
	// for every testcase
	for(int i = 1; i <= tc; i++)
	{
		printf("Case #%d: ",i);
		getline(is,s);
		cout << process_testcaseB(s) << endl;
	}
	is.close();
	return 0;
}
