#include <iostream>
#include <vector>
#include <stdio.h>
void solve(int q_no)
{
	std::cout << "Case #" << q_no << ":\n";
	std::string data[100];
	int size ;
	double owp[100];
	std::cin >> size;
	for(int i =0; i < size;++i)
	{
		std::cin >> data[i];
	}
	
	for(int i =0; i < size;++i)
	{
		int count =0;
		owp[i] =0;
		for(int x =0; x < size; ++x)
		{
			int total =0;
			int win =0;
			if(data[i][x]=='.')
				continue;
			for(int y =0; y < size;++y)
			{
				if(y==i)
					continue;
				if(data[x][y] != '.')
				{
					total +=1;
					if(data[x][y] == '1')
						win+=1;
				}

			}
			count +=1;
			owp[i] += double(win) / double(total);
		}
		owp[i] = owp[i] / double(count);
	}

	for(int i = 0; i < size; ++i)
	{
		double result =owp[i] /2.0;
		int total=0;
		int win =0;
		for(int j =0; j < size;++j)
		{
			if(data[i][j] !='.')
			{
				total +=1;
				if(data[i][j]=='1')
					win +=1;
			}
		}
		result += double(win) / double(total * 4);

		double oowp = 0;
		for(int j =0; j < size;++j)
		{
			if(data[i][j] !='.')
				oowp += owp[j];
		}
		result += oowp/ double(total * 4);
		printf("%.8f\n", result);
	}

}

int main(void)
{
	int count;
	std::cin >> count;
	for(int i =0; i < count;++i)
	{
		solve(i+1);
	}
	return 0;
}
