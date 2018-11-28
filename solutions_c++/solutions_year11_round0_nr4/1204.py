        #include <fstream>
        #include <iostream>
        #include <string>
        #include <stdio.h>
        
        
        using namespace std;
        
        int main()
        {
            ofstream fout ("2011gcj3out.txt");
            ifstream fin ("2011gcj3in.txt");
            
            int t;
            
            fin >> t;
            
            for(int i=0; i<t; i++)
            {
            int n;
            fin >> n;
            
            int perm[n];
            
            for(int j=0; j<n; j++)
            fin >> perm[j];
            
            int cycle[n];
            int last[n];
            int count[n];
            
            for(int j=0; j<n; j++)
            {
            count[j]=0;
            last[j]=-1;
            perm[j]--;
            }
            
            for(int j=0; j<n; j++)
            {
            last[j]=j;
            cycle[j]=1;
            for(int k=0; k<n; k++)
            {
            if(perm[last[j]]!=j)
            {
            last[j]=perm[last[j]];
            cycle[j]++;
            }
            else
            break;
            }
            }
            
            
            
            for(int j=1; j<n+1; j++)
            for(int k=0; k<n; k++)
            {
            if(cycle[k]==j)
            count[j-1]++;
            }
            
            
            fout << "Case #" << i+1 << ": " << n-count[0] << endl;
            
            
            
            
                      
            
            }
             
            
            
            
            
            return 0;
            
        }
        
        

