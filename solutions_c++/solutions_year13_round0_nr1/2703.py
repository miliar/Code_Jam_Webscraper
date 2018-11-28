#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream fin;
    fin.open("input.txt");
    ofstream fout;
    fout.open("output.txt");
    int t,l=0;
    fin>>t;
    while(t--)
    {
              l++;
              bool X=false,O=false;
              char ch[4][4];
              for(int i=0;i<4;i++)
                      for(int j=0;j<4;j++)
                              fin>>ch[i][j];
              int ct=0;
              for(int i=0;i<4;i++)
              {
                      int x=0,o=0,T=0;
                      for(int j=0;j<4;j++)
                      {
                              if(ch[i][j]=='X')
                                     x++;
                              else if(ch[i][j]=='O')
                                     o++;
                              else if(ch[i][j]=='T')
                                     T++; 
                              else
                                     ct++;                      
                      }
                      //cout<<x<<" "<<o<<" "<<T<<endl;
                      if(x==4 || (x==3 && T==1))
                              X=true;
                      else if(o==4 || (o==3 && T==1))
                              O=true;
                      
              }
              for(int j=0;j<4;j++)
              {
                      int x=0,o=0,T=0;
                      for(int i=0;i<4;i++)
                      {
                              if(ch[i][j]=='X')
                                     x++;
                              else if(ch[i][j]=='O')
                                     o++;
                              else if(ch[i][j]=='T')
                                     T++;                 
                      }
                      if(x==4 || (x==3 && T==1))
                              X=true;
                      else if(o==4 || (o==3 && T==1))
                              O=true;
                      
              }
              int i=0,j=0,x=0,o=0,T=0;;
              for(int p=0;p<4;p++)
              {
                      if(ch[i][j]=='X')
                                     x++;
                      else if(ch[i][j]=='O')
                                     o++;
                      else if(ch[i][j]=='T')
                                     T++;
                      i++;
                      j++;
                                     
              }
              if(x==4 || (x==3 && T==1))
                              X=true;
              else if(o==4 || (o==3 && T==1))
                              O=true;  
              i=0,j=3,x=0,o=0,T=0;;
              for(int p=0;p<4;p++)
              {
                      if(ch[i][j]=='X')
                                     x++;
                      else if(ch[i][j]=='O')
                                     o++;
                      else if(ch[i][j]=='T')
                                     T++;
                      i++;
                      j--;
                                     
              }
              if(x==4 || (x==3 && T==1))
                              X=true;
              else if(o==4 || (o==3 && T==1))
                              O=true;
              if(X==true)
                         fout<<"Case #"<<l<<": X won\n";
              else if(O==true)
                         fout<<"Case #"<<l<<": O won\n";
              else if(ct==0)
                         fout<<"Case #"<<l<<": Draw\n";
              else
                         fout<<"Case #"<<l<<": Game has not completed\n"; 
    }   
    fin.close();
    fout.close();         
    return 0;
}
              
              
    
