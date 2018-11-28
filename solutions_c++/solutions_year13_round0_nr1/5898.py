#include <iostream>
#include <stdio.h>
using namespace std;

int main(int argc, const char * argv[])
{
	FILE* ptr=fopen("sample.txt","rt");	
	char A[4][4],c;
	char s[5];
	int X[10];
	int O[10],i,j,k=0,T,X_flag,O_flag,draw,t_flag,incomp;
	fscanf(ptr,"%d",&T);
	// c=fgetc(ptr);
	while(T--)
	{
		X_flag=0;
		O_flag=0;
		draw=0;
		t_flag=0;
		incomp=0;
		k++;
		for(i=0;i<10;i++)
		{
			X[i]=0;
			O[i]=0;
		}
		
		for(i=0;i<4;i++)
		{
			fscanf(ptr,"%s",s);
		//	c=fgetc(ptr);
			for(j=0;j<4;j++)
				A[i][j]=(char)s[j];
		}

		// for(i=0;i<4;i++)
		// {
		// 	for(j=0;j<4;j++)
		// 		{
		// 			A[i][j]=fgetc(ptr);
		// 		}
		// }

		// for(i=0;i<4;i++)
		// {
		// 	for(j=0;j<4;j++)
		// 		cout<<A[i][j];
		// 	cout<<endl;
		// }

		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(A[i][j]=='X')
					X[i]++;
				else if(A[i][j]=='O')
					O[i]++;
				else if(A[i][j]=='T')
					t_flag=1;
				else
					incomp=1;
			}
			if(X[i]==4)
			{
				X_flag=1;
				break;
			}
			else if(O[i]==4)
			{
				O_flag=1;
				break;
			}
			else if(t_flag)
			{
				if(X[i]==3)
				{
					X_flag=1;
					break;
				}
				else if(O[i]==3)
				{
					O_flag=1;
					break;
				}
				else
				{
					t_flag=0;
				}
			}
		}

		if(X_flag!=1 && O_flag!=1)
		{
			for(i=0;i<4;i++)
			{
				for(j=0;j<4;j++)
				{
					if(A[j][i]=='X')
						X[i+4]++;
					else if(A[j][i]=='O')
						O[i+4]++;
					else if(A[j][i]=='T')
						t_flag=1;
					else
						incomp=1;				
				}
				if(X[i+4]==4)
				{
					X_flag=1;
					break;
				}
				else if(O[i+4]==4)
				{
					O_flag=1;
					break;
				}
				else if(t_flag)
				{
				if(X[i+4]==3)
				{
					X_flag=1;
					break;
				}
				else if(O[i+4]==3)
				{
					O_flag=1;
					break;
				}
				else
				{
					t_flag=0;
				}
				}
			}
		}

		if(!X_flag && !O_flag)
		{
			for(i=0;i<4;i++)
			{
				if(A[i][i]=='X')
					X[8]++;
				else if(A[i][i]=='O')
					O[8]++;
				else if(A[i][i]=='T')
					t_flag=1;
				else
					incomp=1;
			}	
				if(X[8]==4)
				{
					X_flag=1;
				}
				else if(O[8]==4)
				{
					O_flag=1;
				}
				else if(t_flag)
				{
				if(X[8]==3)
				{
					X_flag=1;
				}
				else if(O[8]==3)
				{
					O_flag=1;
				}
				else
				{
					t_flag=0;
				}
				}
		if(!X_flag && !O_flag)
		{
			for(i=0;i<4;i++)
			{
				if(A[i][3-i]=='X')
					X[9]++;
				else if(A[i][3-i]=='O')
					O[9]++;
				else if(A[i][3-i]=='T')
					t_flag=1;
				else
					incomp=1;
			}	
				if(X[9]==4)
				{
					X_flag=1;
				}
				else if(O[9]==4)
				{
					O_flag=1;
				}
				else if(t_flag)
				{
				if(X[9]==3)
				{
					X_flag=1;
				}
				else if(O[9]==3)
				{
					O_flag=1;
				}
				else
				{
					t_flag=0;
				}
				}			
		}
		}
	
		if(X_flag==1)
			cout<<"Case #"<<k<<": X won"<<endl;
		else if(O_flag==1)
			cout<<"Case #"<<k<<": O won"<<endl;
		else if(incomp==0)
			cout<<"Case #"<<k<<": Draw"<<endl;
		else
			cout<<"Case #"<<k<<": Game has not completed"<<endl;
		//c=fgetc(ptr);

	}
	fclose(ptr);
    return 0;
}

