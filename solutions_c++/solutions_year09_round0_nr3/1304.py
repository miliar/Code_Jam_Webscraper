#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const int maxnum = 501;

int main()
{
    ifstream fin("C-large.in");
    ofstream fout("C-large.out");   
    
    int i, j, k, l;
    

    
    int N;
    fin >> N;
    char junk[maxnum];
    fin.getline(junk, maxnum);
    
    string s = "welcome to code jam";
    int numchar = s.length();
    
    
    int dpcount[maxnum];
    int linelen;
    int ans;
    
    char line[maxnum];
    char currlett, prevlett;
    string formatans;
    
    for (i=0; i<N; i++)
    {
        ans = 0;
        fin.getline(line, maxnum);
        linelen = fin.gcount() - 1;
            
        for (j=0; j<maxnum; j++)
            dpcount[j] = 0;
        
        //set all with m to 1
        k = numchar-1;
        currlett = s[k];
        
        for (j=0; j<linelen; j++)
            if (line[j] == currlett)
               dpcount[j] = 1;
        
        for (k = numchar-2; k>=0; k--)
        {
            prevlett = currlett;
            currlett = s[k];
            //find all a's
            for (j=0; j<linelen; j++)
            {
                if (line[j] == currlett)
                {
                   dpcount[j] = 0;
                   for (l = j+1; l < linelen; l++)
                   {
                       if (line[l] == prevlett)
                       {
                          dpcount[j] += dpcount[l];
                          dpcount[j] = dpcount[j] % 10000;
                       }
                   }
                   
                   if (k==0) ans += dpcount[j];
                   ans = ans % 10000;
                }
            }
        }

        formatans = "";
        if (ans < 1000) formatans = "0" + formatans;
        if (ans < 100) formatans = "0" + formatans;
        if (ans < 10) formatans = "0" + formatans;
                
        fout << "Case #" << (i+1) << ": " << formatans << ans << endl;
        
    }
    
    
    
    
    //fout << line << endl;
    
    fin.close();
    fout.close();
        
    return 0;
}
