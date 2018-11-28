#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;

static int digs[10];
static int curdigs[10];

bool eqdigs()
{
	int i;
	
	for (i=1; i<10; ++i)
		if (digs[i] != curdigs[i])
			return false;
	
	return true;
}

void getdigs(unsigned long n, int opt=1)
{		
	bool lastdig = false;
	int m;
	
	while (1)
	{
		if (n < 10) lastdig = true;
		m = n%10;
		if (opt)
			++digs[m];
		else
			++curdigs[m];
		n /= 10;
		if (lastdig) break;
	}
}


int main()
{
	int t;
	unsigned long n, n1;
	int i,j,k;
	unsigned long next;
	int m;
	bool lastdig;
	
	cin >> t;
	
	for (i=1; i<=t; ++i)
	{
		cin >> n;
		
		for (j=0; j<10; ++j)
			digs[j] = 0;
		
		getdigs(n);
		next = n;				
		
		while (!eqdigs())
		{
			for (j=0; j<10; ++j)
				curdigs[j] = 0;
			getdigs(++next, 0);
		}
				
		cout << "Case #" << i << ": " << next << endl;
	}
}
