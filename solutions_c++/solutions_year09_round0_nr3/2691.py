#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <iterator>
#include <iomanip>

const std::string Jam = "welcome to code jam";

class not_in_jam
{
    public:
	bool operator()(char c)
	{	
	    return ( find(Jam.begin(), Jam.end(), c) == Jam.end() );
	}
};

void table_fill(std::vector< std::vector<int> > &table, const std::string& str);

int nagyobbak(std::vector< std::vector<int> > &table, const int i, const int j);

using namespace std;

int main(int argc, char* argv[])
{
    if (argc != 2)
    {
	cerr << "use: " << argv[0] << " <input> " << endl;
	exit(1);
    }
    
    ifstream f(argv[1]);
    if (!f)
    {
	cerr << "file error" << endl;
	exit(1);
    }

    int n;
    f >> n;
    
    string tmp;
    getline(f,tmp); // read endline
    for(int i = 0; i < n; ++i)
    {
	getline(f, tmp);
	string::iterator new_end;
	new_end = remove_if(tmp.begin(), tmp.end(), not_in_jam() );
	
	tmp.erase(new_end, tmp.end() );
	
	vector< vector<int> > table(Jam.size() );
	
	table_fill(table, tmp);
	
	int sum = 0;
	for(int i = 0; i < table[0].size(); ++i)
	{
	    sum += (nagyobbak(table, 0, table[0][i]) ) % 10000;
	}

	cout << "Case #" << i+1 << ": " << setfill('0') << setw(4) <<  sum << endl;
	
    }

    return 0;
}

void table_fill(std::vector< std::vector<int> > &table, const string& str)
{
    for(int i =0; i < str.size(); ++i)
    {
	for(int j=0; j < Jam.size(); ++j)
	{
	    bool valid = true;
	    if(Jam[j] == str[i])
	    {
		int l, k = 0;
		for(l = 0; l < i && k < j; ++l)
		{
		    if(Jam[k] == str[l])
		    { 
			++k;
		    }
		}
		if(k != j)
		    valid = false;
		    
		k = j+1;
		for(l = i + 1; l < str.size() && k < Jam.size(); ++l)
		{
		    if(Jam[k] == str[l])
		    {
			++k;
		    }
		}
		if( k != Jam.size() ){
		    valid = false;
		}
		
		if (valid)
		    table[j].push_back(i);
		
	    }
	}
    }

}

int nagyobbak(std::vector< std::vector<int> > &table, const int x, const int y)
{
    int sum = 0;
    if(x+1 == table.size() - 1 )
    {
	for (int i = 0; i < table[x+1].size(); ++i)
	{
	    if (y < table[x+1][i])
		sum += 1;
	}
	return sum;
    }
    
    for(int i = 0; i < table[x+1].size(); ++i)
    {
	if(y < table[x+1][i] )
	    sum += (nagyobbak(table,x+1,table[x+1][i]) ) % 10000;
    }
    return sum;
}


















