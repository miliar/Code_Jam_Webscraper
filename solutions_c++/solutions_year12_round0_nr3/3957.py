#include <iostream>
#include <utility>

#include <boost/unordered_set.hpp>

#include <cinttypes>

#include <boost/assert.hpp>

namespace mine
{
	std::size_t digit_count(std::uint32_t x)
	{
		if (x==0)
			return 1;
		std::size_t c = 0;
		while (x>0)
		{
			++c;
			x /= 10;
		}
		return c;
	}
	inline std::uint32_t tenpow(std::size_t y)
	{
		const static std::uint32_t pow[] =
		{
			1,              // 0
			10,             // 1
			100,            // 2
			1000,           // 3
			1000*10,        // 4
			1000*100,       // 5
			1000*1000,      // 6
			1000*1000*10,   // 7
			1000*1000*100,  // 8
			1000*1000*1000  // 9
		};
		return pow[y];
	}
	inline std::uint32_t mindigit(std::size_t digit)
	{
		BOOST_ASSERT(digit>1);
		return tenpow(digit-1);
	}
	inline std::uint32_t maxdigit(std::size_t digit)
	{
		return mindigit(digit+1)-1;
	}
	inline bool rotate_left(std::uint32_t &x, std::uint32_t digits)
	{
		std::uint32_t d = x%10;
		x /= 10;
		x += tenpow(digits-1)*d;
		return d;
	}
	std::size_t simple_count(std::uint32_t a, std::uint32_t b, std::size_t digits)
	{
		std::size_t cnt = 0;
		for (std::uint32_t i = a; i<=b; ++i)
		{
			std::set<std::size_t> numbers;
			std::uint32_t x = i;
			for (std::size_t j = 1; j<digits; ++j)
			{
				if (rotate_left(x, digits) && a<=x && x<i)
					numbers.insert(x);
			}
			cnt += numbers.size();
		}
		return cnt;
	}
	inline std::size_t predefined_digit_count(std::size_t digits)
	{
		constexpr std::size_t npos = std::numeric_limits<std::size_t>::max();
		static const std::size_t predef[] =
		{
			npos,    // 0
			npos,    // 1
			36,      // 2
			801,     // 3
			12060,   // 4
			161982,  // 5
			2023578, // 6
			npos,    // 7
			npos     // 8
		};
		if (predef[digits]==npos)
		{
			std::size_t ret = simple_count(mindigit(digits), maxdigit(digits), digits);
			std::cerr<<digits<<": "<<ret<<std::endl;
			return ret;
		}
		else
			return predef[digits];
	}
	std::size_t count(std::uint32_t a, std::uint32_t b)
	{
		BOOST_ASSERT(a<=b);
		std::size_t acnt = digit_count(a);
		std::size_t bcnt = digit_count(b);
#if 1
		if (acnt<bcnt)
		{
			std::size_t cnt = simple_count(a, maxdigit(acnt), acnt);
			for (std::size_t i = acnt+1; i<bcnt; ++i)
				cnt += predefined_digit_count(i);
			cnt += simple_count(mindigit(bcnt), b, bcnt);
			return cnt;
		}
		else
		{
			BOOST_ASSERT(acnt==bcnt);
			return simple_count(a, b, bcnt);
		}
#else
		for (std::size_t i = acnt; i<bcnt; ++i)
		{
			std::uint32_t end = maxdigit(i);
			cnt += simple_count(begin, end, i);
			begin = end+1;
		}
		cnt += simple_count(begin, b, bcnt);
		return cnt;
#endif
	}
	bool run_tests()
	{
		BOOST_ASSERT(digit_count(0)==1);
		BOOST_ASSERT(digit_count(1)==1);
		BOOST_ASSERT(digit_count(9)==1);
		BOOST_ASSERT(digit_count(10)==2);
		BOOST_ASSERT(digit_count(19)==2);
		BOOST_ASSERT(digit_count(91)==2);
		BOOST_ASSERT(digit_count(100)==3);
		BOOST_ASSERT(digit_count(999)==3);
		//BOOST_ASSERT(mindigit(1)==0);
		BOOST_ASSERT(mindigit(2)==10);
		BOOST_ASSERT(mindigit(3)==100);
		BOOST_ASSERT(maxdigit(1)==9);
		BOOST_ASSERT(maxdigit(2)==99);
		BOOST_ASSERT(maxdigit(3)==999);
		std::uint32_t x = 123;
		BOOST_ASSERT(rotate_left(x, 3));
		BOOST_ASSERT(x==312);
		x = 1;
		BOOST_ASSERT(rotate_left(x, 1));
		BOOST_ASSERT(x==1);
		x = 101;
		BOOST_ASSERT(rotate_left(x, 3));
		BOOST_ASSERT(x==110);
		BOOST_ASSERT(!rotate_left(x, 3));
		BOOST_ASSERT(x==11);
		BOOST_ASSERT(rotate_left(x, 3));
		BOOST_ASSERT(x==101);
		return true;
	}
}

int main()
{
	BOOST_ASSERT(mine::run_tests());
	std::size_t tests;
	std::cin>>tests;
	std::vector<std::pair<std::uint32_t, std::uint32_t>> cases(tests);
	std::vector<std::size_t> result(tests);
	for (std::size_t test = 0; test<tests; ++test)
		std::cin>>cases[test].first>>cases[test].second;
	#pragma omp parallel for
	for (std::size_t test = 0; test<tests; ++test)
		result[test] = mine::count(cases[test].first, cases[test].second);
	for (std::size_t test = 0; test<tests; ++test)
		std::cout<<"Case #"<<test+1<<": "<<result[test]<<std::endl;
}

