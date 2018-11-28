/*
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
int main()
{
	ofstream out("res.txt");

	int t, i, j, n, cs=0;
	int nums[21];
	int count;
	cin >> t;
	while(cs++ < t)
	{
		cin >> n;
		count = 0;
		while(n > 0)
		{
			nums[count] = n%10;
			n /= 10;
			count++;
		}

		bool found;
		int mins, mini;
		for(i=1; i<count; i++)
		{
			found = false;
			mins = 10;
			mini = 0;
			for(j=0; j<i; j++)
			{
				if(nums[j] > nums[i] && mins > nums[j])
				{
					mins = nums[j];
					found = true;
					mini = j;
				}
			}
			if(found)
				break;
		}
		int res = 0;
		if(found)
		{
			int temp = nums[mini];
			nums[mini] = nums[i];
			nums[i] = temp;

			for(i=0; i<count; i++)
			{
				res *= 10;
				res += nums[i];
			}
		}
		else
		{
			sort(nums, nums+count);
			for(i=0; i<count; i++)
			{
				if(nums[i] != 0)
				{
					res = nums[i] * 10;
					break;
				}
			}
			for(i=1; i<count; i++)
			{
				res *= 10;
				res += nums[i]; 
			}

		}
		out << "Case #" << cs << ": " << res << endl;

	}
	out.close();
	return 0;
}*/

#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
int main()
{
	ofstream out("res.txt");

	int t, i, j, n, cs=0;
	int nums[11];
	int temps[11];
	int count;
	cin >> t;
	while(cs++ < t)
	{
		cin >> n;
		int m = n;
		count = 0;
		memset(nums, 0, 11*sizeof(int));
		while(m>0)
		{
			nums[m%10]++;
			m /= 10;
		}
		n++;
		int res;
		while(1)
		{
			memcpy(temps, nums, sizeof(int)*11);	
			m = n;
			if(m== 150)
			{
				int xx = 0;
			}
			while(m>0)
			{
				int mm = m%10;
				temps[mm]--;
				if(mm>0 && temps[mm] < 0)
					break;
				m /= 10;				
			}
			if(m==0)
			{
				for(i=1; i<10; i++)
				{
					m+=temps[i];
				}
				if(m==0)
				{
					res = n;
					break;
				}
			}
			n++;
			
		}
		out << "Case #" << cs << ": " << res << endl;

	}
	out.close();
	return 0;
}