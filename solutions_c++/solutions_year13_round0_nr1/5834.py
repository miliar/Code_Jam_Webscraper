#include<iostream> 
using namespace std;
int main()
{
  int c=0,t;
  char A[5][5];
  bool flag=0;
  int count_dot=0,count_o=0,count_x=0;
  cin >> t;
  
  while(t--)
  {
   flag=0;
  count_dot=0; 
    c++;
    for(int i=0;i<=3;i++) cin >> A[i];
    
    for(int i=0;i<4;i++)
    {
      for(int j=0;j<4;j++) 
      {
	if(A[i][j]=='.') count_dot++;
      }
      
    }
    
    for(int i=0;i<4;i++)
    {
      count_o=0;
      count_x=0;
      for(int j=0;j<4;j++)
      { 
	if(A[i][j]=='X') count_x++;
	else if (A[i][j]=='O') count_o++;
	else if(A[i][j]=='T'){count_o++;count_x++;}
	if(count_x==4) {cout << "Case #"<<c<<": X won"<<endl;flag=1;break;}
	else if(count_o==4) {cout << "Case #"<<c<<": O won"<<endl;flag=1;break;}
      }
      if(flag) break;
    }
    for(int j=0;j<4;j++)
    {
      count_o=0;
      count_x=0;
      for(int i=0;i<4;i++)
      {
	if(A[i][j]=='X') count_x++;
	else if(A[i][j]=='O') count_o++;
	else if(A[i][j]=='T'){count_o++;count_x++;}
	if(count_x==4) {cout << "Case #"<<c<<": X won"<<endl;flag=1;break;}
	else if(count_o==4) {cout << "Case #"<<c<<": O won"<<endl;flag=1;break;}
      }
      if(flag) break;
    }
    count_o=0;
    count_x=0;
    for(int i=0;i<4;i++)
    {
      for(int j=i;j<i+1;j++)
      {
	if(A[i][j]=='X') count_x++;
	else if(A[i][j]=='O') count_o++;
	else if(A[i][j]=='T'){count_o++;count_x++;}
	if(count_x==4) {cout << "Case #"<<c<<": X won"<<endl;flag=1;break;}
	else if(count_o==4) {cout << "Case #"<<c<<": O won"<<endl;flag=1;break;}
      }
      if(flag) break;
    }
    
     count_o=0;
     count_x=0;
    for(int i=0;i<4;i++)
    {
      for(int j=3-i;j>=3-i;j--)
      {
	if(A[i][j]=='X') count_x++;
	else if(A[i][j]=='O') count_o++;
	else if(A[i][j]=='T'){count_o++;count_x++;}
	if(count_x==4) {cout << "Case #"<<c<<": X won"<<endl;flag=1;break;}
	else if(count_o==4) {cout << "Case #"<<c<<": O won"<<endl;flag=1;break;}
	
      }
      if(flag) break;
    }
    if(flag==0&&count_dot==0) cout << "Case #"<<c<<": Draw"<<endl;
    else if(flag==0&&count_dot>0) cout << "Case #"<<c<<": Game has not completed"<<endl;
  }
  return 0;
}
