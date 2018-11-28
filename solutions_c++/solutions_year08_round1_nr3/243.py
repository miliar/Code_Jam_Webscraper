
#include <iostream>
#include <list>
#include <fstream>
#include <stack>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <stack>
#include <ctime>
#include <set>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

class BigDecimal{
public:
	BigDecimal()
	{
		baseNum = "0";
		floatPos = 0;
	}
	BigDecimal(string num)
	{
		int k = num.find('.');
		if(k == -1)
		{
			floatPos = 0;
			baseNum = num;
		}else{
			floatPos = num.length() - 1 - k;
			baseNum = num.erase(k, 1);
		}
		trimZero();
	}
	BigDecimal(string baseNum, int floatPos)
	{
		this->baseNum = baseNum;
		this->floatPos = floatPos;
		trimZero();
	}
	BigDecimal add(BigDecimal bigD)
	{
		string oneBaseNum = bigD.getBaseNum();
		int oneFloat = bigD.getFloatPos();
		string twoBaseNum = getBaseNum();
		int twoFloat = getFloatPos();
		//结果
		string baseNum = "";
		int floatPos = max(oneFloat, twoFloat);
		//两个数字齐次
		int i, j;

		for (i=0; i<abs(oneFloat - twoFloat); i++)
		{
			if (oneFloat < twoFloat)
			{
				oneBaseNum += "0";
			}else
				twoBaseNum += "0";
		}
		//开始加法操作
		i = oneBaseNum.length() - 1; j = twoBaseNum.length() - 1;
		int addIn = 0; //加法进位
		while (true)
		{
			int bit = 0;
			if (i>= 0 && j >= 0 )
			{
				bit = oneBaseNum[i] - '0' + twoBaseNum[j] - '0' + addIn;
				addIn = bit / 10;
				bit %= 10;
				baseNum = (char)(bit + '0') + baseNum;
				i--; j--;
			}else if (i>=0)
			{
				bit = oneBaseNum[i] - '0' + addIn;
				addIn = bit / 10;
				bit %= 10;
				baseNum = (char)(bit + '0') + baseNum;
				i--;
			}else if (j >= 0)
			{
				bit = twoBaseNum[j] - '0' + addIn;
				addIn = bit / 10;
				bit %= 10;
				baseNum = (char)(bit + '0') + baseNum;
				j--;
			}else break;
		}
		//cout << "Run here1" << endl;
		while (addIn > 0)
		{
			int bit = addIn % 10;
			addIn /= 10;
			baseNum = (char)(bit + '0') + baseNum;
		}
		return BigDecimal(baseNum, floatPos);
	}
	BigDecimal multiply(BigDecimal bigD)
	{
		string oneBaseNum = bigD.getBaseNum();
		int oneFloat = bigD.getFloatPos();
		string twoBaseNum = getBaseNum();
		int twoFloat = getFloatPos();
		//结果
		BigDecimal res;
		//按位乘法
		for(int i=oneBaseNum.length() - 1; i>=0; i--)
		{
			if (oneBaseNum[i] == 0)
			{
				continue;
			}
			int addIn = 0;
			string baseNum = "";
			int floatPos = oneFloat + twoFloat - (oneBaseNum.length() - 1 - i);

			for (int j=twoBaseNum.length() - 1; j>=0; j--)
			{
				int bit = (oneBaseNum[i] - '0') * (twoBaseNum[j] - '0') + addIn;

				addIn = bit / 10;
				bit %= 10;
				baseNum = (char)(bit + '0') + baseNum;
			}
			while (addIn > 0)
			{
				int bit = addIn % 10;
				addIn /= 10;
				baseNum = (char)(bit + '0') + baseNum;
			}
			//cout << BigDecimal(baseNum, floatPos).toString() << endl;
			res = res.add(BigDecimal(baseNum, floatPos));  //Bug
			//cout << "Run here" << endl;
		}
		return res;
	}
	BigDecimal pow(int n)
	{
		if (n == 0)
		{
			return BigDecimal();
		}
		BigDecimal res = *this;
		for (int i=1; i<n; i++)
		{
			res = res.multiply(*this);
		}
		return res;
	}
	int getFloatPos()
	{
		return floatPos;
	}
	string getBaseNum()
	{
		return baseNum;
	}
	string toString()
	{
		string num = "";
		for (int i=0; i<baseNum.length(); i++)
		{
			if (i == baseNum.length() - floatPos)
			{
				num += ".";
			}
			num += baseNum[i];
		}
		if (floatPos < 0)
		{
			for (int i=0; i<abs(floatPos); i++)
			{
				num += "0";
			}
		}
		return num;
	}
private:
	string baseNum;
	int floatPos;
	void trimZero()
	{
		while (baseNum.length() > 1 && baseNum[baseNum.length() - 1] == '0')
		{
			baseNum.erase(baseNum.length() - 1, 1);
			floatPos --;
		}
	}
};


int main(){
	int n;
	int m =0 ;
	fin>>n;
	string base = "5.2360679774997896964091736687313";
	for(m=0; m<n; m++)
	{
		BigDecimal bigD(base);
		int p;
		fin >> p;
		string res = bigD.pow(p).toString();
		//cout << res << endl;
		int k = res.find('.');
		int start = (k - 3) >= 0? k-3:0;
		int len = k - start;
		res = res.substr(start, len);
		for(int i=0; i<3-len; i++)
			res = '0'+res;

		fout << "Case #" << m+1<<": "<<res<<endl;
	}
	return 0;
}