#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>


using namespace std;

#define INTVAR int
vector<INTVAR> tokenize_str(const string & str,
							const string & delims)
{
	using namespace std;
	// Skip delims at beginning, find start of first token
	string::size_type lastPos = str.find_first_not_of(delims, 0);
	// Find next delimiter @ end of token
	string::size_type pos     = str.find_first_of(delims, lastPos);

	// output vector
	vector<INTVAR> tokens;

	while (string::npos != pos || string::npos != lastPos)
	{
		// Found a token, add it to the vector.
		string temp = str.substr(lastPos, pos - lastPos);
		INTVAR tempint = atoi(temp.c_str());
		tokens.push_back(tempint);
		// Skip delims.  Note the "not_of". this is beginning of token
		lastPos = str.find_first_not_of(delims, pos);
		// Find next delimiter at end of token.
		pos     = str.find_first_of(delims, lastPos);
	}

	return tokens;
}
enum values
{
	B=0,
	R=1,
	BOTH=2,
	NEITHER=3
};

void rotate(vector <string>& in)
{
	for (int i =0;i<in.size();i++)
	{
		for (int j=in.size()-1;j>=0;j--)
		{
			if(in[i][j] == '.') 
			{
				bool foundN = false;
				int yc=j;
				int yp=j-1;
				while ( !foundN && yp>=0 )
				{
					if ( in[i][yp] != '.')
					{
						foundN = true;
						bool foundDot = false;
						while (!foundDot && yc>=0 && yp>=0 )
						{
							in[i][yc] = in[i][yp];
							in[i][yp] = '.';
							yc = yc-1;
							yp=yp-1;
						}
						break;
					}
					yp=yp-1;
				}
			}
		}
	}
}

int nx[] = {1,0,-1,0,1,1,-1,-1};
int ny[] = {0,-1,0,1,1,-1,-1,1};

values calculate(vector <string>& in,int K)
{
	values v;
	bool isB = false;
	bool isR = false;
	for (int i =0;i<in.size();i++)
	{
		for (int j=0;j<in.size();j++)
		{
			if(in[i][j] == 'B')
			{
				for (int k = 0; k < 8; k++ && !isB  )
				{
					int tempx = i+nx[k];
					int tempy = j+ny[k];
					bool conti =  true;
					int countB = 1;
					while ( conti )
					{
						if ( tempx >=0 && (tempx  < in.size()) &&
							 tempy >=0 && (tempy  < in.size()) && in[tempx][tempy] == 'B')
						{
							countB++; 
							if(countB == K)
							{
								isB=true;
								break;
							}
							conti=true;
							tempx = tempx+nx[k];
							tempy = tempy+ny[k];
						}
						else
							conti=false;

					}

				}
			}
			else if(in[i][j] == 'R')
			{
				for (int k = 0; k < 8; k++ && !isR  )
				{
					int tempx = i+nx[k];
					int tempy = j+ny[k];
					bool conti =  true;
					int countR = 1;
					while ( conti )
					{
						if ( tempx >=0 && (tempx  < in.size()) &&
							 tempy >=0 && (tempy  < in.size()) && in[tempx][tempy] == 'R')
						{
							countR++; 
							if(countR == K)
							{
								isR=true;
								break;
							}
							conti=true;
							tempx = tempx+nx[k];
							tempy = tempy+ny[k];
						}
						else
							conti=false;

					}
				}
			}
		}
	}
	if ( isB && !isR )
		v = B;
	else if ( !isB && isR )
		v = R;
	else if ( isB && isR )
		v = BOTH;
	else if ( !isB && !isR )
		v = NEITHER;
	return v;
}
int main()
{
	string line;
	ifstream inp("d:/A-small-practice.in");
	ofstream out("d:/A-small-practice.out",ios::out);
    if (! inp.eof() )
    {
      getline (inp,line);
    }
	int Ntc = atoi(line.c_str());
	for (int i=1;i <= Ntc ;i++)
    {
		vector <string> in;
		if (! inp.eof() )
            getline (inp,line);
		string delim=" ";
		vector <INTVAR> TTwo;
        TTwo = tokenize_str(line,delim);
		INTVAR N = TTwo[0];
		INTVAR K = TTwo[1];

		for (int j = 0; j < N;j++)
		{
			getline (inp,line);
			in.push_back(line);
		}
		rotate(in);
		values v = calculate(in,K);
		if ( v == B )
			out<<"Case #"<<i<<": Blue"<<endl;
		else if ( v == R ) 
			out<<"Case #"<<i<<": Red"<<endl;
		else if ( v == BOTH ) 
			out<<"Case #"<<i<<": Both"<<endl;
		else if ( v == NEITHER ) 
			out<<"Case #"<<i<<": Neither"<<endl;
    }
out.close();
inp.close();
return 0;
}


