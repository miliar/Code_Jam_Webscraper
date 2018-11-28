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


//ifstream freader("B-small.in");
//ifstream freader("B-small-attempt0.in");
//ifstream freader("B-small-attempt1.in");
ifstream freader("B-large.in");
ofstream fwriter("B-small.out");


bool is_sorted(string str)
{
     bool is_sorted = true;
     f(i,str.length()-1)
     {
         if (str[i] >= str[i+1]) continue;
         is_sorted = false;
         break;    
     }
     return is_sorted;
}

string reverse(string str)
{
    string to_return = "";
    f(i,str.length())
    {
      to_return = str[i] + to_return;
    }       
    return to_return;
}

string get_first(string str)
{
    f(i,str.length())
    {

     if (str[i] == '0') continue;
     char temp = str[i];
     str[i] = str[0];
     str[0] = temp;
     break;                 
    }      
    return str; 
}

string get_next(string str)
{
       if (is_sorted(str))
       {
          str = reverse(str);
          str = "0" + str;
          str = get_first(str);
          return str;              
       }
       else
       {
        next_permutation(all(str));   
        return str;
       }
}

int main()
{
    int cases, temp;
    string tempstr;
    freader >> cases;

    f(i,cases)
    {   
        freader >> tempstr;
        fwriter << "Case #" << i + 1 << ": " << get_next(tempstr) << endl;
    }

    //getch();
    freader.close();
    fwriter.close();    
}
