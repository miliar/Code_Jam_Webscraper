#include <iostream.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <fstream.h>

class pattern
{
  public:
  int grid[15][26];
  pattern();
};
pattern::pattern()
{
 for(int i=0;i<15;i++)
    for(int j=0;j<26;j++)
    grid[i][j]=0;
}


int count[500];
int main(void)
{
	int len,no_of_strings,n;
	char**string;
	pattern* p=new pattern[500];
	char temp[1000];

	cin >> len >> no_of_strings >> n;
	string=new char*[no_of_strings];
	for(int i=0;i<no_of_strings;i++)
	{ string[i]=new char[len+1];
	  cin >> string[i];
	}

	for(i=0;i<n;i++)
	{
	  cin >> temp;
	      //tokenization
	      int m=0;
	      int flag=0;
	      for(int j=0;j<strlen(temp);j++)
	      {
		if(temp[j]==')')
		{ m++;
		  flag=0;
		  continue;
		}
		if(temp[j]=='(')
		{
		  flag=1;
		  continue;
		}

	   p[i].grid[m][temp[j]-'a']=1;
		if(!flag)
		m++;

	      }
	}

/*	for(i=0;i<n;i++)
	{
	   //cout << " case : " << i+1 << endl;
	   for(int j=0;j<len;j++)
	   {
	     for(int k=0;k<26;k++)
	     //cout << j+'a' << "  " << p[i].grid[j][k] << endl;
	   //getch();
	   }
	}

*/
	int flag;
	for(i=0;i<no_of_strings;i++)
	{
		//cout << string[i] << endl;
		for(int j=0;j<n;j++)
		{
		   flag=1;
		  // cout << endl << "case :" << j << endl;
		   for(int k=0;k<len;k++)
		   {
		    // cout << "string[i][k] : " <<string[i][k]  << endl;
		     //cout << p[j].grid[k][string[i][k]-'a']<< "  ";
		     if(p[j].grid[k][string[i][k]-'a']==0)
		     {
		      flag=0;
		      break;
		     }
		   }
		   if(flag)
		   count[j]++;
		   //getch();
		}
	}





	for(i=0;i<n;i++)
	cout << "Case #" << i+1 << ": " << count[i] << endl;


return 0;

}