#include<iostream>
#include<iterator>
#include<algorithm>
#include<string>
#include<sstream>
#include<numeric>
#include<vector>
#include<deque>
#include<set>
#include<map>
using namespace std;

#include <afxdisp.h>
#include<afx.h>

typedef vector<int> vi;
//typedef vector<int>::iterator viit;	
//typedef vector<int>::reverse_iterator rviit;		

typedef vector<char> vc;
//typedef vector<char>::iterator vcit;	
//typedef vector<char>::reverse_iterator rvcit;		

typedef vector<string> vs;
//typedef vector<string>::iterator vsit;	
//typedef vector<string>::reverse_iterator rvsit;		

typedef vector<bool> vb;
//typedef vector<bool>::iterator vbit;	
//typedef vector<bool>::reverse_iterator rvbit;		
typedef vector<double> vd;

ostream_iterator<int> oi(cout, " ");
ostream_iterator<char> oc(cout, " ");
ostream_iterator<string> os(cout, " ");
ostream_iterator<bool> ob(cout, " ");
ostream_iterator<double> od(cout," ");

stringstream dss;
ostream_iterator<int> doi(dss, " ");
ostream_iterator<char> doc(dss, " ");
ostream_iterator<string> dos(dss, " ");
ostream_iterator<bool> dob(dss, " ");

#define RR 5
#define CC 5
#define R 5
#define BS 256
 
#define sp " "
#define sp1 <<" "<<
#define nl <<endl
#define dot dss<<
#define dnll dss<<endl;

#define ot cout<<
#define nll cout<<endl;

#define For(i,a,b) for ( i=(a); i < b; ++i)
#define Ford(i,a,b) for (i=(a); i >= b; --i)
#define Rep(i,n) for (i=(0); i < n; ++i)
#define Repd(i,n) for (i=((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

#define IMRAN
