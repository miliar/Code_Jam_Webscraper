#include <pcre.h>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <set>
#include <map>
#include <iterator>



using namespace std;

//templates:

#define rpe(i,a,b) for(i=a;i<b;i++)
#define rp(i,n) rpe(i,0,n)
#define er(i,n) if( i == n ) {
#define co if (
#define ex ){
#define el }else{
#define elco }else if (
#define z }


typedef long long ll;

const ll INF = 100000000000000000LL;

////////////////////////////////////////////////////////////////////////
#define zero(S) memset(S,0,sizeof(S))


int k = 0;


std::set<char> vec;
std::map<char, char> m;
std::map<char,int>::iterator it;


int main(){

    int i,j;
    int size,count=0;
    double res;

    ifstream in("in.txt");
    ofstream out("out.txt");

    string s1 = "";

    int testcase;
    getline(in,s1);
    testcase = atoi(s1.c_str());

    int caseId;
    for (caseId=1;caseId<=testcase;caseId++)
    {

        long L;

        string s = "";
        m.clear();
        vec.clear();

        getline(in,s);

        if(size == 1)
        {
            out<<"Case #"<<caseId<<": 1\n";
            out.flush();
            continue;
        }

        if(size == 2)
        {
            int n = 0;
            if(s[1] == s[0]) n=3; else n=2; //base=2

            out<<"Case #"<<caseId<<": " << n<<"\n";
            out.flush();
            continue;
        }

        rp(i,s.size())
        {
           vec.insert(s[i]);
        }

        int base = vec.size();
        if (base==1) base = 2;

        int size = s.size();

        int mult = pow(base,size-1);

        int Number = 0;



        int iter = 0;
        int curdig = 1;

        Number += mult;  //*1
        mult/=base;
        iter++;

        while(s[iter] == s[iter-1]){
           Number += mult;  //*1
           mult/=base;
           iter++;
           if(iter == size) break;

        }

        if(iter == size)
        {
            out<<"Case #"<<caseId<<": " << Number<<"\n";
            out.flush();
            continue;
        }

        m[s[0]] = 1;
        m[s[iter]] = 0;

        //next dig gar to be not as prev - make = 0
        //int curdig = 0;

        //Number += curdig*mult;  --zero

        mult/=base;
        iter++;

        curdig = 2;

        for(;iter<size;iter++)
        {

           if (m.find(s[iter]) != m.end())
           {
               Number += m[s[iter]]*mult;
           }
           else
           {
               Number += curdig*mult;
               m[s[iter]] = curdig;
               curdig++;
           }

           mult/=base;
        }


        out<<"Case #"<<caseId<<": " << Number<<"\n";
        out.flush();
    }


    printf("ALL DONE.\n");

    return 0;
}
