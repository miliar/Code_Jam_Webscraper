#include<fstream.h>
void main()
{
	int t,i,j,k=1,f;
	char a[4][4];
	ifstream fin;
	ofstream fout;
	fin.open("abc.in",ios::in);
	fout.open("out.out",ios::out);
	fin>>t;
	while(t--)
	{
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				fin>>a[i][j];
		f=0;
		for(i=0;i<4;i++)
		{
			if(a[i][0]=='X'&&a[i][1]=='X'&&a[i][2]=='X'&&(a[i][3]=='X'||a[i][3]=='T'))
			{
				f=1;
				fout<<"Case #"<<k++<<": X won\n";
			}
			else if(a[i][0]=='O'&&a[i][1]=='O'&&a[i][2]=='O'&&(a[i][3]=='O'||a[i][3]=='T'))
			{
				f=1;
				fout<<"Case #"<<k++<<": O won\n";
			}
			else if(a[0][i]=='X'&&a[1][i]=='X'&&a[2][i]=='X'&&(a[3][i]=='X'||a[3][i]=='T'))
			{
				f=1;
				fout<<"Case #"<<k++<<": X won\n";
			}
			else if(a[0][i]=='O'&&a[1][i]=='O'&&a[2][i]=='O'&&(a[3][i]=='O'||a[3][i]=='T'))
			{
				f=1;
				fout<<"Case #"<<k++<<": O won\n";
			}
		}
		if(a[0][0]=='X'&&a[1][1]=='X'&&a[2][2]=='X'&&(a[3][3]=='X'||a[3][3]=='T'))
		{
			f=1;
			fout<<"Case #"<<k++<<": X won\n";
		}
		else if(a[0][0]=='O'&&a[1][1]=='O'&&a[2][2]=='O'&&(a[3][3]=='O'||a[3][3]=='T'))
		{
			f=1;
			fout<<"Case #"<<k++<<": O won\n";
		}
		if(a[0][3]=='X'&&a[1][2]=='X'&&a[2][1]=='X'&&(a[3][0]=='X'||a[3][0]=='T'))
		{
			f=1;
			fout<<"Case #"<<k++<<": X won\n";
		}
		else if(a[0][3]=='O'&&a[1][2]=='O'&&a[2][1]=='O'&&(a[3][0]=='O'||a[3][0]=='T'))
		{
			f=1;
			fout<<"Case #"<<k++<<": O won\n";
		}
		if(f==0)
		{
			for(i=0;i<4;i++)
			{
				for(j=0;j<4;j++)
				{
					if(a[i][j]=='.')
					{
						f=1;
						break;
					}
				}
				if(f==1)
					break;
			}
			if(f==0)
				fout<<"Case #"<<k++<<": Draw\n";
			else
				fout<<"Case #"<<k++<<": Game has not completed\n";
		}
	}
	fin.close();
	fout.close();
}