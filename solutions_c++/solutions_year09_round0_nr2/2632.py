#include<fstream.h>
#include<conio.h>

char small(int i,int j,char &ch,int map[100][100],char newmap[100][100])
{  	int s[4],min;
	if(i!=0)
	s[0]=map[i-1][j];
	else
	s[0]=10000;

	if(j!=0)
	s[1]=map[i][j-1];
	else
	s[1]=10000;

	if(j!=99)
	s[2]=map[i][j+1];
	else
	s[2]=10000;

	if(i!=99)
	s[3]=map[i+1][j];
	else
	s[3]=10000;


	min=s[0];
	for(int k=1;k<4;k++)
	{      	if(min>s[k])
		{	min=s[k];
		}
	}
	for(k=0;k<4;k++)
	{      	if(min==s[k])
		{	break;
		}
	}
	//cout<<k<<"a"<<min<<endl;
	if(min<map[i][j])
	{	switch(k)
		{	case 0 : newmap[i-1][j]=small(i-1,j,ch,map,newmap);
				 return newmap[i-1][j];
			 break;
			case 1 : newmap[i][j-1]=small(i,j-1,ch,map,newmap);
				 return newmap[i][j-1];
			 break;
			case 2 : newmap[i][j+1]=small(i,j+1,ch,map,newmap);
				 return newmap[i][j+1];
			 break;
			case 3 : newmap[i+1][j]=small(i+1,j,ch,map,newmap);
				 return newmap[i+1][j];
			 break;
		}
	}
	else
	{	if(newmap[i][j]=='O')
		{	return ch++;
		}
		else
		{	return newmap[i][j];
		}
	}
}

void labelmap(int h,int w,int map[100][100],char newmap[100][100])
{       char ch='a';

	for(int i=0;i<100;i++)
	{	for(int j=0;j<100;j++)
		{     	newmap[i][j]='O';
		}
	}
	for(i=0;i<h;i++)
	{       cout<<i<<endl;
		for(int j=0;j<w;j++)
		{     	newmap[i][j]=small(i,j,ch,map,newmap);
		}
	}
	//clrscr();
	for(i=0;i<h;i++)
	{       cout<<endl;
		for(int j=0;j<w;j++)
		{     	cout<<newmap[i][j]<<" ";
		}
	}

}



void main()
{       clrscr();
	fstream f,o;
	f.open("dinputf.in",ios::in);
	o.open("doutputf.out",ios::out|ios::app);
	int ch,t,i=0,h,w,j,k,map[100][100];
	char newmap[100][100];

	while(f>>ch)
	{	cout<<ch;
		t=ch;
		break;
	}
	//cout<<t<<endl;
	clrscr();
	for(i=1;i<=t;i++)
	{       for(j=0;j<100;j++)
		{	for(k=0;k<100;k++)
			{     	map[j][k]=10000;
			}
		}
		clrscr();
		f>>ch;
		h=ch;
		f>>ch;
		w=ch;
		for(j=0;j<h;j++)
		{	for(k=0;k<w;k++)
			{       f>>ch;
				map[j][k]=ch;
			}
		}

		//clrscr();
		cout<<endl;
		cout<<"map "<<i;
		for(j=0;j<h;j++)
		{       cout<<endl;
			for(k=0;k<w;k++)
			{	cout<<map[j][k]<<" ";
			}
		}
		cout<<endl<<endl;
		labelmap(h,w,map,newmap);
		o<<"Case #"<<i<<":";
		for(j=0;j<h;j++)
		{       o<<endl;
			for(k=0;k<w;k++)
			{	o<<newmap[j][k]<<" ";
			}
		}
		o<<endl;
		getch();
	}
	o.close();
	f.close();
	getch();
}