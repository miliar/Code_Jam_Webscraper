#include<iostream>
#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<fstream>
#include<string.h>
#include<ctype.h>
using namespace std;
class BT
{
  private:
    int bseq[200][700], oseq[200][700], op, bp, ntc, nbp[700];
	char seq[200][700];
  public:
	 void read(ifstream &f1, ofstream &f2);
	 void func(ofstream &f2);
	 void writ(int n, int t, ofstream &f2);
};
void BT::writ(int n, int t, ofstream &f2)
{
     f2.write("Case #", 6);
     f2<<n+1;
     f2.write(": ", 2);
     f2<<t;
     f2.write("\n", 1);
}
void BT::read(ifstream &f1, ofstream &f2)
{
     ntc=0;
     char ch, temp[500], line[200][700], tseq[200][700];
     int tc, i, j=0,k=0,p=0,q=0;
     f1.get(ch);
     while(ch!='\n')
     {
      ntc = (ntc*10)+(ch - '0') ;
     f1.get(ch);
     }
     for(int w=0;w<200;w++)
      for(int v=0;v<200;v++)
      {
              bseq[w][v]='\0';
              oseq[w][v]='\0';
              seq[w][v]='\0';
      }
     while(!f1.eof())
     {
         for(i=0;i<ntc;i++)
         {
                           f1.getline(line[i], 700);
         }
     }
     for(i=0;i<ntc;i++)
     {
        nbp[i]=line[i][0]-'0';
        for(int x =1; line[i][x]!='\0';x++)
        {
                if(isalnum(line[i][x]))
                {
                                       
                                       if(isalpha(line[i][x]))
                                       {
                                                             seq[i][k]=line[i][x];
                                                             k++;
                                       }
                                       if(!isalpha(line[i][x]))
                                       {
                                          if(!isalpha(line[i][x-1]) && line[i][x-1]!=' ')
                                          {     
                                                               int y=x;
                                                               while(!isalpha(line[i][y]))
                                                                y--;
                                                               if(line[i][y]=='B')
                                                               { 
                                                                bseq[i][p-1]=(bseq[i][p-1]*10)+(line[i][x]-'0');
                                                               } 
                                                               else
                                                               {
                                                                oseq[i][q-1]=(oseq[i][q-1]*10)+(line[i][x]-'0');
                                                               }
                                          }
                                          else
                                          {
                                                               int y=x;
                                                               while(!isalpha(line[i][y]))
                                                                y--;
                                                               if(line[i][y]=='B')
                                                               { 
                                                                bseq[i][p]=line[i][x]-'0';
                                                                p++;
                                                               } 
                                                               else
                                                               {
                                                                oseq[i][q]=line[i][x]-'0';
                                                                q++;
                                                               }
                                                               
                                          }                                                            
                                       } 
                }
        }
          k=0;
          p=0;
          q=0;
}//for ntc
     func(f2);
}
void BT::func(ofstream &f2)
{

    int bcp, ocp;
    int i,j,k, btime, x=0, count=0;
    bcp=1;
    ocp=1;
    for(x;x<ntc;x++)
    {
                    bcp=1;
                    ocp=1;
                    bool flag=0;
                    btime=0;
                    i=0;
                    j=0;
                    k=0;
                    int bd, od;
                    bd= abs(bcp-bseq[x][j]);
                    od= abs(ocp-oseq[x][k]);
                    while(seq[x][i]!='\0')
                    {
                            flag=0;
                            if(seq[x][i]=='B')
                            {
                                              if(bd==0)
                                              {
                                                
                                                i++;
                                                btime++;
                                                bcp=bseq[x][j];
                                                j++;
                                                bd= abs(bcp-bseq[x][j]);
                                                if(od>0)
                                                {
                                                  od--;
                                                }
                                                continue;
                                               }
                                             
                                           
                            }
                            else if(seq[x][i]=='O')
                            {
                                              if(od==0)
                                              {
                                                i++;
                                                btime++;
                                                ocp=oseq[x][k];
                                                k++;
                                                od= abs(ocp-oseq[x][k]);
                                                if(bd>0)
                                                {
                                                  bd--;
                                                }
                                                continue;
                                              }
                            }
                            if(bd>0)
                                                {
                                                  bd--;
                                                }
                             if(od>0)
                                               {
                                                   od--;
                                               }
                            btime++;
                    }
                    writ(x, btime, f2);
    }
 
}     
     
     
     
     
int main()
{
    //ifstream f1("A-small-attempt0.in");
    ifstream f1("A-large.in");
    ofstream f2("result.txt");
    BT obj;
    obj.read(f1,f2);
    f2.close();
    f1.close();
    return 0;
}
                 
