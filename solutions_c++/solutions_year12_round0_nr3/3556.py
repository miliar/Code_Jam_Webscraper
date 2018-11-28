#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<sstream>
#include<map>
#include<string>
#include<algorithm>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<cmath>
#include<math.h>


using namespace std;

void print_result(int i, int A, int B)
{
	cout<<"Case #"<< i<< ": ";
	int result = 0;

	int a[7];
	map<pair<int,int>,int> r_num;

	for (int num= A ; num<= B; num ++){
		int digit = 0;
		int c_num = num;
		while(c_num > 0)
		{ 
			a[digit] = c_num % 10; //for example number will be a2 a1 a0
			c_num = c_num /10;
			digit ++;
		}
		//recyle
		for (int j = 1; j <= digit-1  ; j ++) {	
			int temp = a[digit - 1];
			for (int k = digit-2; k >=0 ; k --)
			{
				a[k+1] = a[k];
			}
			a[0] = temp;

			// logic to check
			int sum =0;
			for (int t = 0; t < digit ; t ++) {
				sum = sum + a[t]* pow(10, double(t));

			}

			if ((sum > num) && (sum <= B))
		        
				r_num[make_pair(sum, num)] = 1;
		}
	}
	cout << r_num.size() << endl;
}

void main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int num_case, A, B;
    cin>>num_case;
		for(int i=1; i <= num_case; i++)
		{
			cin>>A;
			cin>>B;
            print_result(i, A, B);
		}
	}


