#include<iostream>
#include<cstdio>
#include<fstream>
#include<cstdlib>
#include<vector>
#include<map>
#include<algorithm>

#define forn(i,n) 	 for(int i=0; i<n; i++)
#define fornd(i,n) 	 for(int i=n-1; i>=0; i--)
#define fornx(i,x,n) for(int i=x; i<n; i++)

using namespace std;

int main(int argc, char** argv)
{
    ifstream entrada("B-large-0.in");
	ofstream salida("B-large-0.out");
	
    int casos;
	entrada >> casos;
	
    /* N S p N*t_i */
    
    int n, s, p;
    
	forn(caso, casos)
	{        
        entrada >> n >> s >> p;
        vector<int> totals (n);
        
        forn(i, n)
            entrada >> totals[i];
            
        /* Divido por 3 y con eso intento formar los valores. 
         * Me quedo con la parte entera de la división y después 
         * me fijo cuanto falta. Si faltan 2 entonces 
         * surprising: [d, d, d + 2]
         * not surprising: [d, d + 1, d + 1].
         * 
         * Si falta 1. 
         * surprising: [d - 1, d + 1, d + 1]
         * not surprising: [d, d, d + 1]         
         * 
         * Si falta 0
         * surprising: [d - 1, d, d + 1]
         * not surprising: [d, d, d]. 
         * 
         * Falta tener en cuenta que los scores van entre 0 y 10. */
        
        int res = 0;
        
        forn(i, n)
        {
            int d = totals[i]/3;
            int miss = totals[i] - d*3;
            
            if (d >= p)
            {
                res++;
            }
            else
            {
                if (d == p - 1)
                {
                    if (miss > 0)
                        res++;
                    else
                    {
                        if (d > 0 and d < 10 and s > 0)
                        {    
                            res++;
                            s--;
                        }
                    }
                }
                else
                {
                    if (d == p - 2 and miss == 2 and d < 9 and s > 0)
                    {
                        //cout << "d: " << d << " s: " << s << endl;
                        res++;
                        s--;
                    }
                }
            }
        }
            
        salida << "Case #" << caso + 1 << ": " << res << endl;
	}
	
	return 0;	
}
