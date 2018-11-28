#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <iterator>

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

    // read input
    int L;
    f >> L;
    int D;
    f >> D;
    vector<string> words(D);
    int N;
    f >> N;
    vector< vector< set<char> > > alien(N);
    
    for(int i = 0; i < N; ++i)
    {
	alien[i].reserve(L);
    }

    
    string tmp;
    getline(f,tmp); // read endline
    for(int i = 0; i < D; ++i)
    {
        getline(f,tmp);
        words[i] = tmp;
    }
    
    // let's fill  vector< vector< set<char> > > :)
    for(int i = 0; i < N; ++i)
    {
         getline(f,tmp);
	 int l = 0; // l should be in [0..L[
         for(int j = 0; j < tmp.size(); ++j)
	 {
	    alien[i][l].clear();
	    switch (tmp[j])
	    {
		case '(' :
		    while( isalpha(tmp[++j]) )
		    {
		        alien[i][l].insert(tmp[j]);
		    }
		    ++l; break;
		case ')' :  // it shouldn't have happened but let's count with that case
		    break;
		default:
		    if (isalpha(tmp[j]) )
			alien[i][l++].insert(tmp[j]);
	    }
	 }
    }



    // do the work
    for(int i = 0; i < N; ++i)
    {
	int s = 0;
	for(int j = 0; j < D; ++j)
	{
	    int l;
	    for ( l = 0; l < L && alien[i][l].find(words[j][l]) != alien[i][l].end(); ++l)
	    {}
	    if (l == L)
		++s;
	}
    
        cout << "Case #" << i+1 << ": " << s << endl;
    }

    return 0;
}

