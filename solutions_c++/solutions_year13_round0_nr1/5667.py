#include<map>
#include<iostream>
#include<stack>
#include<queue>
#include<vector>
#include<algorithm>
#include<set>
#include<cstring>
#include<climits>
#include<cmath>
#include<cstdio>

using namespace std;

int main()
{

  //......file input/output
  //
  ///.................

  int t;
  scanf("%d",&t);
  for(int tt=0;tt<t;tt++)
    {
      string a[4];
      
      cin>>a[0];
      cin>>a[1];
      cin>>a[2];
      cin>>a[3];
      
      int res=3;
      int status=-1;
      char now;
      bool flag=true;

      // row 0
      if(status==-1&&a[0][0]!='.')
	{
	  if(a[0][0]=='T')
	    {
	      now=a[0][1];
	      if(a[0][2]==a[0][3]&&a[0][3]==now)
		if(now=='X')
		  {status=2;}//cout<<"row0:2\n";}
		else
		  {status=1;}//cout<<"row0:1\n";}
	      //status=1;
	    }
	  else
	    {
	      now=a[0][0];
	      flag=true;
	      for(int i=1;i<4;i++)
		if(a[0][i]!=now&&a[0][i]!='T')
		  {flag=false;break;}
	      if(flag)
		if(now=='X')
		  {status=2;}//cout<<"row0:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"row0:1\n";}
	      //status=1;
	    }
	}
      //row 1
      if(status==-1&&a[1][0]!='.')
	{
	  if(a[1][0]=='T')
	    {
	      now=a[1][1];
	      if(a[1][2]==a[1][3]&&a[1][3]==now)
		if(now=='X')
		  {status=2;}//cout<<"row1:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"row1:1\n";}
		/*
		if(now=='X')
		  status=2;
		else
		  status=1;
		*/
	    }
	  else
	    {
	      now=a[1][0];
	      flag=true;
	      for(int i=1;i<4;i++)
		if(a[1][i]!=now&&a[1][i]!='T')
		  {flag=false;break;}
	      if(flag)
		if(now=='X')
		  {status=2;}//cout<<"row1:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"row1:1\n";}

		/*
		if(now=='X')
		  status=2;
		else
		  status=1;
		*/
	    }
	}
	  // row 2
      if(status==-1&&a[2][0]!='.')
	{
	  if(a[2][0]=='T')
	    {
	      now=a[2][1];
	      if(a[2][2]==a[2][3]&&a[2][3]==now)
		if(now=='X')
		  {status=2;}//cout<<"row2:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"row2:1\n";}

		/*
		if(now=='X')
		  status=2;
		else
		  status=1;
		*/
	    }
	  else
	    {
	      now=a[2][0];
	      flag=true;
	      for(int i=1;i<4;i++)
		if(a[2][i]!=now&&a[2][i]!='T')
		  {flag=false;break;}
	      if(flag)
		if(now=='X')
		  {status=2;}//cout<<"row2:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"row2:1\n";}
	      /*
		if(now=='X')
		  status=2;
		else
		  status=1;
	      */
	    }
	}
      // row 3
      if(status==-1&&a[3][0]!='.')
	{
	  if(a[0][0]=='T')
	    {
	      now=a[3][1];
	      if(a[3][2]==a[3][3]&&a[3][3]==now)
		if(now=='X')
		  {status=2;}//cout<<"row3:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"row3:1\n";}
	      /*
		if(now=='X')
		  status=2;
		else
		  status=1;
	      */
	    }
	  else
	    {
	      now=a[3][0];
	      flag=true;
	      for(int i=1;i<4;i++)
		if(a[3][i]!=now&&a[3][i]!='T')
		  {flag=false;break;}
	      if(flag)
				if(now=='X')
		  {status=2;}//cout<<"row3:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"row3:1\n";}
	      /*
		if(now=='X')
		  status=2;
		else
		  status=1;
	      */
	    }
	}

      // col0
      if(status==-1&&a[0][0]!='.')
	{
	  if(a[0][0]=='T')
	    {
	      now=a[1][0];
	      if(a[2][0]==a[3][0]&&a[3][0]==now)
		if(now=='X')
		  {status=2;}//cout<<"row00:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"row00:1\n";}
	      /*
		if(now=='X')
		  status=2;
		else
		  status=1;
	      */
	    }
	  else
	    {
	      now=a[0][0];
	      flag=true;
	      for(int i=1;i<4;i++)
		if(a[i][0]!=now&&a[i][0]!='T')
		  {flag=false;break;}
	      if(flag)
		if(now=='X')
		  {status=2;}//cout<<"row00:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"row00:1\n";}
	      /*
		if(now=='X')
		  status=2;
		else
		  status=1;
	      */
	    }
	}

      //col1
      if(status==-1&&a[0][1]!='.')
	{
	  if(a[0][1]=='T')
	    {
	      now=a[1][1];
	      if(a[2][1]==a[3][1]&&a[3][1]==now)
		if(now=='X')
		  {status=2;}//cout<<"row01:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"row01:1\n";}
	      /*
		if(now=='X')
		  status=2;
		else
		  status=1;
	      */
	    }
	  else
	    {
	      now=a[0][1];
	      flag=true;
	      for(int i=1;i<4;i++)
		if(a[i][1]!=now&&a[i][1]!='T')
		  {flag=false;break;}
	      if(flag)
		if(now=='X')
		  {status=2;}//cout<<"row01:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"row01:1\n";}
	      /*
		if(now=='X')
		  status=2;
		else
		  status=1;
	      */
	    }
	}

      //col2
      if(status==-1&&a[0][2]!='.')
	{
	  if(a[0][2]=='T')
	    {
	      now=a[1][2];
	      if(a[2][2]==a[3][2]&&a[3][2]==now)
		if(now=='X')
		  {status=2;}//cout<<"row02:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"row02:1\n";}
	      /*
		if(now=='X')
		  status=2;
		else
		  status=1;
	      */
	    }
	  else
	    {
	      now=a[0][2];
	      flag=true;
	      for(int i=1;i<4;i++)
		if(a[i][2]!=now&&a[i][2]!='T')
		  {flag=false;break;}
	      if(flag)
		if(now=='X')
		  {status=2;}//cout<<"row02:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"row02:1\n";}
	      /*
		if(now=='X')
		  status=2;
		else
		  status=1;
	      */
	    }
	}

      //col3
      if(status==-1&&a[0][3]!='.')
	{
	  if(a[0][3]=='T')
	    {
	      now=a[1][3];
	      if(a[2][3]==a[3][3]&&a[3][3]==now)
		if(now=='X')
		  {status=2;}//cout<<"row03:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"row03:1\n";}
	      /*
		if(now=='X')
		  status=2;
		else
		  status=1;
	      */
	    }
	  else
	    {
	      now=a[0][3];
	      flag=true;
	      for(int i=1;i<4;i++)
		if(a[i][3]!=now&&a[i][3]!='T')
		  {flag=false;break;}
	      if(flag)
		if(now=='X')
		  {status=2;}//cout<<"row03:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"row03:1\n";}
	      /*
		if(now=='X')
		  status=2;
		else
		  status=1;
	      */
	    }
	}
      //d1 
	  if(status==-1&&a[0][0]!='.')
	    {
	      if(a[0][0]=='T')
		{
		  now=a[1][1];
		  if(a[2][2]==a[3][3]&&a[3][3]==now)
		if(now=='X')
		  {status=2;}//cout<<"d1:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"d1:1\n";}
		  /*
		    if(now=='X')
		      status=2;
		    else
		      status=1;
		  */
		}
	      else
		{
		  now=a[0][0];
		  if((a[1][1]==now||a[1][1]=='T')&&(a[2][2]==now||a[2][2]=='T')&&(a[3][3]==now||a[3][3]=='T'))
		    		if(now=='X')
		  {status=2;}//cout<<"d1:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"d1:1\n";}
		    /*
		    if(now=='X')
		      status=2;
		    else
		      status=1;
		    */
		}
	    }
	  //d2
	  if(status==-1&&a[0][3]!='.')
	    {
	      if(a[0][3]=='T')
		{
		  now=a[1][2];
		  if(a[2][1]==a[3][0]&&a[3][0]==now)
		if(now=='X')
		  {status=2;}//cout<<"d2:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"d2:1\n";}
		  /*
		    if(now=='X')
		      status=2;
		    else
		      status=1;
		  */
		}
	      else
		{
		  now=a[0][3];
		  if((a[1][2]==now||a[1][2]=='T')&&(a[2][1]==now||a[2][1]=='T')&&(a[3][0]==now||a[3][0]=='T'))
		if(now=='X')
		  {status=2;}//cout<<"d2:2\n";}
	      //status=2;
		else
		  {status=1;}//cout<<"d2:1\n";}
		  /*
		    if(now=='X')
		      status=2;
		    else
		      status=1;
		  */
		}
	    }
	  
	  int cool=0;
	  for(int i=0;i<4;i++)
	    for(int j=0;j<4;j++)
	      if(a[i][j]=='.')
		cool++;


      cout<<"Case #"<<tt+1<<": ";
      //...cout answer here
      if(status==1)
	cout<<"O won\n";
      else if(status==2)
	cout<<"X won\n";
      else
	{
	  if(cool)
	    cout<<"Game has not completed\n";
	  else
	    cout<<"Draw\n";
	}
      
      
	}
      
      


  return 0;
}
