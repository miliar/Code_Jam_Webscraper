#include <fstream>
#include <vector>
#include <iostream>
#include <limits>
#include <queue>
#include <algorithm>

std::string cvt_binary(unsigned int input)
{
	if(input == 0)
	{
		return "0";
	}
	std::string result;
	for(int i = std::numeric_limits<unsigned int>::digits - 1; i >= 0; --i)
	{
		if(input & (1 << i))
		{
			result += "1";
		}
		else
		{
			if(!result.empty())
			{
				result += "0";
			}
		}
	}
	if(result.size() < 20)
	{
		std::string temp;
		for(int i=20; i>result.size(); --i)
		{
			temp+="0";
		}
		result=temp+result;
	}
	return result;
}

std::string sum(std::string x, std::string y)
{
	std::string result = "00000000000000000000";
	for(int i=0; i<20; ++i)
	{
		if( (x[i]=='1' && y[i]=='0' ) || (y[i]=='1' && x[i]=='0') )
		{
			result[i]='1';
		}
		else
		{
			result[i]='0';
		}
	}
	return result;
}

unsigned int to_int(std::string x)
{
	int result=0;
	int kerroin=524288;
	for(int i=0; i<20; ++i)
	{
		if(x[i]=='1')
		{
			result+=kerroin;
		}
		kerroin=kerroin/2;
	}
	return result;
}

int main()
{
	std::ifstream in("candy.in");
	std::ofstream out("candy.out");
	int T;
	in >> T;
	
	for(int i=1; i<=T; ++i)
	{
		out << "Case #" << i << ": ";
		std::cout << "Case #" << i << ": ";
		std::vector<int> karkit;
		std::vector<std::string> candies;

		int N;
		in >> N;
		for(int i=0; i<N; ++i)
		{
			int temp;
			in >> temp;
			karkit.push_back(temp);
		}
		std::sort(karkit.begin(), karkit.end());
		for(int i=0; i<N; ++i)
		{
			candies.push_back( cvt_binary(karkit[i]) );
		}
		
		std::string temp="00000000000000000000";
		
		for(int i=0; i<N; ++i)
		{
			temp=sum(temp, candies[i]);
		}
		
		bool able=false;
		if(temp=="00000000000000000000")
		{
			able=true;
		}
		
		if(able)
		{
			int result=0;
			for(int i=1; i<karkit.size(); ++i)
			{
				result+=karkit[i];
			}
			std::cout << result << std::endl;
			out << result << std::endl;
		}
		else
		{
			std::cout << "NO" << std::endl;
			out << "NO" << std::endl;
		}
		
	}
	
}







