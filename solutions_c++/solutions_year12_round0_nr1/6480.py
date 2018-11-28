//      In the Name of God
//      Problem About Equation.cpp      
//      Copyright 2012 Farbod <yadegarianfarbod@yahoo.com>
#include <iostream>
#include <cmath>
#include <cstring>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <vector>
#include <set>
#include <sstream>
#include <stack>

using namespace std;

#define FOR(i, a, n) for (i = (a); i < n; i++)
#define FORINT(i, a, n) for (int i = (a); i < n; i++)
#define FORINTM(i, a, n) for (int i = (a); i < n; i++)
#define FORM(i, a, n) for (i = a; i >= n; i--)
#define Size(n) ((int)(n).size())
#define all(n) (n).begin(), (n).end()
#define ll long long
#define ull unsigned long long
#define pb push_back
#define VAL(x) #x << " = " << x;
#define Wln(x) cout << x << endl
#define W(x) cout << x
#define GetN(n); int n; cin >> n;
#define GetL(n); ll n; cin >> n;
#define GetStr(x); string x; getline(cin,x);
#define CinArray(array,a,n); for(int i = a;i < n ; i ++){ cin >> array[i] ; Max =max(Max,array[i]);}  
#define CoutArray(array,a,n); for(int i = a;i < n ; i ++) cout << array[i] << " ";
#define MapC map <char , int >
#define MapS map <string , int>
#define VecI vector <int>
#define VecS vector <string>
#define Pii pair<int , int >
#define Pll pair<ll , ll >

//**********                            Main CODE                            **********//
int main(){
string s ="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv z q";
string s2="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up q z";
map<char,char> Chars;
       FORINT(i,0,s.length())
       {
                             Chars[s[i]] = s2[i]; 
       }
       GetL(n);
       string Str;
       cin.ignore();
       FORINT(i,0,n)
       {
                  getline(cin,Str);
                  //Wln(Str);
                  FORINT(j,0,Str.length())
                                          Str[j] = Chars[Str[j]];               
                  Wln("Case #"<< i+1 <<": " << Str);  
       }
       //system("PAUSE");
    return 0;
}
