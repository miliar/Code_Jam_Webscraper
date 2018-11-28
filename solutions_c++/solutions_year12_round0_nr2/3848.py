# include <iostream>
using namespace std;

int main()
{
	int T, n, s, p, i, sum, count, k;
	
	k = 1;
	cin >> T;
	while (T--)
	{
		cin >> n >> s >> p;
		count = 0;
		
		for (i = 0; i < n; ++i)
		{
			cin >> sum;
			
			if ((sum + 1) % 3 == 0  &&  (sum + 1) / 3 >= p)
			{	++count;	continue;	}
			
			if (sum % 3 == 0  &&  (sum / 3) >= p)
			{	++count;	continue;	}
			
			if ((sum + 2) % 3 == 0  &&  (sum + 2) / 3 >= p)
			{	++count;	continue;	}
			
			if (s > 0  &&  sum < 29  &&  sum > 1)
			{
				if ((sum + 4) % 3 == 0  &&  (sum + 4) / 3 >= p)
				{	++count;	--s;	continue;	}
				
				if ((sum + 3) % 3 == 0  &&  (sum + 3) / 3 >= p)
				{	++count;	--s;	continue;	}
				
				if ((sum + 2) % 3 == 0  &&  (sum + 2) / 3 >= p)
				{	++count;	--s;	continue;	}
			}
		}
		
		cout << "Case #" << k << ": " << count << "\n";
		++k;
	}
	
	return 0;
}
		
				
		
