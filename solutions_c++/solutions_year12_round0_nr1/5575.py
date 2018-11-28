#include <stdio.h>
#include <fstream>
#include <iostream>
#include <string>
#include <map>

using namespace std;

//long length(int k)
//{
//    int ans = 0;
//    while (k != 0)
//    {
//        k = k/10;
//        ans++;
//    }
//    return ans;
//}
//
//long powLong(long n)
//{
//    long res = 1;
//    for(long i = 0; i<n; i++)
//    {
//        res = res * 10;
//    }
//    return res;
//}
//
//long rotate( long k, long n)
//{
//    long l = length(k);
//    long ost = k % (long)powLong((long)n);
//    k = k / powLong((long)n);
//    k = k + (powLong(l-n) * ost);
//    return k;
//}
//
//long CalcPairs(long k, long a, long b)
//{
//    long pairs = 0;
//    for(int i = 1; i<length(k); i++)
//    {
//        long newK = rotate(k, i);
//        if( ((a <= newK) && (newK <= b)) &&
//             (length(k) == length(newK)) &&
//             (k < newK))
//        {
//            pairs ++;
//        }
//    }
//    return pairs;
//}
//
//long CalcNumbers(long a, long b)
//{
//    long ans = 0;
//    int a1=0, a2=0, a3=0;
//    for(long i = a; i<=b; i++)
//    {
//        long res = CalcPairs(i, a, b);
//        if(res == 1)
//            a1++;
//        if(res == 2)
//            a2++;
//        if(res == 3)
//            a3++;
//        ans += res;
//    }
//    return ans;
//}

std::map<char, char> gRelease;

string convert(string input)
{
    string answer(input);
    for(int i = 0; i<input.length(); i++)
    {
        answer.at(i) = gRelease[input.at(i)];
    }
    return answer;
}

int main()
{
    gRelease['a'] = 'y';
    gRelease['b'] = 'h';
    gRelease['c'] = 'e';
    gRelease['d'] = 's';
    gRelease['e'] = 'o';
    gRelease['f'] = 'c';
    gRelease['g'] = 'v';
    gRelease['h'] = 'x';
    gRelease['i'] = 'd';
    gRelease['j'] = 'u';
    gRelease['k'] = 'i';
    gRelease['l'] = 'g';
    gRelease['m'] = 'l';
    gRelease['n'] = 'b';
    gRelease['o'] = 'k';
    gRelease['p'] = 'r';
    gRelease['q'] = 'z';
    gRelease['r'] = 't';
    gRelease['s'] = 'n';
    gRelease['t'] = 'w';
    gRelease['u'] = 'j';
    gRelease['v'] = 'p';
    gRelease['w'] = 'f';
    gRelease['x'] = 'm';
    gRelease['y'] = 'a';
    gRelease['z'] = 'q';
    gRelease[' '] = ' ';
    gRelease['\n'] = '\n';
    ifstream inp("input1.txt");
    ofstream out("output.txt");
    if(!inp.is_open())
        cout<<"input file is invalid!"<<endl;
    if(!out.is_open())
        cout<<"output file is invalid!"<<endl;
    long long t;
    long long a,b;
    inp>>t;
    char buf[10000];
    inp.getline(buf, 10000);
    for(long i = 0; i<t; i++)
    {
        char buf[10000];
        inp.getline(buf, 10000);
        string inputString(buf);
        string converted = convert(inputString);
        out<<"Case #"<<i+1<<": "<<converted<<endl;
    }
    inp.close();
    out.close();
}