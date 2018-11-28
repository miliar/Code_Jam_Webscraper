#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ofstream fout ("1.out");
ifstream fin ("1.in");
 
class Node
{
public:
	//int num;
	char sym;
	
	Node()
	{

	}
	Node(char b)
	{
		//num=a;
		sym=b;
	}
};

int check(char **in)
{
	int judge=-1;
	int ti=-1;
	int tj=-1;
	bool judge1=false;
	for (int i=0;i<4;i++)
	{
		for (int j=0;j<4;j++)
		{
			if (in[i][j]=='T')
			{
				ti=i;
				tj=j;
				judge1=true;
				break;
			}
		}
		if (judge1==true)
		{
			break;
		}
	}



	if (ti==-1)  //没有T
	{
		//right
		for (int i=0;i<4;i++)
		{
			if (in[i][0]==in[i][1]&&in[i][1]==in[i][2]&&in[i][1]==in[i][3]&&in[i][1]=='X')
			{
				return 2;
			}
			else if(in[i][0]==in[i][1]&&in[i][1]==in[i][2]&&in[i][1]==in[i][3]&&in[i][1]=='O')
			{
				return 3;
			}
		}
		//down
		for (int i=0;i<4;i++)
		{
			if (in[0][i]==in[1][i]&&in[0][i]==in[2][i]&&in[0][i]==in[3][i]&&in[0][i]=='X')
			{
				return 2;
			}
			else if(in[0][i]==in[1][i]&&in[0][i]==in[2][i]&&in[0][i]==in[3][i]&&in[0][i]=='O')
			{
				return 3;
			}
		}
		//diago
		if ((in[0][0]==in[1][1]&&in[0][0]==in[2][2]&&in[0][0]==in[3][3]&&in[0][0]=='O')||(in[0][3]==in[1][2]&&in[0][3]==in[2][1]&&in[0][3]==in[3][0]&&in[0][3]=='O'))
		{
			return 3;
			cout<<endl;
		} 
		else if((in[0][0]==in[1][1]&&in[0][0]==in[2][2]&&in[0][0]==in[3][3]&&in[0][0]=='X')||(in[0][3]==in[1][2]&&in[0][3]==in[2][1]&&in[0][3]==in[3][0]&&in[0][3]=='X'))
		{
			return 2;
		}
	} 
	else if(ti>=0)  //有T
	{
		//right
		bool judge2=false;
		for (int i=0;i<4;i++)
		{
			for (int j=0;j<4;j++)
			{
				if (in[i][j]=='T'||in[i][j]=='X')
				{
					judge2=true;
				} 
				else
				{
					judge2=false;
					break;
				}
			}
			if (judge2==true)
			{
				break;
			}
			
		}
		if (judge2==true)
		{
			return 2;
		}
		judge2=false;
		for (int i=0;i<4;i++)
		{
			for (int j=0;j<4;j++)
			{
				if (in[i][j]=='T'||in[i][j]=='O')
				{
					judge2=true;
				} 
				else
				{
					judge2=false;
					break;
				}

			}
			if (judge2==true)
			{
				break;
			}
			
		}
		if (judge2==true)
		{
			return 3;
		}
		//down
		judge2=false;
		for (int j=0;j<4;j++)
		{
			for (int i=0;i<4;i++)
			{
				if (in[i][j]=='T'||in[i][j]=='X')
				{
					judge2=true;
				} 
				else
				{
					judge2=false;
					break;
				}
			}
			if (judge2==true)
			{
				break;
			}
			
		}
		if (judge2==true)
		{
			return 2;
		}
		
		judge2=false;
		for (int j=0;j<4;j++)
		{
			for (int i=0;i<4;i++)
			{
				if (in[i][j]=='T'||in[i][j]=='O')
				{
					judge2=true;
				} 
				else
				{
					judge2=false;
					break;
				}
			}
			if (judge2==true)
			{
				break;
			}
		}
		
		if (judge2==true)
		{
			return 3;
		}
		//dia
		if (ti==tj||ti+tj==3)
		{
			judge2=false;
			for (int i=0;i<4;i++)
			{
				if (in[i][i]=='T'||in[i][i]=='X')
				{
					judge2=true;
				} 
				else
				{
					judge2=false;
					break;
				}

			}
			if (judge2==true)
			{
				return 2;
			}
			judge2=false;
			for (int i=0;i<4;i++)
			{
				if (in[i][i]=='T'||in[i][i]=='O')
				{
					judge2=true;
				} 
				else
				{
					judge2=false;
					break;
				}
			}
			if (judge2==true)
			{
				return 3;
			}


			judge2=false;
			for (int i=0;i<4;i++)
			{
				if (in[i][3-i]=='T'||in[i][3-i]=='X')
				{
					judge2=true;
				} 
				else
				{
					judge2=false;
					break;
				}
			}
			if (judge2==true)
			{
				return 2;
			}
			judge2=false;
			for (int i=0;i<4;i++)
			{
				if (in[i][3-i]=='T'||in[i][3-i]=='O')
				{
					judge2=true;
				} 
				else
				{
					judge2=false;
					break;
				}
			}
			if (judge2==true)
			{
				return 3;
			}
		}
		else   //t不在对角线
		{
			if ((in[0][0]==in[1][1]&&in[0][0]==in[2][2]&&in[0][0]==in[3][3]&&in[0][0]=='O')||(in[0][3]==in[1][2]&&in[0][3]==in[2][1]&&in[0][3]==in[3][0]&&in[0][3]=='O'))
			{
				return 3;
				cout<<endl;
			} 
			else if((in[0][0]==in[1][1]&&in[0][0]==in[2][2]&&in[0][0]==in[3][3]&&in[0][0]=='X')||(in[0][3]==in[1][2]&&in[0][3]==in[2][1]&&in[0][3]==in[3][0]&&in[0][3]=='X'))
			{
				return 2;
			}
	
		}
}
	


	return judge;
}




int main() {

	int t;
	fin>>t;
	bool *judge_empty=new bool[t];
	
	char ***input;
	input=new char **[t];
	for (int i=0;i<t;i++)
	{
		//int temp=0;
		input[i]=new char*[4];
		for (int j=0;j<4;j++)
		{
			input[i][j]=new char[4];
			for (int k=0;k<4;k++)
			{
				
				fin>>input[i][j][k];
				if (input[i][j][k]=='.')
				{
					judge_empty[i]=true;
				}
				//cout<<input[i][j][k];

			}
			//cout<<endl;
		}
		//cout<<endl;
	}
	for (int i=0;i<t;i++)
	{
		fout<<"Case #"<<i+1<<": ";
		switch(check(input[i]))
		{
		case -1:
			if (judge_empty[i]==true)
			{
				fout<<"Game has not completed"<<endl;
			}
			else 
			{
				fout<<"Draw"<<endl;
			}
			break;
		case 2:
			fout<<"X won"<<endl;
			break;
		case 3:
			fout<<"O won"<<endl;
			break;
		}






		
	}



	//system("pause");
	return 0;
}