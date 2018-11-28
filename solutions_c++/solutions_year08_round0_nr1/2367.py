#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;


int next(string q[], string w, int offset, int m);
int nextse(string S[], string Q[], int n, int m, int offset);

int main() {
    ofstream fout ("test2.out");
    ifstream fin ("test2.in");

    int m;           // Number of current Queries
    int n;           // Number of current Searchengines    
    int N;           // Number of test cases
    string S[100];   // Searchengines
    string Q[1000];  // Queries
    string temp;
    
    if (fin.is_open())
    {

       fin >> N;
       getline(fin, temp);

       for (int q = 1; q <= N; q++) // for each case       
       {
          // Input each case
          fin >> n;
          getline(fin, temp);
          
          for (int w = 0; w < n; w++)
              getline (fin, S[w]);          
          
          fin >> m;
          getline(fin, temp);

          int c;

          if (m == 0)
             c = 1;
          else
          {          
              for (int w = 0; w < m; w++)
                  getline (fin, Q[w]);
    
    
              int k = 0;
              c = 0;
              while (k < m)
              {    
                   k = nextse(S,Q,n,m,k);    
                   c++;
              }
          }
          //cout << next(Q, "Yeehaw", m, 0) << endl;
          
          fout << "Case #" << q << ": " << (c - 1) << endl;
          
          cout << "Answer: " << (c - 1) << endl;
          cout << "============================" << endl;
       }

    }

    system("PAUSE");
    return 0;
}


int next(string Q[], string w, int m, int offset)
{
    int i;

    for (i = offset; i< m; i++)
    {
        if (Q[i] == w)
           return i;
    }    
    return i;
}

int nextse(string S[], string Q[], int n, int m, int offset)
{
    int max = 0;
    string se;
    int nextcount;

    for (int j = 0; j < n; j++)
    {
        nextcount = next(Q,S[j],m,offset);
        //cout << S[j] << ": " << nextcount << endl;
        if (nextcount > max)
        {
           max = nextcount;
           se = S[j];
        }  
    }
    
    cout << se << ": " << max - offset << endl;
    return max;
}
