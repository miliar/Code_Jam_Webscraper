#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<fstream>

using namespace std;

void get_file();
void readt();
void readn();
void readLine();

char arr[500000];

unsigned long int tk=0,tnum,pos=0,x=0,k=0,n=0,t=0,num,totalTime,button_c[100],button_p[100],line;

class robot {
public:
	int position;
	int color;
	int timeToMove;
}blue,orange;



void main()
{
	get_file();
	readt();
//	cout << "\nT = " << t;
	for(int ii = 0;ii<t;ii++)
	{
		readn();
		blue.position = 1;
		blue.color = 'B';
		orange.position = 1;
		orange.color = 'O';
		readLine();
		totalTime=0;
		//cout << "\nN = " << n; 
				//cout << "\n Line = " << line;
				/*for(int kk =0;kk<line;kk++)
			{cout << "\n Button Color : " << button_c[kk] << "  Button Position : " << button_p[kk];}*/

			for(int kk =0;kk<n;kk++)
			{
				int tempTime=0;
				switch(button_c[kk])
				{
				case 'O':
					if(button_p[kk] != orange.position)
					{
						tempTime = button_p[kk]>orange.position?(button_p[kk]-orange.position):(orange.position-button_p[kk]);
						totalTime = totalTime + tempTime;
						orange.position = button_p[kk];
					}
					if(button_p[kk] == orange.position)
					{
						tempTime++;
						totalTime++;
					}
					for(int ll=kk+1;button_c[ll-1] != 'B' && ll <n ;ll++)
						{
							if(button_c[ll] == 'B' && button_p[ll] != blue.position)
							{
							
								blue.timeToMove = button_p[ll]>blue.position?(button_p[ll]-blue.position):(blue.position-button_p[ll]);
								blue.timeToMove = blue.timeToMove - tempTime;
								if(blue.timeToMove <= 0)
								{blue.position = button_p[ll];}
								else
								{blue.position = button_p[ll]>blue.position?(blue.position + tempTime):(blue.position - tempTime);}
								
							}
						}
					break;
				case 'B':
					if(button_p[kk] != blue.position)
					{
						tempTime = button_p[kk]>blue.position?(button_p[kk]-blue.position):(blue.position-button_p[kk]);
						totalTime = totalTime + tempTime;
						//cout << "\nIn Blue Case , Total Time for N = "<< kk << " is " << totalTime << " Button Position = " << blue.position << " Button[kk] = " << button_p[kk];
						blue.position = button_p[kk];
						
					}
					if(button_p[kk] == blue.position)
					{
						tempTime++;
						totalTime++;
					}
					for(int ll=kk+1;button_c[ll-1] != 'O' && ll<n;ll++)
						{
							if(button_c[ll] == 'O' && button_p[ll] != orange.position)
							{
								orange.timeToMove = button_p[ll]>orange.position?(button_p[ll]-orange.position):(orange.position-button_p[ll]);
								orange.timeToMove = orange.timeToMove - tempTime;
								if(orange.timeToMove <= 0)
								{orange.position = button_p[ll];}
								else
								{orange.position = button_p[ll]>orange.position?(orange.position + tempTime):(orange.position - tempTime);}
								
							}

						}
					break;
				}
				//cout << "\nTotal Time for N = "<< kk << " is " << totalTime;
			
			
			
		}
			//cout << "\nTotal Time : " << totalTime<< "\n";
			ofstream fout;
			fout.open("output.in" , ios :: app);
			fout << "Case #" << ii+1 << ": " << totalTime<<"\n";
			fout.close();
	}
	getch();
}





void get_file()
{
	ifstream fin;
	fin.open("input.in" , ios :: in);
	while(fin)
	{
		fin.get(arr[x]);
		x++;
	}
	fin.close();
}

void readt()
{
	while (arr[pos] != '\n')
	{
		t =  (t*10) + (arr[pos] - 48);
		pos++;
	}
}

void readn()
{
	n=0;
	pos++;
	while (arr[pos] != ' ')
	{
		n = (n*10) + ( arr[pos] - 48 );
		pos++;
	}
}

void readLine()
{
	line =0;
	
	while(arr[pos] != '\n' && arr[pos] != '\0')
	{
		pos++;
		button_p[line] = 0;
		button_c[line] = arr[pos];
		pos = pos + 2;
		while(arr[pos] != '\n' && arr[pos] != ' ' && arr[pos] != '\0')
		{
			button_p[line] = (button_p[line]*10) + ( arr[pos] -48);
			pos++;
		}
		line++;
	}
}
