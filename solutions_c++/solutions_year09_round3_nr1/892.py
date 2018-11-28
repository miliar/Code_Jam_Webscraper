#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<algorithm>
#include<math.h>
#include<time.h>
#include<conio.h>
using namespace std;

#define f(i,x) for(int i = 0; i < x; i++)
#define fv(i,x) for(int i = 0; i < x.size(); i++)
#define fr(i,a,b) for(int i = a; i <=b; i++)
#define all(x) x.begin(),x.end()
#define pb(x) push_back(x)
#define print(i,x) fv(i,x) cout << x[i] << " ";

typedef long long int64;
typedef unsigned long long uint64;
//End Defn

ifstream freader("A-small.in");
//ifstream freader("A-small-attempt0.in");
//ifstream freader("A-small-attempt1.in");
//ifstream freader("A-large.in");
ofstream fwriter("A-small.out");

vector<char> map;
vector<char> mapto;
 
double get_dec(char c)
{
 if (c >= 32 && c<=41) return c-32;
 else return (c - 'A') + 10;    
    
}

double to_decimal(string str)
{
 int base = mapto.size();
 if (base == 1) base ++;
 double power = 0;
 double answer = 0;
 for (int i = str.length()-1;i>=0;i--)
 {
     answer += get_dec(str[i]) * pow(base,power);
     power+=1;
 }
// cout << endl;
 return answer;
}

string to_basestring(string str)
{
 map.clear();
 mapto.clear();
 mapto.push_back(33);
 map.push_back(str[0]);
 char incrementer = 32;
 
 fr(i,1,str.length()-1)
 {
  if (find(all(map),str[i]) != map.end()) continue;
  map.push_back(str[i]);
  mapto.push_back(incrementer);
  if (incrementer == 32) incrementer = 34;
  else if (incrementer == 41) incrementer = 65;
  else incrementer++;
 }
 vector<char> consumed;
 fv(i,map)
 {
 
  f(j,str.length())
  {
     if (map[i] == str[j])
     {
                 str[j] = mapto[i];
     }                 
  }         
 }
 
 return str;
 
}
int main()
{
    int cases, temp;
    string tempstr;
    freader >> cases;
    f(i,cases)
    {   
        freader >> tempstr;
        //cout << tempstr << " - ";
        tempstr = to_basestring(tempstr);
        //cout << tempstr << endl;
        uint64 num = to_decimal(tempstr);
        fwriter << "Case #" << i + 1 << ": " << num << endl;
        //getch();
    }

   // getch();    
    freader.close();
    fwriter.close();    
}
