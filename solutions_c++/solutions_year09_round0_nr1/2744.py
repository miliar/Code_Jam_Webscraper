#include<iostream>
#include<string.h>
#include <fstream>
#include<map>
#include<sstream>
#include<vector>
#include<algorithm>
using namespace std;
ifstream fin("A-small-attempt3.IN");
ofstream fout("A-small-attempt3.OUT");
#define cin fin
#define cout fout
int main()
{
string vi = "abc";
int L,D,N;
string names;
string cases[501] ;
string samples[501][501];
string mybuff;
int track=0;
cin >> L >> D >> N ;
vector<string> map1;
for(int t=0;t<D;t++)
{
cin >>  names;
map1.push_back(names);
}

for(int t=0;t<N;t++)
{
cin >> cases[t];
//cout << cases[t]  << " lengths" << endl;
}
//cout << cases[0] << endl;

for(int t=0;t<N;t++)
{
    track=0;
   // cout << t << " t" << endl;
    for(int g=0;g<cases[t].length();g++ )
    {
      //  cout << g << " g" << endl;
        if(cases[t][g] == '(')
        {

       //     cout << t <<  " " <<g  << " t g" << endl;
            g++;
            samples[t][track] = "";
            while(cases[t][g] !=')')
            {
      //       cout << cases[0]  << " " << cases[t] << " cases" << endl;
      //      cout << t <<  " " <<g  << " " << cases[t][g] << " t g " << cases[t] << endl;
            samples[t][track] = samples[t][track] + cases[t][g] ;
            g++;

            }
       //     cout << samples[t][track]  << " 234" << endl;
           track++;

        }
        else
        {
       //     cout << t <<  " " << g  << " t g" << endl;
            samples[t][track] = "";
            while(cases[t][g] != '(' and g < cases[t].length())
            {
      //      cout << t <<  " " <<g  << " t g" << endl;
             samples[t][track] = samples[t][track] + cases[t][g] ;
             track++;
             g++;

            }
            g--;
       //     cout << samples[t][track]  << " 123" << endl;
            //track++;
      //      cout << t <<  " " <<g  << " t g" << endl;
        }

    }
}

for(int h=0;h<N;h++)
{
int count=0;
for(int t=0;t<D;t++)
{
    int lower=0;
    for(int r=0;r<L;r++)
    {
    string::iterator it = samples[h][r].begin();
    it = find(samples[h][r].begin(),samples[h][r].end(),map1[t][r]);
    if(it != samples[h][r].end())
    lower++;
    }
    if(lower==L)
    count++;
}
cout << "Case #"  << h+1 << ": " << count << endl;
}

}
