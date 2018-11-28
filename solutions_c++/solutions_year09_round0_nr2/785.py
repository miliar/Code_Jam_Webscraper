#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

typedef vector<vector<int> > vvi_t;
typedef vector<vector<char> > vvc_t;
typedef map<int, int> mii_t;


template <typename T>
ostream &
operator<<(ostream &out, vector<vector<T> > const &data)
{
    for (int i = 0; i < data.size(); ++i)
    {
	for (int j = 0; j < data[i].size(); ++j)
	{
	    out<<data[i][j];
	    if (j != data[i].size() - 1)
		out<<" ";
	}
	out<<"\n";
    }
    return out;
}


bool
valid(vvi_t &in, int i, int j)
{
    return i >= 0 && j >= 0 && i < in.size() && j < in[0].size();
}

void
find_min_neighbour(vvi_t &in, vvc_t& out, int i, int j, int &ni, int &nj, int &min_altitude)
{
    if (valid(in, i, j) && in[i][j] <= min_altitude)
    {
	ni = i;
	nj = j;
	min_altitude = in[i][j];
    }
}




char
fill_solution(vvi_t &in, vvc_t& out, char next_char, int i, int j)
{
    if (out[i][j] != 'X')
	return out[i][j];

    cerr<<"fill_solution("<<i<<", "<<j<<", "<<next_char<<")\n";

    int ni = -1 , nj = -1;
    int min_altitude = 20000;

    /* South */
    find_min_neighbour(in, out, i+1, j, ni, nj, min_altitude);

    /* East */
    find_min_neighbour(in, out, i, j+1, ni, nj, min_altitude);

    /* West */
    find_min_neighbour(in, out, i, j-1, ni, nj, min_altitude);

    /* North */
    find_min_neighbour(in, out, i-1, j, ni, nj, min_altitude);

    cerr<<"Min neighbour: "<<ni<<", "<<nj<<endl;

    if (min_altitude < in[i][j])
    {
	cerr<<"Accepted min neighbour with value: "<<in[ni][nj]<<endl;

	/* This means ni != -1 */
	/* What is the basin label of this minimum neighbour? */
	char mn_basin = out[ni][nj];
	if (mn_basin != 'X')
	{
	    /* Already assigned to someone. Assign this guy with the same and
	     * return the same
	     */
	    out[i][j] = mn_basin;
	    return mn_basin;
	}
	else
	{
	    /* Unassigned. Try with it's neighbours */
	    char _nc = fill_solution(in, out, next_char, ni, nj);
	    out[i][j] = _nc;
	    return _nc;
	}
    }
    else
    {
	/* We may have found a min neighbour, but that neighbour isn't < the
	 * current node, so we can't proceed further
	 */

	cerr<<"At ("<<i<<", "<<j<<"). Can not proceed further. Filling with: "<<next_char<<endl;

	/* Could not find any un-visited neighbour. Fill in with next_char */
	out[i][j] = next_char;
	return next_char;
    }
}


void
process_test_case(int n)
{
    int h, w;
    cin>>h>>w;

    vvi_t terrain(h, vector<int>(w, 0));
    vvc_t out(h, vector<char>(w, 'X'));
    char nc = 'a';

    // cout<<out<<endl;

    for (int i = 0; i < h; ++i)
    {
	for (int j = 0; j < w; ++j)
	{
	    cin>>terrain[i][j];
	}
    }

    for (int i = 0; i < h; ++i)
    {
	for (int j = 0; j < w; ++j)
	{
	    if (out[i][j] == 'X')
	    {
		char _nc = fill_solution(terrain, out, nc, i, j);
		cerr<<"fill_solution("<<i<<", "<<j<<", "<<nc<<") == "<<_nc<<endl;
		if (_nc == nc)
		    ++nc;
	    }
	}
    }

    cout<<"Case #"<<n<<":\n"<<out;

}


int
main()
{
    int t = 0;
    cin>>t;

    for (int i = 0; i < t; ++i)
    {
	process_test_case(i+1);
    }
}
