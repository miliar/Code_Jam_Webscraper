#include<iostream>
#include<fstream>
#include<string>
using namespace std;
char li(string line)
{  int xw=0,ow=0;
    
     
 //    cout << endl << line << endl;
    for(int i=0;i<4;i++)
    {if(line[i]=='X') 
      xw++;
      
    if(line[i]=='O') 
      ow++;
      if(line[i]=='T')
      {
                      xw++;
                      ow++;
      }
      }
 //     cout << xw << " " << ow << endl;
      if(xw==4)
      return 'X';
      if(ow==4)
      return 'O';
      return 'S';
    }
 
 
   

int main()
{
ifstream a;
    a.open("A-large.in");
    ofstream b;
    b.open("output.txt");
    int x,z=0;
    a>>x;
    for(int o=0;o<x;o++){b<<"Case #"<<o+1<<":"<<" ";
        char c[4][4],y;
       for(int i=0;i<4;i++)
       for(int j=0;j<4;j++)
       {
       a>>y;
       c[i][j]=y;
       }
        int done = 0;
   for(int k=0;k<4;k++){
           string line="";
           for(int j=0;j<4;j++)
           {
           line+=c[k][j];
           }
          char x;
        x=li(line);
        if(x=='X'){
        b<<"X won"<<endl;
        done = 1;
        break;
        }else if(x=='O')
        {b<<"O won"<<endl;
        done = 1;
        break;}
        }
        
     if(done)
             continue;
                
     for(int k=0;k<4;k++)
{
                       string line1="";
               for(int j=0;j<4;j++)
               {
               line1+=c[j][k];
               }
               char x;
            x=li(line1);
            if(x=='X')
            {b<<"X won"<<endl;
            done = 1;
            break;} 
            else
            if(x=='O')
            {b<<"O won"<<endl;
   done = 1;
            break;}
            }
            
            if(done)
                    continue;
string line2="";
   for(int m=0;m<4;m++)
   line2+=c[m][m];
    char x;
x=li(line2);
if(x=='X')
{b<<"X won"<<endl;
continue;} 
else
if(x=='O')
{b<<"O won"<<endl;
continue;}

string line3="";
   for(int m=3,n=0;m>=0;m--,n++)
   line3+=c[n][m];
   li(line3);
 char x1;
x1=li(line3);
if(x1=='X')
{b<<"X won"<<endl;
continue;} 
else
if(x1=='O')
{b<<"O won"<<endl;
continue;}

int flag=0;
for(int n=0;n<4;n++)
for(int q=0;q<4;q++)
if(c[n][q]=='.')
flag=1;
 if(flag == 1)
 b<<"Game has not completed";
 else
 b<<"Draw";
 b<< endl;
}
}
