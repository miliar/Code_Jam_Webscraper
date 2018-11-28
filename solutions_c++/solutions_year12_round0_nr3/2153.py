#include <iostream>
#include <sstream>
#include <set>
#include <cstdlib>

using namespace std;

string intToStr(int a)
{
    ostringstream ss;
    ss << a;
    return ss.str();
}

int strToInt(string a)
{
    return atoi(a.c_str());
}

string generateMinValue(int n)
{
    string tmp(n, '0');
    tmp[0] = '1';
    return tmp;
}

string generateMaxValue(int n)
{
    string tmp(n, '9');
    return tmp;
}

int main()
{
	int cnt = 0;
	cin >> cnt;

    for(int i = 0 ; i < cnt; ++i)
    {
        int a,b;
        string strA,strB;
        cin >> a >> b;
        int result = 0;

        if(b >= 10)
        {
            strA = intToStr(a);
            strB = intToStr(b);

            int minDigits = strA.size();
            int maxDigits = strB.size();
            for(int curDigits = minDigits; curDigits <= maxDigits; ++curDigits)
            {
                string start = strA;
                string end = strB;
                if(curDigits > minDigits)
                {
                    start = generateMinValue(curDigits);
                }
                if(curDigits < maxDigits)
                {
                    end = generateMaxValue(curDigits);
                }

                int startInt = strToInt(start);
                int endInt = strToInt(end);
                if(startInt < 10)
                {
                    continue;
                }
                for(;startInt <= endInt; ++startInt)
                {
                    string ttmp = intToStr(startInt);
                    set<int> uniquier;
                    for(int k = 1; k < curDigits; ++k)
                    {
                        string tmp2;
                        tmp2.push_back(ttmp[ttmp.size() - 1]);
                        tmp2.append(ttmp.substr(0, curDigits-1));
                        int tmpNumber = strToInt(tmp2);

                        if(tmpNumber <= endInt && tmpNumber > startInt)
                        {
                            uniquier.insert(tmpNumber);
                        }
                        ttmp = tmp2;
                    }
                    result += uniquier.size();
                }
            }
        }

        cout << "Case #" << (i+1) << ": " << result << endl;
    }

	return 0;
}
