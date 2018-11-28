#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iostream>
#include <set>

using namespace std;

vector<long long> tokenize_str(const string & str,
							const string & delims)
{
	using namespace std;
	// Skip delims at beginning, find start of first token
	string::size_type lastPos = str.find_first_not_of(delims, 0);
	// Find next delimiter @ end of token
	string::size_type pos     = str.find_first_of(delims, lastPos);

	// output vector
	vector<long long> tokens;

	while (string::npos != pos || string::npos != lastPos)
	{
		// Found a token, add it to the vector.
		string temp = str.substr(lastPos, pos - lastPos);
		long long tempint = atoi(temp.c_str());
		tokens.push_back(tempint);
		// Skip delims.  Note the "not_of". this is beginning of token
		lastPos = str.find_first_not_of(delims, pos);
		// Find next delimiter at end of token.
		pos     = str.find_first_of(delims, lastPos);
	}

	return tokens;
}
#define TOTAL_GROUP_SIZE 1001
long long group_data[TOTAL_GROUP_SIZE];
long long temp_data1[TOTAL_GROUP_SIZE];
long long temp_data2[TOTAL_GROUP_SIZE];
int main()
{
	string line;
	ifstream in("C:/Documents and Settings/sxv23/My Documents/C-large.in.txt");
	ofstream out("C:/Documents and Settings/sxv23/My Documents/C-large.out.txt",ios::out);
    getline (in,line);

	int Ntc = atoi(line.c_str());
	for (int i=1;i <= Ntc ;i++)
    {
		memset(group_data,0,sizeof(group_data));
		memset(temp_data1,0,sizeof(temp_data1));
		memset(temp_data2,0,sizeof(temp_data2));
        getline (in,line);
		string delim=" ";
		vector <long long> TTwo;
        TTwo = tokenize_str(line,delim);
		long long R = TTwo[0];
		long long k = TTwo[1];
		long long N = TTwo[2];
		long long rcount = 0;
		getline (in,line);
		vector <long long> T3;
		T3 = tokenize_str(line,delim);
		for(int a=0;a<N;a++)
			group_data[a]=T3[a];
		int pos=0;
		long long totalsum=0;
		bool loopDetected=false;
		while (rcount < R)
		{
			rcount++;
			long long sum =0;
			int gcount=0;
			while((sum+group_data[pos])<=k && gcount<N)
			{
				gcount++;
				sum=sum+group_data[pos];
				pos++;
				if(pos==N)
					pos=0;
			}
			totalsum=totalsum+sum;
			if ( !loopDetected )
			{
				if (!temp_data1[pos])
				{
					temp_data1[pos]=totalsum;
					temp_data2[pos]=rcount;
				}
				else
				{
					long long diffCount = rcount-temp_data2[pos];
					long long rem=(R-rcount)%diffCount;
					long long fact=(R-rcount)/diffCount;
					totalsum=totalsum+((totalsum-temp_data1[pos])*fact);
					rcount=R-rem;
					loopDetected = true;
				}
			}
		}
		out<<"Case #"<<i<<": "<<totalsum<<endl;
    }
out.close();
in.close();
return 0;
}