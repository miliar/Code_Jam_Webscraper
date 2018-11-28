#include<fstream>
#include<iostream>

using namespace std;
int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int t,count=0,check=1,dotcheck=0;
    char ch[4][4],ch1;
    fin>>t;
    while(t--)
    {
              check=1;
              dotcheck=0;
              count++;
              for(int i=0;i<4;i++)
              for(int j=0;j<4;j++)
              fin>>ch[i][j];
              fout<<"Case #"<<count<<": ";
              for(int i=0;i<4;i++)
              {
                      check=1;
                      if(ch[i][0]!='T')ch1=ch[i][0];
                      else ch1=ch[i][1];
                      for(int j=0;j<4;j++)
                      {
                              if((ch1==ch[i][j] || ch[i][j]=='T') && (ch1=='X' || ch1=='O')) continue;
                              else 
                              {
                                               check=0; 
                                               break; 
                              }
                      }
                      if(check==1)
                      break;
              }
              
              if(check!=1)
              {
              for(int i=0;i<4;i++)
              {
                      check=1;
                      if(ch[0][i]!='T')ch1=ch[0][i];
                      else ch1=ch[1][i];
                      for(int j=0;j<4;j++)
                      {
                              if((ch1==ch[j][i] || ch[j][i]=='T') && (ch1=='X' || ch1=='O')) continue;
                              else 
                              {
                                               check=0; 
                                               break; 
                              }
                      }
                      if(check==1)
                      break;
              }
              }
              
              if(check!=1)
              {
                          if((ch[0][0]=='T'||ch[0][0]=='X')&&(ch[1][1]=='T'||ch[1][1]=='X')&&(ch[2][2]=='T'||ch[2][2]=='X')&&(ch[3][3]=='T'||ch[3][3]=='X')) 
                          {
                          check=1;
                          ch1='X';
                          }
                          else if((ch[0][0]=='T'||ch[0][0]=='O')&&(ch[1][1]=='T'||ch[1][1]=='O')&&(ch[2][2]=='T'||ch[2][2]=='O')&&(ch[3][3]=='T'||ch[3][3]=='O'))
                          {
                          check=1;
                          ch1='O';
                          }
                          else if((ch[0][3]=='T'||ch[0][3]=='X')&&(ch[1][2]=='T'||ch[1][2]=='X')&&(ch[2][1]=='T'||ch[2][1]=='X')&&(ch[3][0]=='T'||ch[3][0]=='X')) 
                          {
                          check=1;
                          ch1='X';
                          }
                          if((ch[3][0]=='T'||ch[3][0]=='O')&&(ch[1][2]=='T'||ch[1][2]=='O')&&(ch[2][1]=='T'||ch[2][1]=='O')&&(ch[3][0]=='T'||ch[3][0]=='O'))
                          {
                          check=1;
                          ch1='O';
                          }
              }
                          
                          
              
              
              if(check==1)
              fout<<ch1<<" won"; 
              else
              {
                  for(int i=0;i<4;i++)
                  for(int j=0;j<4;j++)
                  if(ch[i][j]=='.')
                  dotcheck=1;
                  
                  if(dotcheck==1)
                  fout<<"Game has not completed";
                  else
                  fout<<"Draw";
              }
              fout<<endl;
    }
    return 0;
}
        
