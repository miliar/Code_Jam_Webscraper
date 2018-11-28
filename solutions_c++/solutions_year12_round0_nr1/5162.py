/*
 * Author: FreePascal
 * Created Time:  2012/4/14 9:41:24
 * File Name: 
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <list>
#include <stack>
#include <fstream>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
string s1 = "abcdefghijklmnopqrstuvwxyz ";
string s2 = "yhesocvxduiglbkrztnwjpfmaq ";
int main() {
    ifstream cin("input.txt");
    ofstream cout("output.txt");
   int T;
  cin>>T;
  string tm;
  getline(cin,tm);
 for(int cs = 1;cs <= T;cs++)
 {
    string src;
   getline(cin,src);
   //cout<<src<<endl;
   cout<<"Case #"<<cs<<": "; 
   //printf("Case #%d: ",cs);
  for(int i = 0;i < src.size();i ++)
    cout<< s2[s1.find(src[i])];
  cout<<endl;
 } 
    return 0;
}

