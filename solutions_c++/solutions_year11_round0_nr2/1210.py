        #include <fstream>
        #include <iostream>
        #include <string>
        #include <stdio.h>
        
        
        using namespace std;
        
        int main()
        {
            ofstream fout ("2011gcj4out.txt");
            ifstream fin ("2011gcj4in.txt");
            
            int t;
            fin >> t;
            
            for(int i=0; i<t; i++)
            {
            int n, m, size;
            char aux, aux2;
            
            fin >> n;
            
            char comb[2*n][3];
            
            for(int j=0; j<2*n; j=j+2)
            {
            fin >> aux;
            fin >> aux2;
            comb[j][0]=aux;
            comb[j][1]=aux2;
            comb[j+1][0]=aux2;
            comb[j+1][1]=aux;
            fin >> aux;
            comb[j][2]=aux;
            comb[j+1][2]=aux;
            
        //    fout << comb[j][0] << " " << comb[j][1] << " " << comb[j][2] << endl;
            }
            
            
            
            fin >> m;
            
        
            
            char opp[2*n][2];
            
            for(int j=0; j<2*m; j=j+2)
            {
            fin >> aux;
            fin >> aux2;
            opp[j][0]=aux;
            opp[j][1]=aux2;
            opp[j+1][0]=aux2;
            opp[j+1][1]=aux;
      //      fout << opp[j][0] << " " << opp[j][1] << endl;
            }
            
            fin >> size;
            
            int sizenow=0;
            char res[size];
            
            
            for(int j=0; j<size; j++)
            {
            fin >> aux;
            
            if(sizenow==0)
            {
            res[0]=aux;
            sizenow++;
            }
            else
            {
            aux2=res[sizenow-1];
            int check=0;
            
            for(int k=0; k<2*n; k++)
            if(comb[k][0]==aux2 && comb[k][1]==aux)
            {
            res[sizenow-1]=comb[k][2];
            check=1;
            break;
            }
            
            if(check==0)
            {
            for(int k=0; k<sizenow; k++)          
            for(int l=0; l<2*m; l++)
            if(res[k]==opp[l][0] && aux==opp[l][1])
            {
            check=1;
            sizenow=0;
            break;
            } 
            }
            
            if(check==0)
            {
            res[sizenow]=aux;
            sizenow++;
            }            
            }
            
            }
            
            char c;
            char d;
            char e;
            c = 91;
            d= 93;
            e=44;
            
            fout << "Case #" << i+1 << ": [" ;
            
            if(sizenow>0)
            {
            for(int j=0; j<sizenow-1; j++)
            fout << res[j]  << ", ";
            
            fout << res[sizenow-1] << "]" << endl;
            }
            else
            fout << "]" << endl;
            
          
            
            
            
                    
            }
             
            
            
            
            
            return 0;
            
        }
        
        

