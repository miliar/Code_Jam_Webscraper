        #include <fstream>
        #include <iostream>
        #include <string>
        #include <stdio.h>
        #include <math.h>
        
        
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
            int aux;
            int res=0;
            int aux2, aux3;
            int aux4;
            
           for(int j=2; j*j <= n; j++)
            {
            aux = 0;
            
            for(int k=2; k<j; k++)
            if(j % k == 0)
            {
            aux = 1;
            break;
             }
             
             if(aux == 0)
             {
             aux2 = j*j;
           
             for(int l=2; l < 40; l++)
             {
             if(aux2 <= n)
             {
             res++;
             }
             else
             break;
             
             aux2 = aux2*j;
             } 
             }
            } 
            
            if(n> 1)
            fout << "Case #" << i+1 << ": " << res+1 << endl;
            else
            fout << "Case #" << i+1 << ": " << 0 << endl;
            
           
            } //ciclo do i
             
            
            
            
            
            return 0;
            
        }
        
        
