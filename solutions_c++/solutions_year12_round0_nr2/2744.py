#include<iostream.h>
#include<conio.h>
void main()
{
	clrscr();
	int n;
	cin>>n;
	int player[100],cases[100],surprise[100],minscore[100],tscore[100][100];
	for(int i=0;i<n;i++)
	{
		cases[i]=0;
	}
	for(i=0;i<n;i++)
	{
		cin>>player[i]>>surprise[i]>>minscore[i];
		for(int j=0;j<player[i];j++)
		{
			cin>>tscore[i][j];
		}
	}
	for(i=0;i<n;i++)
	{
		for(int j=0;j<player[i];j++)
		{
			int base = tscore[i][j]/3;
			switch(tscore[i][j]%3)
			{
				case 0:
					if(base>=minscore[i])
					{
						cases[i]++;
					}
					else
					{
						if((surprise[i]>0)&&(base>0)&&(base+1>=minscore[i]))
						{
							cases[i]++;
							surprise[i]--;
						}
					}
					break;
				case 1:
					if(base>=minscore[i]||(base+1>=minscore[i]))
					{
						cases[i]++;
					}
					else
					{
						if(surprise[i]>0 && base+1>=minscore[i])
						{
							cases[i]++;
							surprise[i]--;
						}
					}
					break;

				case 2:
					if(base+1>=minscore[i] || base>=minscore[i])
					{
						cases[i]++;
					}
					else
					{
						if(surprise[i]>0 && base+2>=minscore[i])
						{
							cases[i]++;
							surprise[i]--;
						}

					}
			}

		}

	}
	for(i=0;i<n;i++)
	{
		cout<<endl<<"Case #"<<i+1<<": "<<cases[i];
	}
	getch();
}