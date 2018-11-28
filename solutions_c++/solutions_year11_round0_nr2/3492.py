#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	int t,n,c,d,count=0;
	ifstream ifile;
	ofstream ofile;
	ifile.open("input.txt");
	ofile.open("output.txt");
	ifile>>t;
	char C[37][3],D[29][2],N[100],O[100];
	for(int i=0;i<t;i++)
	{
		ifile>>c;
		for(int j=0;j<c;j++)
			for(int k=0;k<3;k++)
				ifile>>C[j][k];
		ifile>>d;
		for(int j=0;j<d;j++)
			for(int k=0;k<2;k++)
				ifile>>D[j][k];
		ifile>>n;
		for(int j=0;j<n;j++)
			ifile>>N[j];
		O[0]=N[0];
		count=0;
		char ch;
		int a=0;
		int flag=0;
		for(int j=1;j<n;j++)
		{
			flag=0;
			if(count==-1)
			{
				O[0]=N[j];
				count=0;
			}
			else
			{
				ch=N[j];
				for(a=0;a<c;a++)
					if((C[a][0]==ch&&C[a][1]==O[count])||(C[a][1]==ch&&C[a][0]==O[count]))
						break;
				if(a<c)
				{
					O[count]=C[a][2];
				}
				else
				{	
					for(int k=0;k<d && flag!=1;k++)
					{
						if(D[k][0]==ch)
						{
							for(int b=0;b<=count;b++)
								if(D[k][1]==O[b])
								{
									count=-1;
									flag=1;
									break;
								}
						}
						else
						if(D[k][1]==ch)
						{
							for(int b=0;b<=count;b++)
								if(D[k][0]==O[b])
								{
									count=-1;
									flag=1;
									break;
								}
						}
					}
					if(!flag)
					{
						count++;
						O[count]=ch;
					}
				}
			}
		}
		ofile<<"Case #"<<i+1<<": [";
		if(count>=0)
		{
			ofile<<O[0];
			for(int j=1;j<=count;j++)
				ofile<<", "<<O[j];
		}
		ofile<<"]\n";
	}
	ifile.close();
	ofile.close();
}