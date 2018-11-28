
#ifndef _FUNC_H_
#define _FUNC_H_

#include <string>
#include <sstream>

namespace func
{
	// ������� �� ������ � �����
	int FromStrToInt(std::string const& str)
	{
		int num = 0;
		std::istringstream iss(str);
		iss >> num;
		return num;
	}
	// ������� �� ����� � ������
	std::string FromIntToStr(int value)
	{
		std::ostringstream oss;
		oss << value;
		return oss.str();
	}

	// ������� �� ����� � ������
	std::string FromIntToStr(long long value)
	{
		std::ostringstream oss;
		oss << value;
		return oss.str();
	}
}
#endif // _FUNC_H_