#include <iostream>
#include <fstream>
using namespace std;
bool check_row(string tictac[4],int row)
{
  bool flag=true;
  char check=tictac[row][0];
  
  for(int i=1;i<4;i++)
  {
    if(tictac[row][i]=='.')return false;
    if(tictac[row][i]!='T'&&tictac[row][i]!=check){flag=false;break;}
    
  }
  // cout<<"flag["<<row<<"]="<<flag<<endl;
  return flag;
}
bool check_col(string tictac[4],int col)
{
  bool flag=true;
  char check=tictac[0][col];
  for(int i=1;i<4;i++)
  {
    if(tictac[i][col]=='.')return false;
    if(tictac[i][col]!='T'&&tictac[i][col]!=check){flag=false;break;}
  }
   //cout<<"flag["<<col<<"]="<<flag<<endl;
  return flag;
}
bool check_diag_left(string tictac[4])
{
   bool flag=true;
  char check=tictac[0][0];
   for(int i=1;i<4;i++)
   {
     if(tictac[i][i]=='.')return false;
     if(tictac[i][i]!='T'&&tictac[i][i]!=check){flag=false;break;}
   }
   return flag;
}
bool check_diag_right(string tictac[4])
{
   bool flag=true;
  char check=tictac[0][3];
   for(int i=1;i<4;i++)
   {
     if(tictac[i][3-i]=='.')return false;
     if(tictac[i][3-i]!='T'&&tictac[i][3-i]!=check){flag=false;break;}
   }
  
   return flag;
}

int main()
{
    
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("outputl.txt");
    int t;
    fin>>t;
  
     int case_no=1;
     string grbge;
     //-1 for undefined, 1 for X wins,2 for O wins
     while(t--)
     {   getline(fin,grbge);
        string tictac[4];
        int state=-1;
          bool blankcount = false;
        for(int i=0;i<4;i++)
        {
           getline(fin,tictac[i]);
          // cout<<tictac[i]<<endl; 
           if(tictac[i].find('.')!=string::npos)blankcount=true;           
        }
         fout<<"Case #"<<case_no++<<": ";
        for(int row=0;row<4;row++)
        {
          if(check_row(tictac,row)){state=(tictac[row][0]=='X')?1:2;break;}
        }
        if(state==-1)
        {
          for(int col=0;col<4;col++)
          {
            if(check_col(tictac,col)){state=(tictac[0][col]=='X')?1:2;break;}
          }
        }  
        if(state==-1)
        {
          if(check_diag_left(tictac)) {state=(tictac[0][0]=='X')?1:2;}  
          if(check_diag_right(tictac)){state=(tictac[3][0]=='X')?1:2;}
        }
       // cout<<"state="<<state<<endl;
        //cout<<"blankcount"<<blankcount<<endl;
        if(state==-1)
        {
          if(blankcount)fout<<"Game has not completed"<<endl;
          else fout<<"Draw"<<endl;
        }
        else
        {
          if(state==1)fout<<"X won"<<endl;
          else fout<<"O won"<<endl;
        }
         
             
     }
    // system("pause");       
 
 


}
