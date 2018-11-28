        #include <fstream>
        #include <iostream>
        #include <string>
        #include <stdio.h>
        
        
        using namespace std;
        
        int main()
        {
            ofstream fout ("2011gcj1.txt.txt");
            ifstream fin ("2011gcj1.in.txt");
            
            int t;
            int n;
            int end;
            int aux, auy;
            
            fin >> t;
            
            int res;
            
            
            for(int i=0; i<t; i++)
            {
            
            auy=0;
            res=0;
            fin >> n;
            
            int d[n];
            int l[n];
            int b[n];
            
            for(int j=0; j<n; j++)
            b[j]=0;
            
            for(int j=0; j<n; j++)
            {
            fin >> d[j];
            fin >> l[j];
            }
            
            fin >> end;
            
            b[0] = d[0];
            
            for(int j=1; j<n; j++)
            {
            aux = 0;
            
            for(int k=0; k<j; k++)
            {
            if(b[k]+d[k] >= d[j])
            {
            if(d[j]-d[k] > l[j])
            b[j] = l[j];
            else
            b[j] = d[j]-d[k];
            
            aux=1;
            break;
            }
            }
            
            if(aux==0)
            {
            auy = 1;
            break;
            }
            }
            
            //for(int j=0; j<n; j++)
            //fout << b[j] << endl;
            
            if(auy==1)
            fout << "Case #" << i+1 << ": " << "NO" << endl;
            else
            {
            for(int j=0; j<n; j++)
            if(d[j]+b[j] >= end)
            res=1;
            
            if(res==1)
            fout << "Case #" << i+1 << ": " << "YES" << endl;
            else
            fout << "Case #" << i+1 << ": " << "NO" << endl;
            }
            }
            
                        
            
            
            
            
            
            return 0;
            
        }
        
        
