#include	<fstream>
#include	<cmath>
#include	<vector>
#include	<list>
#include	<algorithm>
#include	<map>
#include	<set>
#include	<climits>
#include	<utility>
#include	<deque>
#include	<queue>
#include	<stack>

using namespace	std;

ifstream	in("A-large.in");
ofstream	out("A-large.out");

long	arr[2000];

int	main(int argc, char** argv)
{
	__int64 N;
	__int64 P, K, L;
	__int64 i, j, k, n, m;
	__int64 res;
	bool	b;

	in >> N;
	for(k = 1; k <= N; ++k)
	{
		memset(arr, 0, sizeof(arr));
		res = 0;
		b = false;
		in >> P >> K >> L;
		for(i = 0; i < L; ++i)
			in >> arr[i];
		sort(arr, arr+L);
		i = L-1;
		for(n = 0; n < P; ++n)
		{
			for(m = 0; m < K; ++m)
			{
				res += arr[i]*(n+1);
				i--;
				if(i == -1)
				{
					b = true;
					break;
				}
			}
			if(b)
				break;
		}
		out << "Case #" << k << ": " << res << endl;
	}
	return	0;
}

//#include	<fstream>
//#include	<cmath>
//#include	<vector>
//#include	<list>
//#include	<algorithm>
//#include	<map>
//#include	<set>
//#include	<climits>
//#include	<utility>
//#include	<deque>
//#include	<queue>
//#include	<stack>
//#include	<string>
//
//using namespace	std;
//
//ifstream	in("input.txt");
//ofstream	out("output.txt");
//
//bool	b[50];
//
//class	Bignum
//{
//public:
//	char	digits[50];
//	int		lastdigit;
//	Bignum(string str = "");
//
//	Bignum	operator+(Bignum& num);
//	Bignum	operator-(Bignum& num);
//};
//
//Bignum::Bignum(string str)
//{
//	int i;
//
//	for(i = 0; i < str.size(); ++i)
//		digits[i] = (str[str.size()-i-1] - '0');
//	lastdigit = str.size()-1;
//}
//
//void	zero(Bignum& num)
//{
//	while((num.lastdigit > 0) && (num.digits[num.lastdigit] == 0))
//		num.lastdigit--;
//}
//
//Bignum	Bignum::operator+(Bignum& num)
//{
//	Bignum	res;
//	int i, carry;
//
//	res.lastdigit = max(lastdigit, num.lastdigit)+1;
//	for(i = 0, carry = 0; i <= res.lastdigit; ++i)
//	{
//		res.digits[i] = (char)(carry + digits[i] + num.digits[i])%10;
//		carry = (carry + digits[i] + num.digits[i])/10;
//	}
//	zero(res);
//	return	res;
//}
//
//Bignum	Bignum::operator-(Bignum& num)
//{
//	Bignum	res;
//	int borrow;
//	int i, v;
//
//	res.lastdigit = max(lastdigit, num.lastdigit);
//	borrow = 0;
//	for(i = 0; i <= res.lastdigit; ++i)
//	{
//		v = (digits[i] - borrow - num.digits[i]);
//		if(digits[i] > 0)
//			borrow = 0;
//		if(v < 0)
//		{
//			v += 10;
//			borrow = 1;
//		}
//		res.digits[i] = (char)v%10;
//	}
//	zero(res);
//	return	res;
//}

//vector<string>	vec;
//
//bool	checkstring(string str)
//{
//	int i;
//	int j;
//	int t;
//	t = 0;
//	int tt;
//	__int64	ttt = 0;
//
//	if(!(str[str.size()-1]-'0')%2)
//		return	true;
//	for(i = 0; i < str.size(); ++i)
//		t += str[i]-'0';
//	if(!t%3)
//		return	true;
//	t = 0;
//	tt = str[str.size()-1] - '0';
//	if(tt == 0 || tt == 5)
//		return	true;
//	for(i = str.size()-2, j = 0; i >= 0; --i)
//		ttt += (double)(pow((double)10, (double)j)*(str[i]-'0'));
//	t = 2*(str[str.size()-1]-'0');
//	if(!(ttt - t)%7)
//		return	true;
//	return	false;
//}
//
//
//int	main(int argc, char** argv)
//{
//	int N;
//	int i, j, k, l;
//	string	num;
//	int size;
//	long res;
//
//	in >> N;
//
//	bool	t = false;
//
//	for(k = 1; k <= N; ++k)
//	{
//		in >> num;
//		res = 0;
//		memset(b, false, sizeof(b));
//		size = num.size();
//		while(!b[size-1])
//		{
//			i = 0;
//			while(b[i])
//			{
//				b[i] = false;
//				i++;
//			}
//			b[i] = true;
//			l = 0;
//			vec.clear();
//			t = false;
//			for(i = 0; i < size-1; ++i)
//			{
//				if(b[i])
//				{
//					vec.push_back(string(num.begin()+l, num.begin()+i+1));
//					l = i+1;
//					t = true;
//				}
//			}
//			if(t)
//				vec.push_back(string(num.begin()+l, num.end()));
//
//		}		
//	}
//	return	0;
//}