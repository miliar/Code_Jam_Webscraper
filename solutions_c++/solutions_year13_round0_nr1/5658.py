#include <iostream>
#include <fstream>
using namespace std;
bool check4 (char arr[4][4],char& temp)
{
	int count;
	int m,n;
	//check for rows
	for(m=0;m<4;m++)
	{	count =1;
		temp=arr[m][0];
		if(temp!='.') 
		{
		for(n=1;n<4;n++)
			{
				if(arr[m][n]!=temp&&arr[m][n]!='T')
				break;
			    else count ++;
		   
		        if(count==4)
				return true;
		    }
		}
	}
	//check for colomn
	for(m=0;m<4;m++)
	{	count =1;
		temp=arr[0][m];
		if(temp!='.') 
		{
			for(n=1;n<4;n++)
			{
				if(arr[n][m]!=temp&&arr[n][m]!='T')
				break;
			    else count ++;
		   
		        if(count==4)
				return true;
		    }
		}
     }
	//chek for diagonal
	temp=arr[0][0];
	count =1;
	if(temp!='.') 
	{
		for(m=1;m<4;m++)
		{
				if(arr[m][m]!=temp&&arr[m][m]!='T')
				break;
			    else count ++;
		   
		        if(count==4)
				return true;
		 }
	}
	//check for other diagonal 
	temp=arr[0][3];
	count =1;
	if(temp!='.') 
	{
	for(m=1;m<4;m++)
		{
				if(arr[m][3-m]!=temp&&arr[m][3-m]!='T')
				break;
			    else count ++;
		   
		        if(count==4)
				return true;
		 }
	}
	return false;

}
bool check(char arr[4][4])
{
	int n,m;
	for(n=0;n<4;n++)
		for(m=0;m<4;m++)
			if(arr[n][m]=='.')
				return true;

return false;
}
int main ()
{ 
  ifstream fin ("input.txt");
  ofstream fout ("google1.txt");
 int num;
 int j,k;
 char s='X';
 fin>>num;
 char arr1[4][4];
 for(int i=0;i<num;i++)
 {
    //enter data//
	 for(j=0;j<4;j++)
		 for(k=0;k<4;k++)
			fin>>arr1[j][k];
	 //====================
	if(check4(arr1,s))
     fout<<"Case #"<<i+1<<": "<<s<<" won"<<endl;
	else
	{if(check(arr1))
	   fout<<"Case #"<<i+1<<": "<<"Game has not completed"<<endl;
	else  fout<<"Case #"<<i+1<<": "<<"Draw"<<endl;
	}
}
return 0;
}