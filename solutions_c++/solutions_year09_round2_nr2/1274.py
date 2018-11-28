#include <vector>
#include <string>
#include <iostream>
#include <memory.h>
#include <algorithm>
#include <stack>
#include <fstream>

using namespace std;


#define All(v) (v).begin(), (v).end()
#define ffor(i,n) for(int i=0; i<n; i++)
#define LL long long
#define LD long double
#define psh push_back
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))

string itoa (int n) {
 
        char * s = new char[45];
        string u;
 
        if (n < 0) { //turns n positive
                n = (-1 * n); 
                u = "-"; //adds '-' on result string
        }
 
        int i=0; //s counter
  
        do {
                s[i++]= n%10 + '0'; //conversion of each digit of n to char
                n -= n%10; //update n value
        }
 
        while ((n /= 10) > 0);
 
        for (int j = i-1; j >= 0; j--) { 
                u += s[j]; //building our string number
        }
 
        delete[] s; //free-up the memory!
        return u;
}

int main()
{
	int c;
	cin >> c;

	for(int i = 0; i < c; i++)
	{
		int num;
		cin >> num;

		string str	= itoa(num);

		int greater	= -1;
		sort(All(str));
		while(next_permutation(All(str)))
		{
			int r	= atoi(str.c_str());
			if(r > num && (r < greater || greater == -1))
				greater	= r;
		}
		str	+= "0";
		sort(All(str));
		while(next_permutation(All(str)))
		{
			int r	= atoi(str.c_str());
			if(r > num && (r < greater || greater == -1))
				greater	= r;
		}

		cout << "Case #" << i+1 << ": " <<  greater <<     endl;
	}
}
