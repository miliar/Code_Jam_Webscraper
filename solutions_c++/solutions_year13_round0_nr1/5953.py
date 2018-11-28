#include<iostream>
#include<conio.h>
#include<math.h>
#include<string>
#include<algorithm>
#include<map>
#include<vector>
#include<array>
#include<fstream>
#include<sstream>

using namespace std;

ifstream myfilein;
ofstream myfileout;
string line;	
bool myfunction (long long i,long long j) { return (i>j); }


void open2()
  {
    freopen("test1.in", "rt", stdin);
   freopen("test1.out", "wt", stdout);
  }  



string IntToStr(int& s )
  {
  string result;
	result = s;
  return result;
  } 

char line1[4][4];
string line2;
int cnt,cnt2,T;
void main()
	{ 
	open2();
	
	
	

	cin>>T;
	for (int i = 1; i <=T; i++)
	{

	for (int j = 0; j <4; j++)
	{
	for (int k = 0; k <4; k++)
	{
		cin>>line1[j][k];
	}	
	}
	
	
	cnt=0;

/// horizontal X
	for (int j = 0; j <4; j++)
	{
	cnt=0;
	cnt2=0;
	for (int k = 0; k <4; k++)
	{
		if ((line1[j][k]=='X') || (line1[j][k]=='T')) 
		{
		cnt=cnt+1;
		}


		
		if ((line1[j][k]=='O') || (line1[j][k]=='T')) 
		{
		cnt2=cnt2+1;
		}

		if(cnt==4)
		{
			cout<<"Case #"<<i<<": "<<"X won";
			goto next;
		}
				
		if(cnt2==4)
		{
			cout<<"Case #"<<i<<": "<<"O won";
			goto next;
		}
	}	
	}
	cnt=0;
//vertical X
	for (int j = 0; j <4; j++)
	{
	cnt=0;
	cnt2=0;
	for (int k = 0; k <4; k++)
	{
		if ((line1[k][j]=='X') || (line1[k][j]=='T')) 
		{
		cnt=cnt+1;
		}



		if ((line1[k][j]=='O') || (line1[k][j]=='T')) 
		{
		cnt2=cnt2+1;
		}

		if(cnt==4)
		{
			cout<<"Case #"<<i<<": "<<"X won";
			goto next;
		}
		if(cnt2==4)
		{
			cout<<"Case #"<<i<<": "<<"O won";
			goto next;
		}
	}
	}
	cnt=0;
//diagonal 1 X
	cnt=0;
	cnt2=0;
	for (int j = 0; j <4; j++)
	{
	
	
		if ((line1[j][j]=='X') || (line1[j][j]=='T')) 
		{
		cnt=cnt+1;
		}
		if(cnt==4)
		{
			cout<<"Case #"<<i<<": "<<"X won";
			goto next;
		}
		if ((line1[j][j]=='O') || (line1[j][j]=='T')) 
		{
		cnt2=cnt2+1;
		}
		if(cnt2==4)
		{
			cout<<"Case #"<<i<<": "<<"O won";
			goto next;
		}
	}
	cnt=0;
	cnt2=0;
	//diagonal 2 X
	for (int j = 3; j >=0; j--)
	{
	
	
		if ((line1[3-j][j]=='X') || (line1[3-j][j]=='T')) 
		{
		cnt=cnt+1;
		}

		if(cnt==4)
		{
			cout<<"Case #"<<i<<": "<<"X won";
			goto next;
		}
		
		if ((line1[3-j][j]=='O') || (line1[3-j][j]=='T')) 
		{
		cnt2=cnt2+1;
		}
		if(cnt2==4)
		{
			cout<<"Case #"<<i<<": "<<"O won";
			goto next;
		}
	}
cnt=0;
	/// horizontal .
for (int j = 0; j<4; j++)
{
	for (int k = 0; k<4; k++)
	{
		if ((line1[j][k]=='X') || (line1[j][k]=='T') || (line1[j][k]=='O') ) 
		{
		cnt=cnt+1;
		}
		if (cnt==16)
		{
			cout<<"Case #"<<i<<": "<<"Draw";
			goto next;
		}

	}	

}	

	
	
			cout<<"Case #"<<i<<": "<<"Game has not completed";
			goto next;
	


	next:
	cout<<endl;
 

	}





	



	//_getch();
	}