#include<iostream>
#include<fstream>
#include<string>
using namespace std;
char fun(string l)
{  int x=0,o=0; 
    for(int i=0;i<4;i++)
    {if(l[i]=='X') 
      x++;      
    if(l[i]=='O') 
      o++;
      if(l[i]=='T')
      { x++;
        o++;
      }
      }
      if(o==4)
      return 'O';
      if(x==4)
      return 'X';
      return 'N';
    }
 
 
   

int main()
{
 ifstream in("A-large.in");
 ofstream out("output.txt");
    int x,flag1=0;
    in>>x;
    for(int o=0;o<x;o++)
	{
	 out<<"Case #"<<o+1<<":"<<" ";
     char c[4][4],y;
     for(int i=0;i<4;i++)
      for(int j=0;j<4;j++)
       {
       in>>c[i][j];
       }
        int f=0;
     for(int k=0;k<4;k++){
           string l2="";
           for(int j=0;j<4;j++)
           {
           l2+=c[k][j];
           }
          char x;
        x=fun(l2);
        if(x=='X'){
        out<<"X won"<<endl;
        f=1;
        break;
        }
		else
		if(x=='O')
        {out<<"O won"<<endl;
        f=1;
        break;}
        }
        
     if(f)
      continue;
                
     for(int k=0;k<4;k++)
{
              string l1="";
               for(int j=0;j<4;j++)
               {
               l1+=c[j][k];
               }
               char x;
            x=fun(l1);
            if(x=='X')
            {out<<"X won"<<endl;
            f=1;
            break;} 
            else
            if(x=='O')
            {out<<"O won"<<endl;
   		f=1;
            break;}
            }
            
            if(f)
                    continue;
string l2="";
   for(int m=0;m<4;m++)
   l2+=c[m][m];
    char x;
x=fun(l2);
if(x=='X')
{out<<"X won"<<endl;
continue;} 
else
if(x=='O')
{out<<"O won"<<endl;
continue;}

string l3="";
   for(int i=0;i<4;i++)
   {for(int j=0;j<4;j++) 
     if(i+j==3)
	 l3+=c[i][j];
   }
   fun(l3);
 char x1;
x1=fun(l3);
if(x1=='X')
{out<<"X won"<<endl;
continue;} 
else
if(x1=='O')
{out<<"O won"<<endl;
continue;}

int flag=0;
for(int n=0;n<4;n++)
for(int q=0;q<4;q++)
if(c[n][q]=='.')
flag=1;
 if(flag == 1)
out<<"Game has not completed";
 else
 out<<"Draw";
 out<< endl;
}
}
