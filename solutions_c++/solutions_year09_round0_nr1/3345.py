
#include<iostream>
#include <string>
using namespace std;


int line,count,test;
char agi[600][6000];
char temp[600][6000];
bool chk=false;
int re[600];
string con;
int main()
{
	cin >> count >> line >> test;
	int j,k;
	for(int i =0;i<line;i++)
	{
		cin >> temp[i];
	}
	for(int i =0;i<test;i++)
	{
		re[i]=0;
		cin >> agi[i];
	


		for(int b = 0;b<line;b++)
		{
			j =0;
			for(int c=0;c<count;c++)
			{
					chk =false;
					con = "";
					if(agi[i][j]=='(')
					{
						char k= 'f';
						do
						{
							k=agi[i][++j];
							if(k==')') break;
							con +=k;
						}	while(k!=')');
					}
					else
					{
						con=agi[i][j];
					}
					j++;

					for(int ci =0;ci< con.length();ci++)
					{
						if(temp[b][c]==con[ci])
						{
							chk =true;
							break;
						}
					}				
				
					if(!chk)break;
				if(c == count-1) re[i]++;
			}
		}
	}
	for(int i =0;i<test;i++)
	{
		cout <<"Case # "<<i+1<<':'<< re[i]<<endl;
	}
	int sfdsf;
	cin >> sfdsf;
}