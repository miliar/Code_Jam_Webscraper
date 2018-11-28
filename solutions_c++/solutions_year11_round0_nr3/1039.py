#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <stack>
#include <string>
using namespace std;


typedef long long cybers ;


#define MAX_SIZE 1000
#define INFINITY 1000000000
#define PI 3.1415926

#define PRT_F(a,b) cout<<"Case #"<<a<<": "<<b<<endl;


int main()
{
	char tchar;
	int tvalue;

	freopen("C-large.in","rt",stdin); freopen("C-large.out","wt",stdout);
	int ARRAY_OF_PARTS[1000];
	int amount = 0;
	cin>>amount;
	int p = 0;
	
	while (p<amount)
		{
		int arraysize  = 0;
		int sum = 0;
		int min = INFINITY;
		int sumxor  = 0;
		cin>>arraysize;
		for (int i=0;i<arraysize;i++)
			{
				cin>>ARRAY_OF_PARTS[i];
				sum +=ARRAY_OF_PARTS[i];
				sumxor ^= ARRAY_OF_PARTS[i];
				if (ARRAY_OF_PARTS[i]<min) min=ARRAY_OF_PARTS[i];

			}
		
		p++;
		cout<<"Case #"<<p<<": ";
		if (sumxor!=0) 
			cout<<"NO";
		else
			cout<<sum-min;
		cout<<endl;
		}
}

