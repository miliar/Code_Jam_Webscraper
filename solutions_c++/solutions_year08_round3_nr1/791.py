// Compile: cl  /GX a.cpp
#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include <fstream>



using namespace std;


int al[1001];


void read_case(int ncase, fstream &in)
{
    int P,K,L;
    in >> P >> K >> L;
    for(int i=1; i<=L; i++){
        in >> al[i];
    }
    int max,almax;
    for(int i=1; i<=L;i++)
    {
        max = i;
        for(int k=i; k<=L; k++)
        {
          if(al[max] < al[k])max =k;
        }
        almax=al[i];
        al[i]=al[max];
        al[max]=almax;
    }
    int count=0;
    int press=1;
    /*for(int i=1;i<=L;i++)
    {
        cout <<al[i] <<" ";
    }
    cout <<endl;
    */
    for(int i=1;i<=L;i++)
    {
        count+=(press*al[i]);
        if(!(i%(K)))press++;
    }

    printf("Case #%d: %d",ncase,count);
    cout<<endl;

}

int main(int argc, char* argv[])
{
    fstream input(argc>1 ? argv[1]:"input", ios::in);
    if(!input.is_open()) return -1;
    int ncase;
    input >> ncase;
    for(int i=1;i<=ncase;i++) read_case(i,input);
    return 0;
}