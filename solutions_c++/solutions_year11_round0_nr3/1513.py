#include <iostream>
#include <string>
#include <vector>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

//*
#include <fstream>
fstream fin ("C-large.in",ios::in);
fstream fout ("output.txt", ios::out);
#define cin fin
#define cout fout
//*/

string convertToBinary(int number, int weishu)
{
    char* binary = new char[weishu];
    while(number!=0)
    {
        weishu--;
        binary[weishu] = '0' + number % 2;
        number/=2;
    }
    while(weishu >= 0)
    {
        weishu--;
        binary[weishu] = '0';
    }
    return string(binary);
}

int GetWeiShu(int number)
{
    int weishu = 0;
    while(number!=0)
    {
        number/=2;
        weishu++;
    }
    return weishu;
}

int maxInArray(int* array, int length)
{
    int max = -99999;
    for(int i=0; i<length; i++)
        if(array[i] > max)
        {
            max = array[i];
        }

    return max;
}

int minInArray(int* array, int length)
{
    int min = 9999999;
    for(int i=0; i<length; i++)
        if(array[i] < min)
        {
            min = array[i];
        }
    return min;
}

int sumOfArray(int* array, int length)
{
    int sum = 0;
    for(int i=0; i<length; i++)
        sum += array[i];
    return sum;
}

bool CheckCanDivide(vector<string> binarynumbers, int weishu)
{
    for(int i=0; i<weishu; i++)
    {
        int sumOfOne = 0;
        for(int j=0; j<binarynumbers.size(); j++)
        {
            if( binarynumbers.at(j)[i] == '1')
                sumOfOne++;
        }
        if(sumOfOne % 2 != 0)
            return false;
    }
    return true;
}

int main()
{
    int caseNum;
    cin >> caseNum;

    for(int m=0; m<caseNum; m++)
    {
        int candyNumber;
        cin >> candyNumber;

        int* candies = new int[candyNumber];
        for(int i=0; i<candyNumber; i++)
        {
            int temp;
            cin >> temp;
            candies[i] = temp;
        }


        int max = maxInArray(candies, candyNumber);
        int weishu = GetWeiShu(max);
        vector<string> binaries;
        for(int i=0; i<candyNumber; i++)
        {
            string str = convertToBinary(candies[i],weishu);

            binaries.push_back(str);

            //cout << str << endl;

        }
        cout <<"Case #" << m+1 << ": ";
        if(CheckCanDivide(binaries, weishu))
        {
            int result = sumOfArray(candies, candyNumber) - minInArray(candies,candyNumber);
            cout << result <<endl;
        }
        else
        {
            cout << "NO" << endl;
        }

    }
    return 0;
}
