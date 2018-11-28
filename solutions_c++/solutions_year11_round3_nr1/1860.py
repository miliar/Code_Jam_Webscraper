#include<iostream>
#include<cstdio>

using namespace std;

void main()
{
	//list<comb> CombList;
	//list<oppo> OppoList;
	//list<char> Seq;
	int T,R,C,blues;
	int i,j;
	char arr[60][60];
	
	char a;
		
	cin>>T;
	for(int cases=1;cases <= T;cases++)
	{
		cin>>R>>C;
		blues = 0;
		for(i=0;i<R;i++)
		{
			//gets(&arr[i][0]);
			scanf("%s",&arr[i][0]);
			for(j=0;j<C;j++)
			{
				if(arr[i][j] == '#')
					blues++;
			}
		}

		if(blues%4 == 0 )
		{
			for(i=0;i<R-1;i++)
			{
				for(j=0;j<C-1;j++)
				{
					if(arr[i][j] == '#' && arr[i][j+1] == '#' && arr[i+1][j] == '#'  && arr[i+1][j+1] == '#' )
					{
						blues = blues - 4;
						arr[i][j] = '/';
						arr[i][j+1] = '\\';
						arr[i+1][j] = '\\';
						arr[i+1][j+1] = '/';
					}
				}
			}
		}

		cout<<"Case #"<<cases<<":"<<endl;
		if(blues == 0 )
		{
			for(i=0;i<R;i++)
			{
				for(j=0;j<C;j++)
				{
					cout<<arr[i][j];
				}
				cout<<endl;
			}
		}
		else
		{
			cout<<"Impossible"<<endl;
		}

		

	}
		
}

