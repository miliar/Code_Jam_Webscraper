/*
 * Google Code Jam template :-)
 */

#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
//#include <ctype.h>
//#include <assert.h>
//#include <math.h>
//#include <set>
//#include <map>

using namespace std;

typedef unsigned idx;
typedef unsigned long long num;

#define logR 28 // R<=2^logR
#define maxGN 1010 //maximal group number

class rideInfo
{
    public:
	idx next;
	num count;
	rideInfo(const idx n=maxGN, const num c=0):next(n), count(c) {}
};

typedef rideInfo rideRow[maxGN];

rideRow rows[logR];

template<class T> void line2list(string &str, vector<T> &v)
{
    istringstream ss(str,istringstream::in);
    T t;
    while (ss >> t)
    {
	v.push_back(t);
    }
}

void combine(rideRow &tgt, const rideRow& A, const rideRow& B, const idx N)
    //combines A and B and puts the result into tgt, only considering first N columns
{
    rideRow temp;
    for(idx i=0; i<N; ++i)
    {
	temp[i].next = B[A[i].next].next;
	temp[i].count = A[i].count + B[A[i].next].count;
    }
    
    //copy result
    for(idx i=0; i<N; ++i) tgt[i]=temp[i];
}

void print(const rideRow& A, const idx N)
{
    for (idx i=0; i<N; ++i)
    {
	cerr << "[" << A[i].next << "," << A[i].count << "] ";
    }
    cerr << endl;
}

void solve(const idx t)
{
    num R, k;
    idx N;
    string line;
    vector<num> g;
    num temp;
    rideRow tr;

    cin >> R >> k >> N;
    getline(cin,line);
    getline(cin,line);
    line2list(line,g);

    for (idx i=0; i<N; ++i) tr[i]=rideInfo(i,0); //R=0 implies next is current and 0 people carried

    //compute rows
    //compute the first row
    for(idx i=0; i<N; ++i)
    {
	idx next = (i+1) % N;
	num count=g[i];
	while(count+g[next] <= k  &&  next != i)
	{
	    count += g[next];
	    next = (next+1) % N;
	}
	rows[0][i].next = next;
	rows[0][i].count = count;
	//cerr << 0 << ": "; print(rows[0],N);
    }
    //now the rest
    temp = 2;
    for(idx i=1; R >= temp; ++i, temp = temp << 1)
    {
	combine(rows[i], rows[i-1], rows[i-1], N);
	//cerr << i << ": "; print(rows[i],N);
    }

    //compute result
    temp = 1;
    for(idx i=0; R >= temp; ++i, temp = temp << 1)
    {
	if (R & temp)
	{
	    combine(tr, tr, rows[i], N);
	}
    }

    cout << "Case #" << t << ": " << tr[0].count << endl;
}

int main(void)
{
    idx T;

    cin >> T;
    for(idx t=1; t<=T; ++t) solve(t);

    return 0;
}
