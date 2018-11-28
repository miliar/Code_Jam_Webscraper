#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int flip(int *p, int *q)
{
    int t = *q;
    while(q > p){
	*q = *(q-1);
	--q;
    }
    *p = t;
}

int main(int argc, char *argv[])
{
    ifstream in(argv[1]);
    while(in.good()){
	int n;
	in>>n;
	for (int i = 0; i < n; ++i)
	{
	    int a;
	    in>>a;
	    int b;
	    in>>b;
	    int rec = 0;
	    if(!in.good())
		return 0;
	    for (int j = a; j < b; ++j)
	    {
		int digits[7] = {0};
		int n = j;
		int count = 0;
		vector<int> added;
	    
		while(n>=10){
		    digits[count] = n % 10;
		    n /= 10;
		    count++;
		}
		digits[count] = n;
		count++;
		for (int p = 0, q = count -1; p < q ; ++p, --q)
		{
		    int t = digits[p];
		    digits[p] = digits[q];
		    digits[q] = t;
		}

		for (int q = 0; q < count-1; ++q)
		{
		    flip(digits, digits+count-1);

		    int m = 0;
		    int mul = 1;
		    for (int p = count - 1; p >= 0; --p)
		    {
			m += digits[p] * mul;
			mul *= 10;
		    }
		
		    if((m <= b) && (m >= a) && (m > j)){
			if(find(added.begin(), added.end(), m) == added.end()){
			    added.push_back(m);
			    rec++;
			}
		    }
		}
	    }
	    cout<<"Case #"<<i+1<<": "<<rec<<endl;
	}
    }
    return 0;
}
