#include<iostream>
#include<fstream>
#include<string>
using namespace std;
char f1(string l);
int main()
{
 ifstream inn("A-large (1).in");
 ofstream cc("output.txt");
    int H,flag1=0;
    inn>>H;
    for(int o=1;o<=H;o++)
	{
 	
     char c[4][4],y;
     for(int i=0;i<4;i++)
      for(int j=0;j<4;j++)
       {
       inn>>c[i][j];
       }
        int f=0;
     for(int k=0;k<4;k++){
           string l2="";
           for(int j=0;j<4;j++)
           {
           l2+=c[k][j];
           }
          char x;
        x=f1(l2);
        if(x=='X'){
        cc<<"Case #"<<o<<":"<<" "<<"X won"<<endl;
        f=1;
        break;
        }
		else
		if(x=='O')
        {cc<<"Case #"<<o<<":"<<" "<<"O won"<<endl;
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
            x=f1(l1);
            if(x=='X')
            {cc<<"Case #"<<o<<":"<<" "<<"X won"<<endl;
            f=1;
            break;} 
            else
            if(x=='O')
            {cc<<"Case #"<<o<<":"<<" "<<"O won"<<endl;
   		f=1;
            break;}
            }
            
            if(f)
                    continue;
string l2="";
   for(int m=0;m<4;m++)
   l2+=c[m][m];
    char x;
x=f1(l2);
if(x=='X')
{cc<<"Case #"<<o<<":"<<" "<<"X won"<<endl;
continue;} 
else
if(x=='O')
{cc<<"Case #"<<o<<":"<<" "<<"O won"<<endl;
continue;}

string l3="";
   for(int i=0;i<4;i++)
   {for(int j=0;j<4;j++) 
     if(i+j==3)
	 l3+=c[i][j];
   }
   f1(l3);
 char x1;
x1=f1(l3);
if(x1=='X')
{cc<<"Case #"<<o<<":"<<" "<<"X won"<<endl;
continue;} 
else
if(x1=='O')
{cc<<"Case #"<<o<<":"<<" "<<"O won"<<endl;
continue;}

int flag=0;
for(int n=0;n<4;n++)
for(int q=0;q<4;q++)
if(c[n][q]=='.')
flag=1;
 if(flag == 1)
cc<<"Case #"<<o<<":"<<" "<<"Game has not completed";
 else
 cc<<"Case #"<<o<<":"<<" "<<"Draw";
 cc<< endl;
}
}

char f1(string l)
{  int x=0,o=0,i=0; 
    while(i<4)
    {if(l[i]=='X') 
      x++;      
    if(l[i]=='O') 
      o++;
      if(l[i]=='T')
      { x++;
        o++;
      }
      i++;
      }
      if(o==4)
      return 'O';
      if(x==4)
      return 'X';
      return 'N';
    }