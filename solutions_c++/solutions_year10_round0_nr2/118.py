#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
#include <cassert>
#include "BigIntegerLibrary.hh"

using namespace std;

#define v(x) vector< x >
#define vv(x) v(v(x))
#define pb push_back
#define forlist(_type,_list,_it) for(list< _type >::iterator _it=_list.begin();_it!=_list.end();_it++)

BigInteger euclid(BigInteger a, BigInteger b)
{
    while(b!=0)
    {
        BigInteger t = b;
        b = a%b;
        a = t;
    }
    return a;
}

int main(int argc, char* argv[])
{
    ifstream input("B-large.in");
    assert(input.is_open());
    ofstream output("B-large.out");
    assert(output.is_open());

    int C;
    input>>C;
    for(int caseNum=0;caseNum<C;caseNum++)
    {
        list<BigInteger> numbers;
        int N;
        input>>N;
        BigInteger minNumber;
        for(int i=0;i<N;i++)
        {
            string s;
            input>>s;
            BigInteger x = stringToBigInteger(s);
            numbers.pb(x);
            if(i==0) minNumber = x;
            else if(x<minNumber) minNumber = x;
        }
        //cout<<"BEGIN CASE #"<<caseNum+1<<endl;

        //cout<<"original list:"<<endl;
        //forlist(BigInteger,numbers,it) cout<<*it<<" ";
        //cout<<endl;

        numbers.sort();
        numbers.unique();
        numbers.remove(minNumber);
        forlist(BigInteger,numbers,it) *it-=minNumber;

        //cout<<"list after reduction:"<<endl;
        //forlist(BigInteger,numbers,it) cout<<*it<<" ";
        //cout<<endl;

        BigInteger gcd = *numbers.begin();
        numbers.pop_front();
        forlist(BigInteger,numbers,it) gcd = euclid(gcd,*it);

        //cout<<"GCD: "<<gcd<<endl;

        BigInteger answer = (gcd - minNumber%gcd)%gcd;

        output<<"Case #"<<caseNum+1<<": "<<answer<<endl;
    }
    input.close();
    output.close();
    return 0;
}