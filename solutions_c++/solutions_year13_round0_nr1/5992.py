#include<iostream>
#include<fstream>
using namespace std;
int main()
{   
	int i,j,rowx=0,rowo=0,flag=1,won=0,diax1=0,diao1=0,diax2=0,diao2=0,n;
	char c[4][4];
		ifstream fin("C:\\Users\\sesir_000\\Documents\\C++ stuff\\A.in");
	ofstream fout("C:\\Users\\sesir_000\\Documents\\C++ stuff\\A.out");
	fin>>n;
	for(int p=1;p<=n;p++)
	{
		won=0;flag=1;
		diax1=0;diax2=0;diao1=0;diao2=0;
	for(i=0;i<4;i++)
	for(j=0;j<4;j++)
	fin>>c[i][j];
	for(i=0;i<4;i++)
	{
		rowx=0;
		rowo=0;
		for(j=0;j<4;j++)
		if(c[i][j]=='.')flag=0;
		else if(c[i][j]=='O')rowo++;
		else if(c[i][j]=='X')rowx++;
		else if(c[i][j]=='T'){rowo++;rowx++;}
		if(c[i][i]=='X')diax1++;
		else if(c[i][i]=='O')diao1++;
		else if(c[i][i]=='T'){diax1++;diao1++;}
			if(c[i][4-i-1]=='X')diax2++;
		else if(c[i][4-i-1]=='O')diao2++;
		else if(c[i][4-i-1]=='T'){diax2++;diao2++;}
		if(rowo==4){fout<<"Case #"<<p<<": O won\n";	won=1;goto SKIP;}
		else if(rowx==4){fout<<"Case #"<<p<<": X won\n";	won=1;goto SKIP;}
	
	}
	for(j=0;j<4;j++)
	{
		rowx=0;
		rowo=0;
		for(i=0;i<4;i++)
		if(c[i][j]=='O')rowo++;
		else if(c[i][j]=='X')rowx++;
		else if(c[i][j]=='T'){rowo++;rowx++;}
		if(rowo==4){fout<<"Case #"<<p<<": O won\n";	won=1;goto SKIP;}
		else if(rowx==4){fout<<"Case #"<<p<<": X won\n";	won=1;goto SKIP;}
		
	}
	if(diax1==4||diax2==4){fout<<"Case #"<<p<<": X won\n";won=1;}
	else if(diao1==4||diao2==4){fout<<"Case #"<<p<<": O won\n";won=1;}
	if(won==0&&flag==0)fout<<"Case #"<<p<<": Game has not completed\n";
	else if(won==0&&flag==1)fout<<"Case #"<<p<<": Draw\n";
	
	SKIP:;
	}
	return 0;
}
	
	
