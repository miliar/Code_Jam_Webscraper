#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int T;
int n;
int a[21], b[11];

int main(int argc, char *argv[])
{
    ifstream cin("b-large.in");
    ofstream cout("b-large.out");
    
    cin >> T;
    string tmp;
    getline(cin, tmp);
    for (int i = 0; i < T; i++)
    {    
        getline(cin, tmp);        
        n = tmp.length();
        memset(b, 0, sizeof(b));
        for (int j = 0; j < n; j++)
        {
            a[j] = tmp[j] - '0';
            b[a[j]]++;
        }
        
        int newN = 0;
        for (int j = n-2; j >= 0; j--)
        {   
            newN = 0;         
            for (int k = a[j]+1; k < 10; k++)
                if (b[k] > 0)
                {
                    for (int u = j+1; u < n; u++)
                        if (a[u] == k)
                        {
                            newN = k;
                            break;
                        }
                    if (newN != 0) break;        
                }
            
            if (newN != 0)
            {
                for (int k = 0; k < j; k++)
                    b[a[k]]--;
                
                a[j] = newN;
                b[a[j]]--;
                
                for (int k = j+1; k < n; k++)
                {
                    int num = 0;
                    for (int u = 0; u < 10; u++)
                        if (b[u] > 0)
                        {
                            num = u;
                            b[u]--;
                            break;     
                        }
                    a[k] = num;
                }    
                break;
            }  
        }
        
        if (newN == 0)
            {   
                for (int u = 1; u < 10; u++)
                        if (b[u] > 0)
                        {
                            a[0] = u;
                            b[u]--;
                            break;     
                        }
                
                a[1] = newN;
                n++;
                
                for (int k = 2; k < n; k++)
                {
                    int num = 0;
                    for (int u = 0; u < 10; u++)
                        if (b[u] > 0)
                        {
                            num = u;
                            b[u]--;
                            break;     
                        }
                    a[k] = num;
                }    
            }


        cout << "Case #" << i+1 << ": ";
        for (int j = 0; j < n; j++) cout << a[j]; 
        cout << endl;                        
    }
    
    cout.close();
    cin.close();
    //system("PAUSE");
    return EXIT_SUCCESS;
}
