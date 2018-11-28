#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<fstream>
#include<string>

unsigned long int tk=0,c_x=0,pos=0,x=0,c=0,o=0,k=0,n=0,t=0,num,totalTime,button_c[100],button_p[100],line;
char arr[500000],combine[100][4],oppose[100][3],invoke[100],com_r[100];

void get_file();
void readt();
void readc();
void reado();
void readn();
void readCombines();
void readOpposed();
void readInvoke();
int checkCombine(int p);
int checkOppose(int p);

using namespace std;

void main()
{
	get_file();
	readt();
	//cout << "\n T = " << t;
	for( int ii=0 ; ii<t ; ii++ )
	{
		readc();
		readCombines();
		reado();
		readOpposed();
		readn();
		readInvoke();
		/*cout << "\nC = " << c << " O = " << o << " N = " << n << "\n";
		cout << "\nCombinations : \n";
		for(int xx =0; xx <c;xx++)
		{puts(combine[xx]);cout << " -> " << com_r[xx]<<"\n";}
		cout<< "\nOpposes : \n";
		for(int xx =0; xx <o;xx++)
		{puts(oppose[xx]);}
		cout << "\nInvoke : ";
		puts(invoke);*/

		for(int jj=1;jj<strlen(invoke);jj++)
		{
			jj = checkCombine(jj);
			jj = checkOppose(jj);
			//cout << "\nii=" << ii << " jj = " << jj;
		}
		//cout << "\nFINAL OUTPUT = " ;
		puts(invoke);
		ofstream fout;
		fout.open("output.in" , ios :: app);
		fout << "Case #" << ii+1 << ": ";
		

		if(strlen(invoke) != 0)
			fout << "[" << invoke[0];
		else
			fout << "[" ;
		for(int jj =1; jj<strlen(invoke); jj++)
		{
			fout << ", "<<invoke[jj];
		}
		fout<< "]\n";
		fout.close();

		
	}
	//getch();
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

void readc()
{
	c=0;
	pos++;
	while (arr[pos] != ' ')
	{
		c = (c*10) + ( arr[pos] - 48 );
		pos++;
	}
	//cout << "\nIn readc Arr["<<pos <<"] is " << arr[pos]<<".";
}

void readCombines()
{
	for(int xx=0;xx<c;xx++)
	{
		pos++;
		combine[xx][0]=arr[pos];
		pos++;
		combine[xx][1]=arr[pos];
		pos++;
		com_r[xx]=arr[pos];
		combine[xx][2]='\0';
		pos++;
	}
	//cout << "\nIn read Combines Arr["<<pos <<"] is " << arr[pos];
}

void reado()
{
	pos++;
	o=0;
	while (arr[pos] != ' ')
	{
		o = (o*10) + ( arr[pos] - 48 );
		pos++;
	}
	//cout << "\nIn reado Arr["<<pos <<"] is " << arr[pos] <<".";
}

void readOpposed()
{
	
	for(int xx=0;xx<o;xx++)
	{
		pos++;
		oppose[xx][0]=arr[pos];
		pos++;
		oppose[xx][1]=arr[pos];
		pos++;
		oppose[xx][2]='\0';
		
	}
	//cout << "\nIn readOpposed Arr["<<pos <<"] is " << arr[pos];
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
	//cout << "\nIn End of readn Arr["<<pos <<"] is " << arr[pos];
}

void readInvoke()
{
	pos++;
	int count=0;
	while(arr[pos] != '\n' && arr[pos] != '\0')
	{
		invoke[count]=arr[pos];
		pos++;
		count++;
	}
	invoke[count] = '\0';
}

int checkCombine(int p)
{
	for (int xx=0;xx<c;xx++)
	{
		if(invoke[p] == combine[xx][0])
		{
			if(invoke[p-1] == combine[xx][1])
			{
				invoke[p-1] = com_r[xx];
				int tempLen = strlen(invoke);
				for(int yy=p;yy<tempLen;yy++)
				{invoke[yy] = invoke[yy+1];}
				/*cout << "\nIn First Condition of combine, Invoke = ";  
					puts(invoke);
					cout << " Length of invoke = " << strlen(invoke);*/
			//cout << "\nP = " << p << " TempLen = " << tempLen << "\tNew Length = "<<strlen(invoke);
				return (p-1);
			}
		}
		else if(invoke[p] == combine[xx][1])
		{
			if(invoke[p-1] == combine[xx][0])
			{
				invoke[p-1] = com_r[xx];
				int tempLen = strlen(invoke);
				for(int yy=p;yy<tempLen;yy++)
				{invoke[yy] = invoke[yy+1];}
				//cout << "\n\t"<<strlen(invoke);
			/*	cout << "\nIn Second Condition of combine, Invoke = ";  
					puts(invoke);
					cout << " Length of invoke = " << strlen(invoke);*/
				return (p-1);
			}
		}
	}
	return p;
}

int checkOppose(int p)
{
	for(int xx=0 ; xx<o ; xx++)
	{
		if(invoke[p] == oppose[xx][0])
			for(int yy=0;yy<p;yy++)
			{
				if(invoke[yy] == oppose[xx][1])
				{
					//cout << "\n\t YY = " << yy;
					int temp = p+1;
					int temp2=0;
					while(invoke[temp-1] != '\0')
					{invoke[temp2] = invoke[temp];temp++;temp2++;}
					/*for(int zz = yy; zz<=p && invoke[p + (zz-yy)+1  ] != '\0' ;zz++)
					{
						invoke[zz] = invoke[p + (zz-yy) +1];
						
					}
					//puts(invoke);
					cout << "\nIn First Condition of oppose, Invoke = ";  
					puts(invoke);
					cout << " Length of invoke = " << strlen(invoke);
					*/
					return 0;
				}
			}
		if(invoke[p] == oppose[xx][1])
			for(int yy=0;yy<p;yy++)
			{
				if(invoke[yy] == oppose[xx][0])
				{
					int temp = p+1;
					int temp2=0;
					while(invoke[temp-1] != '\0')
					{invoke[temp2] = invoke[temp];temp++;temp2++;}
					/*for(int zz = yy; zz<=p && invoke[p + (zz-yy)+1] != '\0' ;zz++)
					{
						invoke[zz] = invoke[p + (zz-yy) +1];
						
					}
					cout << "\nIn Second Condition of oppose, Invoke = ";  
					puts(invoke);
					cout << " Length of invoke = " << strlen(invoke);
					*/
					return 0;
				}
			}
	}
	return p;
}