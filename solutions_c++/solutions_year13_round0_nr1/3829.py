#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ofstream output;
	ifstream input;
	input.open("input.txt");
	output.open("output.txt");

//	FILE * input;
//	input = fopen("input.txt","r");

	int n;

//	fread(&n, sizeof(int), 1, input);cout<<n<<endl; char cc=getchar();

	input>>n;// cout<<n<<endl;
	int a[4][4];
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			a[i][j]=0;
		}

	char c;
	for(int k=0;k<n;k++)
	{
		c='\n';
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
//				c=fgetc(input); cout<<c<<endl;
				input>>c; //cout<<c<<endl;
				

					while((c!='X')&&(c!='O')&&(c!='T')&&(c!='.'))
					{
						//c=fgetc(input);
						input>>c;
					}
				//	 cout<<c<<endl;
				
				switch(c)
				{
				case 'X':
					a[i][j]=100;
					break;
				case 'O':
					a[i][j]=90;
					break;
				case 'T':
					a[i][j]=900;
					break;
				default:
					a[i][j]=1;
					break;
				}
			}
		}

//		for(int i=0;i<4;i++)
//		{
//			for(int j=0;j<4;j++)
//			{
//				cout<<a[i][j]<<' ';
//			}
//			cout<<endl;
//		}
//		cout<<endl;
		

		int sum=0;
		int result=0;
		bool b = 0;

		for (int i = 0; i < 4; i++)
		{
			if(result)
				break;
			sum=0;
			for (int j = 0; j < 4; j++)
			{
				sum+=a[i][j];
			}
			if(sum%100==0)
			{
				result =1;
				break;
			}
			else if(sum%90==0)
			{
				result = 2; //cout<<endl<<endl<<endl<<i<<" "<<1<<endl<<endl<<endl;
				break;
			}
			else if(sum%10)
			{
				b=1;
			}

		}
		for (int i = 0; i < 4; i++)
		{
			if(result)
				break;
			sum=0;
			for (int j = 0; j < 4; j++)
			{
				sum+=a[j][i];
			}
			if(sum%100==0)
			{
				result =1;
				break;
			}
			else if(sum%90==0)
			{
				result = 2;
				break;
			}
			else if(sum%10)
			{
				b=1;
			}

		}

		for (int i = 0; i < 1; i++)
		{
			if(result)
				break;
			sum=0;
			for (int j = 0; j < 4; j++)
			{
				sum+=a[j][j];
			}
			if(sum%100==0)
			{
				result =1;
				break;
			}
			else if(sum%90==0)
			{
				result = 2;
				break;
			}
			else if(sum%10)
			{
				b=1;
			}

		}

		for (int i = 0; i < 1; i++)
		{
			if(result)
				break;
			sum=0;
			for (int j = 0; j < 4; j++)
			{
				sum+=a[j][3-j];
			}
			if(sum%100==0)
			{
				result =1;
				break;
			}
			else if(sum%90==0)
			{
				result = 2;
				break;
			}
			else if(sum%10)
			{
				b=1;
			}

		}

		output<<"Case #"<<k+1<<": "; 
		if(result)
		{
			if(result==1)
				output<<"X won"<<endl;
			else if(result ==2)
				output<<"O won"<<endl;
		}
		else
			if(b)
				output<<"Game has not completed"<<endl;
			else
				output<<"Draw"<<endl;

		//do
		//	{
		//		//c=fgetc(input);
		//		input>>c;
		//	}
		//	while((c!='X')&&(c!='O')&&(c!='T')&&(c!='.'));
	}
//	fclose(input);
	input.close();
	output.close();
//	system("pause");
	return 0;
}
