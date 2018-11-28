#include <iostream>
#include <fstream>
#include <string>

using namespace std;
char box[4][4];

int checkO()
{
	int i,j,s,t;
	s=0;
	t=0;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(box[i][j]=='O')
				s++;
			else if(box[i][j]=='T')
				t++;
			else { s=0;t=0;}
		}
		if(s==4 || (s==3 && t==1))
			return 1;
		s=0;
		t=0;

		for(j=0;j<4;j++)
		{
			if(box[j][i]=='O')
				s++;
			else if(box[j][i]=='T')
				t++;
			else { s=0;t=0;}
		}
		if(s==4 || (s==3 && t==1))
			return 1;
		s=0;
		t=0;
	}
	for(j=0;j<4;j++)
		{
			if(box[j][j]=='O')
				s++;
			else if(box[j][j]=='T')
				t++;
			else { s=0;t=0;}
		}
		if(s==4 || (s==3 && t==1))
			return 1;
		s=0;
		t=0;

	for(j=0;j<4;j++)
		{
			if(box[j][4-j-1]=='O')
				s++;
			else if(box[j][4-j-1]=='T')
				t++;
			else { s=0;t=0;}
		}
		if(s==4 || (s==3 && t==1))
			return 1;

	return 0;
}

int checkX()
{
	int i,j,s,t;
	s=0;
	t=0;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(box[i][j]=='X')
				s++;
			else if(box[i][j]=='T')
				t++;
			else { s=0;t=0;}
		}
		if(s==4 || (s==3 && t==1))
			return 1;
		s=0;
		t=0;

		for(j=0;j<4;j++)
		{
			if(box[j][i]=='X')
				s++;
			else if(box[j][i]=='T')
				t++;
			else { s=0;t=0;}
		}
		if(s==4 || (s==3 && t==1))
			return 1;
		s=0;
		t=0;
	}
	for(j=0;j<4;j++)
		{
			if(box[j][j]=='X')
				s++;
			else if(box[j][j]=='T')
				t++;
			else { s=0;t=0;}
		}
		if(s==4 || (s==3 && t==1))
			return 1;
		s=0;
		t=0;

	for(j=0;j<4;j++)
		{
			if(box[j][4-j-1]=='X')
				s++;
			else if(box[j][4-j-1]=='T')
				t++;
			else { s=0;t=0;}
		}
		if(s==4 || (s==3 && t==1))
			return 1;

	return 0;
}

int checkY()
{
	int i,j;
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			if(box[i][j]=='.')
				return 1;
	return 0;
}

int main()
{
	int i,j,k,n;
	ifstream in;
	ofstream out;
	in.open("A-large.in");
	out.open("outout.in");
	in >> n;
	string line;
	getline(in, line);
	for(k=0;k<n;k++)
	{
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				in >> box[i][j];
			}
		}
		if(checkX()==1)
			out << "Case #" << k+1 << ": X won\n";
		else if(checkO()==1)
			out << "Case #" << k+1 << ": O won\n";
		else if(checkY()==1)
			out << "Case #" << k+1 << ": Game has not completed\n";
		else out << "Case #" << k+1 << ": Draw\n";
	}
		
	in.close();
	out.close();
	return 0;
}
