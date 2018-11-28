#include <vector>
#include <iostream>

using namespace std;

int handle_case()
{
		int n, sum = 0;
		cin >> n;
		int i = 0; 
		vector<int> x, y;
		while( i < n )
		{
				int tmp;
				int j = 0;
				cin >> tmp;
				for( j = 0; j < x.size(); j++ )
				{
						if( tmp < x[j] ) break;	
				}
				x.insert(x.begin()+j, tmp);
				i++;
		}
		i = 0;
		while( i < n )
		{
				int tmp;
				int j = 0;
				cin >> tmp;
				for( j = 0; j < y.size(); j++ )
				{
						if( tmp < y[j] ) break;	
				}
				y.insert(y.begin()+j, tmp);
				i++;
		}
		
		for( i = 0; i < n; i++ )
		{
				sum += x[i]*y[n-i-1];
		}

		return sum;
}


int main()
{
	int case_nums;
	cin >> case_nums;

	for( int i = 0; i < case_nums; i++ )
	{
		cout << "Case #" << i+1 << ": " << handle_case() << endl;
	}
}
