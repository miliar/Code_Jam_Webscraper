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

int P, Q;
vector<int> loc;
vector<bool> to_release;
vector<bool> released;

ifstream freader("C-small.in");
//ifstream freader("C-small-attempt0.in");
//ifstream freader("C-small-attempt1.in");
//ifstream freader("C-large.in");
ofstream fwriter("C-small.out");



int main()
{
    int cases, temp;
    string tempstr;
    freader >> cases;

    f(i,cases)
    {   
        loc.clear();       //int P, Q;
        freader >> P >> Q;
        to_release.clear();
        released.clear();
        to_release.resize(P,0);
        released.resize(P, 0);
        f(j,Q) 
        {
               freader >> temp;
               loc.push_back(temp - 1);
               to_release[temp - 1] = 1;
        }
        
        sort(all(loc));
        //vector<int> optimal_loc;
        int min_length = 1000000;
        do
        {
                released.clear();
                released.resize(P, 0);
               int traversed_len = 0;
               fv(j,loc)
               {
                       released[loc[j]] = 1;
                       for (int k = loc[j] - 1; released[k] != 1 && k!= -1; k--) {traversed_len++; }
                       for (int k = loc[j] + 1; released[k] != 1 && k!= P; k++) {traversed_len++; }
               }  
               if (traversed_len < min_length)
               {
                  min_length = traversed_len;
//                  optimal_loc.clear();
//                  fv(j,loc) 
//                  {
//                     optimal_loc.push_back(loc[j]);       
//                  }                  
               }          

               //getch();          
        }
        while (next_permutation(all(loc)));
         fwriter << "Case #" << i + 1 << ": " << min_length << endl;
         //      cout << min_length << endl; 
        //cout << endl;
        //print(j,to_release);
        //cout << endl;
    }
//getch();
    freader.close();
    fwriter.close();    
}
