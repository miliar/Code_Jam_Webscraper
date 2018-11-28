#include<iostream>
using namespace std;
string long2string(long number)
{   
	bool isNeg = false;
	string s;
	long lastdigit = 0;
	if(number < 0 )
	{
		isNeg = true;
		number *= -1;
	}
	if(number == 0)
	{
		return string(1,'0');

	}
	while((number / 10 >= 0) && (number > 0))
	{
		lastdigit = number % 10;

		s = string(1,lastdigit + '0') + s;

		number=(number-lastdigit)/10;
	}
	if(isNeg)
		s = '-'+s;
	return s;

}
long string2long(string str)
{
	int i = 0;
	long number = 0;
	bool isNeg = false;
	if(str[0] == '-')
	{
		isNeg = true;
		i = 1;
	}
	for(; i < str.length(); i++)
		number = number * 10 + str[i] - '0';
	if(isNeg)
		number *= -1;
	return number;

}

string stringShitOne2R(string str)
{
    string ret;
    ret = str.substr(1) + str[0];
    return ret;
}

int getRecycledNum(long num, long A, long B)
{
    int total = 0;
    string str = long2string(num);
    //cout << "long2string: " << str << endl;
    int len = str.length();
    for(int i = 1 ; i < len; i++)
    {
        str = stringShitOne2R(str);
        long tmp = string2long(str);
        if(tmp <= num) // same
        {
            continue;
        }
       // cout << "string2long: " << tmp << endl;
        if(tmp >=A && tmp <=B)
        {
            total++;
        }
    }
    return total;
}
int main()
{
    long A, B;
    int caseNum;
    cin >> caseNum;
    for(int i = 1; i <= caseNum ; i++)
    {
        cout << "Case #" << i << ": " ;
        int total = 0;
        cin >> A;
        cin >> B;
       // cout << "A: " <<A << " B: " << B<<endl;
        if ( B >= A)
        {
            for(long tmp = A; tmp <=B; tmp++ )
            {
                total += getRecycledNum(tmp,A,B);
            }
        }
       // cout <<"total ";
        cout << total <<endl;
    }
}