#include<fstream.h>
#include<conio.h>
#include<string.h>
void main()
{
	clrscr();
	char* ch1;
	char instr[50][500],test[500],check[500];
	ifstream fin;
	ofstream fout;
	fout.open("A-small.out",ios::out);
	fin.open("A-small.in",ios::in);
	int l,d,n,count=0;
	char ch;
	fin>>l>>d>>n;
	for(int i=0;i<d;i++)
	{
		fin.read(ch1,1);
		fin.get(instr[i],l+1);
	}
	for(i=0;i<n;i++)
	{
		fin.read(ch1,1);
		fin.get(test,500);
		count=0;
		for(int j=0;j<d;j++)
		{
			strcpy(check,instr[j]);
			for(int k=0,m=0;k<l;k++)
			{
			lb:
				ch=test[m];
				if(ch=='(')
				{
					while(ch!=')')
					{
						ch=test[++m];
						if(ch==check[k])
						{
							while(ch!=')')
							{
								ch=test[++m];
							}
							if(k==l-1)
								count++;
						}
						else
						{
							if(ch==')')
							{
								goto lb;
							}
						}
					}
					m++;
				}
				else
				{
					if(ch!=check[k])
					{
						break;
					}
					if(k==l-1)
					{
						if(ch==check[k])
							count++;
					}
					m++;
				}
			}
		}
		fout<<"Case #"<<i+1<<": "<<count<<"\n";
	}
}
