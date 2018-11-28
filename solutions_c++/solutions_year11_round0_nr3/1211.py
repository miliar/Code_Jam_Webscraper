        #include <fstream>
        #include <iostream>
        #include <string>
        #include <stdio.h>
        
        
        using namespace std;
        
        int main()
        {
            ofstream fout ("2011gcj2out.txt");
            ifstream fin ("2011gcj2in.txt");
            
            int t;
            fin >> t;
            
            for(int i=0; i<t; i++)
            {
                    
            int n;
            
            fin >> n;
            
            int num[n];
            
            for(int j=0; j<n; j++)
            fin >> num[j];
        
            
            int aux;
            
            int soma[20];
            
            for(int k=0; k<20; k++)
            soma[k]=0;
            
            for(int j=0; j<n; j++)
            {
            aux = num[j];
            for(int k=0; k<20; k++)
            {
            soma[k]=(aux + soma[k])%2;
            aux = aux/2;
            }
            }
            
            int check=0;
            
            
            
            for(int k=0; k<20; k++)
            {
            if(soma[k]!=0)
            check=1;
            }
            
            if(check==1)
            fout << "Case #" << i+1 << ": NO" << endl;
            else
            {
            int min=num[0];
            int res=0;
            
            for(int j=1; j<n; j++)
            {
            if(num[j] < min)
            {
            res=res+min;
            min=num[j];
            
            }
            else
            {
            res=res+num[j];
            
            }

            }
            
            fout << "Case #" << i+1 << ": " << res << endl;
            }
                    
            }
             
            
            
            
            
            return 0;
            
        }
        
        
