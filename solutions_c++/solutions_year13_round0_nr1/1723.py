#include<fstream>
#include<string>
#include<iostream>
using namespace std;
void z_clean(int* gameboard)
{
	for(int i=0;i<16;i++)gameboard[i]=0;
}

void z_input(ifstream& ifile,int * gameboard)
{
	string line;
	
	for(int i=0;i<4;i++)
	{
		getline(ifile,line);
		cout<<line<<endl;
		for(int j=0;j<4;j++)
		{
			if(line[j]=='X')gameboard[i*4+j]=-1;
			else if(line[j]=='O')gameboard[i*4+j]=1;
			else if(line[j]=='.')gameboard[i*4+j]=0;
			else gameboard[i*4+j]=2;
		}
	}
	getline(ifile,line);
}
int z_c(int a,int b)
{
	if(a==0||b==0)return 0;
	else if(a==-100||b==-100)return -100;
	else
	{
		if(a==b&&a!=2)return a;
	else if(a==2)return b;
	else if(b==2)return a;
	else return -100;
	}
}
string z_print(int i)
{
	if(i==-1)return "X won";
	else if(i==1)return "O won";
	else return "";
}
//0123
//4567
//891011
//12131415
string z_check(int* g)
{
	bool n=false;
	int h=z_c(g[0],z_c(g[1],z_c(g[2],g[3])));
	if(h==0)n=true;
	else if(h!=-100)
	{	
		return z_print(h);
	}
	h=z_c(g[4],z_c(g[5],z_c(g[6],g[7])));
	if(h==0)n=true;
	else if(h!=-100)
	{	
		return z_print(h);
	}
	h=z_c(g[8],z_c(g[9],z_c(g[10],g[11])));
	if(h==0)n=true;
	else if(h!=-100)
	{	
		return z_print(h);
	}
	h=z_c(g[12],z_c(g[13],z_c(g[14],g[15])));
	if(h==0)n=true;
	else if(h!=-100)
	{	
		return z_print(h);
	}
	h=z_c(g[0],z_c(g[4],z_c(g[8],g[12])));
	if(h==0)n=true;
	else if(h!=-100)
	{	
		return z_print(h);
	}
	h=z_c(g[1],z_c(g[5],z_c(g[9],g[13])));
	if(h==0)n=true;
	else if(h!=-100)
	{	
		return z_print(h);
	}
	h=z_c(g[2],z_c(g[6],z_c(g[10],g[14])));
	if(h==0)n=true;
	else if(h!=-100)
	{	
		return z_print(h);
	}
	h=z_c(g[3],z_c(g[7],z_c(g[11],g[15])));
	if(h==0)n=true;
	else if(h!=-100)
	{	
		return z_print(h);
	}
	h=z_c(g[0],z_c(g[5],z_c(g[10],g[15])));
	if(h==0)n=true;
	else if(h!=-100)
	{	
		return z_print(h);
	}
	h=z_c(g[3],z_c(g[6],z_c(g[9],g[12])));
	if(h==0)n=true;
	else if(h!=-100)
	{	
		return z_print(h);
	}
	if(n)return "Game has not completed";
	else return "Draw";

}
int main()
{
	ifstream ifile("input.txt");
	ofstream ofile("output.txt");
	int T;
	int gameboard[16];
	ifile>>T;
	string nu;
	getline(ifile,nu);
	for(int i=1;i<=T;i++)
	{
		z_input(ifile,gameboard);
		ofile<<"Case #"<<i<<": "<<z_check(gameboard)<<endl;
	}
}