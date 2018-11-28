#include<iostream>
using namespace std;
main()
{
 int t;
 cin>>t;
 for(int c=1;c<=t;c++)
 {
  char x[5][5],v;
  int done=0;
  for(int i=0;i<4;i++)
  cin>>x[i];
  int countdot=0,countO=0, countX=0, countT=0;
 
  for(int i=0;i<4;i++)
  {
   countO=0, countX=0, countT=0;
   for(int j=0;j<4;j++)
   {
     if(x[i][j]=='O') countO++;
     else if(x[i][j]=='T') countT++;
     else if(x[i][j]=='X') countX++;
     else countdot++;
   }
   if(countO+countT==4)
   {
    done=1;
    cout<<"Case #"<<c<<": "<<"O won"<<endl;
    break;
   }
   else if(countX+countT==4)
   {
    cout<<"Case #"<<c<<": "<<"X won"<<endl;
    done=1;
    break;
   }
  }
   if(done==1) continue;


   for(int i=0;i<4;i++)
   {
    countO=0, countX=0, countT=0;
    for(int j=0;j<4;j++)
    {
     if(x[j][i]=='O') countO++;
     else if(x[j][i]=='T') countT++;
     else if(x[j][i]=='X') countX++;
     else countdot++;
    }
    if(countO+countT==4)
    {
     done=1;
     cout<<"Case #"<<c<<": "<<"O won"<<endl;
     break;
    }
    else if(countX+countT==4)
    {
     cout<<"Case #"<<c<<": "<<"X won"<<endl;
     done=1;
     break;
    }
   }
    if(done==1) continue;
  
    countO=0; countT=0; countX=0;
    for(int i=0;i<4;i++)
    {
     if(x[i][i]=='O') countO++;
     else if(x[i][i]=='T') countT++;
     else if(x[i][i]=='X') countX++;
     else countdot++;
    }
    if(countO+countT==4)
    {
     done=1;
     cout<<"Case #"<<c<<": "<<"O won"<<endl;
    }
    else if(countX+countT==4)
    {
     cout<<"Case #"<<c<<": "<<"X won"<<endl;
     done=1;
    }
    if(done==1) continue;
  
    countO=0; countT=0; countX=0;
    for(int i=0;i<4;i++)
    {
     if(x[i][3-i]=='O') countO++;
     else if(x[i][3-i]=='T') countT++;
     else if(x[i][3-i]=='X') countX++;
     else countdot++;
    }
    if(countO+countT==4)
    {
     done=1;
     cout<<"Case #"<<c<<": "<<"O won"<<endl;
    }
    else if(countX+countT==4)
    {
     cout<<"Case #"<<c<<": "<<"X won"<<endl;
     done=1;
    }
    if(done==1) continue;
    else if(countdot==0)
     cout<<"Case #"<<c<<": "<<"Draw"<<endl;
    else
     cout<<"Case #"<<c<<": "<<"Game has not completed"<<endl;     
  }
 return 0;
}
 
