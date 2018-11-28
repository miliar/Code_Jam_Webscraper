#include <iostream>
#include <fstream>
#include <string>

#define MAXL 15
#define MAXD 5000

using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
        
    char dict[MAXD][MAXL];
    
    int i, j, k;
    
    int L, D, N;
    fin >> L >> D >> N;
    //fout << L << " " << D << " " << N << endl;

    for (i=0; i<MAXD; i++)
    {
        for (j=0; j<MAXL; j++)
        {
            dict[i][j] = ' ';
        }
    }   
    
    for (i=0; i<D; i++)
    {
        for (j=0; j<L; j++)
        {
            char temp;
            fin >> temp;
            dict[i][j] = temp;
        }
    }

    /*
    for (i=0; i<D; i++)
    {
        for (j=0; j<L; j++)
        {
            fout << dict[i][j];
        }
        fout << endl;
    }
    */
    
    string word;
    char c = ' ';
    int token = 0;
    int posswords[D];
    int stillposs[D];
    int ans;
    
    for (i=0; i<N; i++)
    {

        for (k=0; k<D; k++)
        {
            posswords[k] = 1;
            stillposs[k] = 0;
        }

        fin >> word;
        //fout << word << endl;
        

        token = 0;
        j = 0;
        while (token < L)
        {      
            c = word[j];
            if (c == '(')
            {
                  for (k=0; k<D; k++)
                      stillposs[k] = 0;
                      
                  j++;
                  c = word[j];
                  while (c != ')')
                  {
                        for (k=0; k<D; k++)
                        {
                            if (posswords[k])
                            {
                               if (dict[k][token] == c)
                               {
                                  stillposs[k] = 1;
                               }
                            }
                         }
                        j++;
                        c = word[j];
                  }
                  for (k=0; k<D; k++)
                  {
                      if (posswords[k] && (!stillposs[k])) posswords[k] = 0;
                  }
                  
            }
            else
            {
                for (k=0; k<D; k++)
                {
                    if (posswords[k])
                    {
                       if (dict[k][token] != c)
                       {
                          posswords[k] = 0;
                       }
                    }
                }
            }
            token++;
            j++;
        }
        
        ans = 0;
        for (k=0; k<D; k++)
        {
            //fout << posswords[k] << endl;
            ans += posswords[k];
        }
            
        fout << "Case #" << i+1 << ": " << ans << endl;
    }
            

    fin.close();
    fout.close();
    
    return 0;
}
    
    
    
