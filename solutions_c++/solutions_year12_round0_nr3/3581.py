#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int prova[1001];

int parseInt(string a)
{
    stringstream ss(a);
    int i;
    ss >> i;
    return i;
}

string toString(int a)
{
    ostringstream oss;
    oss << a;
    return oss.str();
}

string solve(string a, int size)
{
    string tmp = a.substr(a.length()-size, a.length());
    tmp += a.substr(0,a.length()-size);
    return tmp;
}

int main()
{
    string tmp,strA,strB;
    ifstream in("input");
    ofstream out("output");
    ofstream three("three");
    int t=0,a=0,b=0,inA,inB;
    in >> t;
    int result;
    for(int i=0; i<t; i++)
    {
        result =0;
        in >> a;
        in >> b;
        inA=a;
        inB=b;
        if(inB < 10)
            out << "Case #" << i+1 << ": 0" << endl;
        else
        {
            int num = inA;
            string prvTmp = "";
            for(int j=0;j<=(inB - inA); j++)
            {
                strA = toString(num);
                for(int k=1;k<strA.length();k++)
                {
                    tmp = solve(strA, k);
                    if(parseInt(tmp) <= inB && parseInt(tmp) >= inA && parseInt(tmp) > parseInt(strA))
                    {
                        if(tmp != prvTmp)
                        {
                            result++;
                            prvTmp = tmp;
                        }
                    }
                }
                prvTmp="";
                tmp = "";
                num++;
            }
            out << "Case #" << i+1 << ": " << result << endl;
        }
    }
    in.close();
    out.close();
    three.close();
    return 0;
}
