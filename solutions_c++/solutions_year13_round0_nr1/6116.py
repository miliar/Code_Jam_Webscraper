#include<iostream.h>
#include<stdio.h>
#include<conio.h>
class codejam
{
	private:
		char a[4][4];
	public:
	void setvalue()
	{
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		cin>>a[i][j];
	}
	void getvalue()
	{
		{
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
				cout<<a[i][j];
				cout<<endl;
			}
		}
	}
	int rowcheck(int i,char q)
	{
		for(int j=0;j<4;j++)
		{
			if((a[i][j]==q || a[i][j]=='T'))
			{
				continue;
			}
			else
			{
				return 0;
			}
		}
		return 1;
	}
	int colcheck(int i,char q)
	{
		for(int j=0;j<4;j++)
		{
			if((a[j][i]==q || a[j][i]=='T'))
			{
				continue;
			}
			else
			{
				return 0;
			}
		}
		return 1;
	}
	int diacheck(char q)
	{
		int i=0,j=0;
		while(i<4 && j<4)
		{
			if((a[j][i]==q || a[j][i]=='T'))
			{
				i++;
				j++;
				continue;
			}
			else
			{
				return 0;
			}
		}
		return 1;
	}
	int revdiacheck(char q)
	{
		int i=0,j=3;
		while(i<4)
		{
			if((a[j][i]==q || a[j][i]=='T'))
			{
				i++;
				j--;
				continue;
			}
			else
			{
				return 0;
			}
		}
		return 1;
	}
	int drawcheck()
	{
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			if(a[i][j]=='.')
			return 0;
		}
		return 1;
	}
};
int main()
{
	codejam c;
	int z=1;
	int w;
	cin>>w;
	while(w>0)
	{
	c.setvalue();
	for(int i=0;i<4;i++)
	{
		if(c.rowcheck(i,'X')==1)
		{
			cout<<"Case #"<<z<<": X won\n";
			goto end;
		}
	}
	for(int i=0;i<4;i++)
	{
		if(c.colcheck(i,'X')==1)
		{
			cout<<"Case #"<<z<<": X won\n";
			goto end;
		}
	}
	if(c.diacheck('X')==1)
	{
		cout<<"Case #"<<z<<": X won\n";
		goto end;
	}
	if(c.revdiacheck('X')==1)
	{
		cout<<"Case #"<<z<<": X won\n";
		goto end;
	}
	for(int i=0;i<4;i++)
	{
		if(c.rowcheck(i,'O')==1)
		{
			cout<<"Case #"<<z<<": O won\n";
			goto end;
		}
	}
	for(int i=0;i<4;i++)
	{
		if(c.colcheck(i,'O')==1)
		{
			cout<<"Case #"<<z<<": O won\n";
			goto end;
		}
	}
	if(c.diacheck('O')==1)
	{
		cout<<"Case #"<<z<<": O won\n";
		goto end;
	}
	if(c.revdiacheck('O')==1)
	{
		cout<<"Case #"<<z<<": O won\n";
		goto end;
	}
	if(c.drawcheck()==1)
	{
		cout<<"Case #"<<z<<": Draw\n";
	}
	else
	{
		cout<<"Case #"<<z<<": Game has not completed\n";
	}
	end:
	z++;
	w--;
	}
	return 0;
}