#include <string>
#include <iostream>

bool Add1(int* signs, int N)
{
	int j = 0;
	while (signs[j] == 2 && j < N-1)
	{
		signs[j++] = 0;
	}
	if (j != N-1) {
		signs[j]++;
		return true;
	}
	else
	{
		return false;
	}
}

bool IsUgly(long long K)
{
	return !(K % 2) || !(K%3) || !(K%5) || !(K%7);
}

void ProcessCurSign(long long& res, long long tmp, int cur)
{
	if (cur == 1)
	{
		res+=tmp;
	}
	else if (cur == 2)
	{
		res-=tmp;
	}
	else/*Never was cursign*/
	{
		res = tmp;
	}
}

long long ConvertToNum(std::string s, int* signs)
{
	long long res = 0;
	long long tmp = 0;
	int cursign = 0;
	tmp = s[0]-'0';
	for (unsigned int i = 1; i < s.length(); ++i)
	{
		if (signs[i-1] > 0 ) /*plus*/
		{
			ProcessCurSign(res,tmp,cursign);
			cursign = signs[i-1];
			tmp = 0;
		}
		/* nothing*/
		{
			tmp*=10;
			tmp+=s[i]-'0';
		}
	}
	ProcessCurSign(res,tmp,cursign);
/*	for (int i = 0; i < s.length(); ++i)
	{
		if (signs[i] == 1) std::cout<<"+";
		if (signs[i] == 2) std::cout<<"-";
		if (signs[i] == 0) std::cout<<"0";
	}
	std::cout<<" "<<res<<std::endl;*/
	return res;
}

long long DoTest(std::istream& f, int TestNum)
{
	std::string s;
	f>>s;
	int N = s.length();
	long long res = 0;
	long long num;
	int signs[14] = {0};
	num = _atoi64(s.c_str());
	if (IsUgly(num)) res++;
	while (Add1(signs,N))
	{
		num = ConvertToNum(s,signs);
		if (IsUgly(num)) res++;
	}
	std::cout<<"Case #"<<TestNum<<": "<<res<<std::endl;
	return 0;
}

int main(int argc, char** argv)
{
	int T;
//	std::ifstream f("A.in");
	std::cin>>T;
	for (int i = 0; i < T; ++i)
	{
		DoTest(std::cin, i+1);
	}
}
