#include <algorithm>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>


using namespace std;


//copy(sequence.begin(), sequence.end(), ostream_iterator<E>(cout, " "));
//cout << endl;


vector<set<string> > g_HappyNumbers(10);
vector<set<string> > g_NonHappyNumbers(10);


string IntToStr(unsigned int num, unsigned int base)
{
    vector<char> str;
    unsigned int n = num;

    if (n == 0)
    {
        return "0";
    }

    if (n == 1)
    {
        return "1";
    }

    while (n != 0)
    {
        str.push_back((n % base) + '0');
        n /= base;
    }

    reverse(str.begin(), str.end());
    str.push_back(0);   // Append \0

    return &str[0];
}


bool IsHappy(const string &num, unsigned int base)
{
    //cout << "IsHappy: num=" << num << " base=" << base << endl;

    if (g_HappyNumbers[base - 1].find(num) != g_HappyNumbers[base - 1].end())
    {
        //cout << "hit: happy: " << num << endl;
        return true;
    }

    if (g_NonHappyNumbers[base - 1].find(num) != g_NonHappyNumbers[base - 1].end())
    {
        //cout << "hit: nonhappy: " << num << endl;
        return false;
    }

    set<string> s;
    string n(num);

    while (1)
    {
        unsigned int sum = 0;

        for (int i=0; i<n.size(); ++i)
        {
            const int digit = n[i] - '0';
            sum += digit * digit;
        }

        //cout << n << ": " << sum << endl;

        if (sum == 1)
        {
            g_HappyNumbers[base - 1].insert(n);

            for (set<string>::iterator it=s.begin(); it!=s.end(); ++it)
            {
                //cout << "insert happy: " << *it << " (" << base << ")"<< endl;
                g_HappyNumbers[base - 1].insert(*it);
            }
            return true;
        }

        n = IntToStr(sum, base);

        //cout << "New n: " << n << endl;

        if (s.find(n) != s.end())
        {
            //cout << n << ": XX" << endl;
            //g_NonHappyNumbers[base - 1].insert(n);
            for (set<string>::iterator it=s.begin(); it!=s.end(); ++it)
            {
                //cout << "insert nonhappy: " << *it << " (" << base << ")"<< endl;
                g_NonHappyNumbers[base - 1].insert(*it);
            }
            return false;
        }

        s.insert(n);
    }

    return false;
}


void RunTestCase(int testCaseIndex)
{
    vector<unsigned int> nums;
    string str;
    int n;

    getline(cin, str);
    //cout << str << endl;

    stringstream stream(str);

    while (stream)
    {
        if (stream >> n)
        {
            nums.push_back(n);
        }
    }

    //copy(nums.begin(), nums.end(), ostream_iterator<unsigned int>(cout, " "));
    //cout << endl;

    int candidate = 2;

    while (1)
    {
        bool found = true;

        for (int i=0; i<nums.size(); ++i)
        {
            if (!IsHappy(IntToStr(candidate, nums[i]), nums[i]))
            {
                found = false;
                break;
            }
        }

        if (found)
        {
            break;
        }

        ++candidate;
    }

    cout << "Case #" << (testCaseIndex + 1) << ": " << candidate << endl;
}


int main()
{
/*
    cout << "100: " << IsHappy(IntToStr(68, 10), 10) << endl;
    cout << "100: " << IsHappy(IntToStr(82, 10), 10) << endl;
    cout << "100: " << IsHappy(IntToStr(100, 10), 10) << endl;
    */
    //cout << "91: " << IsHappy(IntToStr(91, 9), 9) << endl;
    //cout << "91: " << IsHappy(IntToStr(91, 10), 10) << endl;
/*
    cout << "68: " << IsHappy("68", 10) << endl;
    cout << "82: " << IsHappy("82", 10) << endl;
    */

    int N;

    cin >> N;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int testCaseIndex=0; testCaseIndex<N; ++testCaseIndex)
    {
        RunTestCase(testCaseIndex);
    }

    return 0;
}
