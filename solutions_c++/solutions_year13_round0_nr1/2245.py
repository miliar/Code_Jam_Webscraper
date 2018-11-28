        #include <fstream>
        #include <iostream>
        #include <string>
        #include <stdio.h>
        
        
        using namespace std;
        
        int main()
        {
            ofstream fout ("2011gcj1out.txt");
            ifstream fin ("2011gcj1in.txt");
            
            int t;
            int tie;
            char res;
            
            fin >> t;
            
            for(int i=0; i<t; i++)
            {
             
            tie = 1;
            res = 'T';  
            char data[16];
            int o[16];
            int x[16];
            
            for(int j=0; j<16;j++)
            fin >> data[j];
            
            
            
            for(int j=0; j<16;j++)
            {
            if(data[j]=='X')
            {
            x[j]=1;
            o[j]=0;
            }  
            if(data[j]=='O')
            {
            x[j]=0;
            o[j]=1;
            } 
            if(data[j]=='T')
            {
            x[j]=1;
            o[j]=1;
            } 
            if(data[j]=='.')
            {
            x[j]=0;
            o[j]=0;
            tie = 0;
            }       
            }
            
            for(int l=0;l<4;l++)
            if(x[4*l]==1&&x[4*l+1]==1&&x[4*l+2]==1&&x[4*l+3]==1)
            res = 'X';
            
            for(int l=0;l<4;l++)
            if(x[l]==1&&x[l+4]==1&&x[l+8]==1&&x[l+12]==1)
            res = 'X';
            
            if(x[0]==1&&x[5]==1&&x[10]==1&&x[15]==1)
            res = 'X';            
                      
            if(x[3]==1&&x[6]==1&&x[9]==1&&x[12]==1)
            res = 'X';
            
            for(int l=0;l<4;l++)
            if(o[4*l]==1&&o[4*l+1]==1&&o[4*l+2]==1&&o[4*l+3]==1)
            res = 'O';
            
            for(int l=0;l<4;l++)
            if(o[l]==1&&o[l+4]==1&&o[l+8]==1&&o[l+12]==1)
            res = 'O';
            
            if(o[0]==1&&o[5]==1&&o[10]==1&&o[15]==1)
            res = 'O';            
                      
            if(o[3]==1&&o[6]==1&&o[9]==1&&o[12]==1)
            res = 'O';
            
            if(res=='T')
            {
            if(tie==1)
            fout << "Case #" << i+1 << ": Draw" << endl;
            else
            fout << "Case #" << i+1 << ": Game has not completed" << endl;
            }
            else
            fout << "Case #" << i+1 << ": " << res << " won" << endl;
            
            } 
            
            
            
            
            return 0;
            
        }
        
        
