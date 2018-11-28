#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int T,i,j,k,countx,counto,countt,dot;
    char a[4][4];
    ifstream fin;
    ofstream fout;
    fout.open("tttt.out");  
    fin.open("tttt.in.txt");
    fin>>T;
    for(k=0;k<T;k++)
    {
                    dot=0;
    
                    for(i=0;i<4;i++)
                    {
                                   countx=counto=countt=0;
                                   for(j=0;j<4;j++)
                                   {
                                   fin>>a[i][j];
                                   //fout<<a[i][j];
                                   }
                                  // fout<<endl;
                    }
                    for(i=0;i<4;i++)
                    {
                                    countx=0;
                                    counto=0;
                                    countt=0;
                                    for(j=0;j<4;j++)
                                    {                              
                                                  if(a[i][j]=='X')
                                                  countx=countx+1;
                                                  else if (a[i][j]=='O')
                                                  counto++;
                                                  else if (a[i][j]=='T')
                                                  countt++;
                                                  else 
                                                  dot++;
                                   }//fout <<"number of x="<< countx<<endl;
                                   if(countx +countt==4)
                                   {
                                               fout<<"Case #"<<k+1<<": X won\n";
                                               goto next;
                                   }
                                   else if(counto==4 || (counto==3 && countt==1))
                                   {
                                       fout<<"Case #"<<k+1<<": O won\n";
                                       goto next;
                                   }
                    }
                    
                    for(j=0;j<4;j++)
                    {
                                   countx=counto=countt=0;
                                   for(i=0;i<4;i++)
                                   {
                                                  if(a[i][j]=='X')
                                                  countx++;
                                                  else if (a[i][j]=='O')
                                                  counto++;
                                                  else if (a[i][j]=='T')
                                                  countt++;
                                                  else 
                                                  dot++;
                                   }
                                   if(countx==4 ||(countx==3 && countt==1))
                                   {
                                               fout<<"Case #"<<k+1<<": X won\n";
                                               goto next;
                                   }
                                   else if(counto==4 || (counto==3 && countt==1))
                                   {
                                       fout<<"Case #"<<k+1<<": O won\n";
                                       goto next;
                                   }
                    }     
                    countx=counto=countt=0;
                    for(i=0,j=0;i<4;i++,j++)
                    {
                                                  if(a[i][j]=='X')
                                                  countx++;
                                                  else if (a[i][j]=='O')
                                                  counto++;
                                                  else if (a[i][j]=='T')
                                                  countt++;
                                                  else 
                                                  dot++;
                    }
                    if(countx==4 ||(countx==3 && countt==1))
                    {
                                 fout<<"Case #"<<k+1<<": X won\n";
                                 goto next;
                    }
                    else if(counto==4 || (counto==3 && countt==1))
                    {
                         fout<<"Case #"<<k+1<<": O won\n";
                         goto next;
                    }
                    countx=counto=countt=0;
                    for(i=0,j=3;i<4;i++,j--)
                    {
                                                  if(a[i][j]=='X')
                                                  countx++;
                                                  else if (a[i][j]=='O')
                                                  counto++;
                                                  else if (a[i][j]=='T')
                                                  countt++;
                                                  else 
                                                  dot++;
                    }
                    if(countx==4 ||(countx==3 && countt==1))
                    {
                                 fout<<"Case #"<<k+1<<": X won\n";
                                 goto next;
                    }
                    else if(counto==4 || (counto==3 && countt==1))
                    {
                         fout<<"Case #"<<k+1<<": O won\n";
                         goto next;
                    }
                    if(dot>0)
                    fout<<"Case #"<<k+1<<": Game has not completed\n";
                    else
                    fout<<"Case #"<<k+1<<": Draw\n";
                    next:;
    }
    fout.close();
    fin.close();
    return(0);
}
                     
