#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

const int MAXD = 5000;
const int MAXN = 500;

int L, D, N;
string a[MAXD];
string p;

int matchPattern(string p, string w)
{
    int np = p.length();
    int nw = w.length();
          
    int parenthesis = 0;    
    int i = 0;
    int j = 0;
    while (i < nw && j < np)
    {
         bool ok = false; 
         if (p[j] == ')')              
         {
             return 0;     
         }
         else if (p[j] == w[i])
         {
             ok = true;              
             if (parenthesis < 0) 
             {
                  while (p[j] != ')') j++;
                  parenthesis = 0;                      
             }
         }
         else if (p[j] == '(') parenthesis = -1;
         j++; 
         
         if (parenthesis == 0)
         {         
             if (!ok) return 0;
             i++;    
         }
    }
    return 1;
}

int main(int argc, char *argv[])
{
    ifstream cin("a-large.in");
    ofstream cout("a-large.out");	
    
    cin >> L >> D >> N;
    for (int i = 0; i < D; i++)
        cin >> a[i];
    for (int j = 0; j < N; j++)
    {
        int x = 0;
        cin >> p;
        for (int i = 0; i < D; i++)
            if (matchPattern(p, a[i])) x++;
        cout << "Case #" << j+1 << ": " << x << endl;
    }
    
	cout.close();    
	cin.close();
    
     
    //system("PAUSE");
    return EXIT_SUCCESS;
}
