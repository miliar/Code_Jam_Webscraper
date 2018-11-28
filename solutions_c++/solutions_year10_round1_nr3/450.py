#include <iostream>
#include <fstream>
#include <algorithm>
bool is_winning(int x, int y)
{
	if(x==y)
	{
		return false;
	}
	else if(x < 2*y)
	{
		return !is_winning(y, x-y);
	}
	int mod = x%y;
	if(mod==0)
	{
		return true;
	}
	else
	{
		return (is_winning(y, mod) || is_winning(y+ mod, y));
	}
}
long long solve(int x1, int x2, int y1, int y2)
{
	long long result =0;
	for(int i = x1; i <=x2;++i)
	{
		for(int j = y1; j<=y2;++j)
		{
			int a = i;
			int b=j;
			if(a< b)
				std::swap(a, b);
			if(is_winning(a,b))
			{
				result +=1;
			}
		}
	}
	return result;
}
int main(int argc, char* argv[])
{
        std::ifstream inf(argv[1]);
        int cases ;
        inf >> cases;
	
	for(int i =0 ; i < cases;++i)
	{
		int x1, x2, y1, y2;
		inf >> x1 >> x2 >> y1 >> y2;
		
		std::cout << "Case #" << i+ 1 << ": " <<  solve(x1, x2, y1, y2) << "\n";
	}
	return 0;
}
