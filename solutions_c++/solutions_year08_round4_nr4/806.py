#include <cstdio>
#include <iostream>
#include <vector>
#include <fstream>
#include <cassert>
#include <string>
#include <algorithm>
#include <iomanip>
#include <functional>
#include <map>
#include <set>
#include <list>
#include <deque>
using namespace std;

int BreadCalc( const vector<int> & v, const string & s)
{
	size_t base = 0;
	string tmp = s;
	while( base < s.size() )
	{
		for( size_t i = 0; i < v.size(); ++i )
		{
			tmp[ i+base] = s[v[i]+base];
		}
		base += v.size();
	}

	int length = 1;
	char lastChar = tmp[0];
	for( size_t i = 1; i < tmp.size(); ++i )
	{
		if( tmp[i] != lastChar )
		{
			length++;
			lastChar = tmp[i];
		}
	}
	return length;
}

int BreadMin(int n, const string & s)
{
	assert( s.size() % n == 0 );

  /*Init*/
	int a[50];
	int b[50];
    int max=n,arrow=-1,i,mobile=1;
    a[0]=a[n+1]=100000000;a[n+2]=-100000000;
    for(i=1;i<=n;i++){a[i]=i;b[i]=-1;}
    

	int minRLE = 2147483647;
    while(mobile)
    {
		vector<int> v;
        for(i=1;i<=n;i++)
		{
			v.push_back( a[i]-1);
		}

		int ret = BreadCalc(v,s) ;
		minRLE = min(minRLE, ret );

                
        /*Find the largest mobile integer max*/
        mobile=0;
        max=n+2;
        for(i=1;i<=n;i++)
        if(a[i]>a[max]&&a[i+b[i]]<a[i])
        {
            max=i;
            mobile=1;
            arrow=b[max];
        }    
        
        /*Switch max and the adjacent integer its arrow points to*/ 
        i=a[max+arrow];
        a[max+arrow]=a[max];
        a[max]=i;
        i=b[max+arrow];
        b[max+arrow]=b[max];
        b[max]=i;
        max=max+arrow;
        
        /*Switch the direction of all integer i with i>max*/
        for(i=1;i<=n;i++)if(a[i]>a[max])b[i]*=-1;
    }

//	delete []a;
//	delete []b;
	return minRLE;
}

int main(int argc, char* argv[])
{

	if ( argc < 3 )
	{
		cout << "Round1C inputfile outputfile" << endl;
		return 1;
	}

	ifstream in(argv[1],ios::in);
	ofstream out(argv[2]);
	if( !in )
	{
		cout << "can't open input file" << endl;
		return 1;
	}

	if( !out )
	{
		cout << "can't open output file" << endl;
		return 1;
	}
	

	int totalCase = 0;
	in>> totalCase;
//	cout << totalCase << endl;
	assert( totalCase > 0 );

	for( int i = 1; i <= totalCase; ++i )
	{
		int k;
		in >> k;
		string s;
		in >> s;
		out << "Case #" << i <<": " << BreadMin(k,s) << endl;
	}
	return 0;
}

