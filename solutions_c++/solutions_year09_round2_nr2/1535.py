#include<fstream.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>

/*int fact(int n)
{
	if(n==1)
	{	return n;
	}
	else
	{	return n*fact(--n);
	}

} */


void sort(int tmp[10],long int n)
{       int tp;
	for(int i=0;i<n;i++)
	{       for(int j=i+1;j<n;j++)
		{	if(tmp[i]>tmp[j])
			{	tp=tmp[i];
				tmp[i]=tmp[j];
				tmp[j]=tp;

			}
		}
	}
}

int parse(int tmp[10],long int n)
{	long int f=1,i;
	while(n>f)
	{	f=10*f;
	}
	f=f/10;
	//cout<<endl<<endl;
	i=0;
	while(n)
	{	tmp[i]=n/f;
		n=n%f;
		f=f/10;
		//cout<<tmp[i]<<" ";
		i++;
	}
	sort(tmp,i);
	//for(int j=0;j<i;j++)
	//{	cout<<tmp[j]<<" ";
	//}
	//cout<<endl;
	//cout<<"digit"<<i;
	return i;
}

int cmpare(int l,int ltmp,int tmp[10],int ctmp[10])
{       int i=0,z=0;
	while(ctmp[i]==0)
	{	i++;
	}
	while(tmp[z]==0)
	{	z++;
	}
	for(int k=i,m=z;k<l;k++,m++)
	{	if(tmp[m]!=ctmp[k])
		{	return 0;
		}
	}
	if(m<ltmp)
	{	return 0;
	}
	return 1;
}



long int generate(long int n,int tmp[10],int ltmp)
{     	int j,ctmp[10],flag=0,l;
	//int f;long int st[720];
	//f=fact(i)*i;
	//cout<<f;
	//cout<<endl<<n;
	while(1)
	{       for(int i=0;i<10;i++)
		{       ctmp[i]=0;
		}
		n++;
		//cout<<endl<<n;
		l=parse(ctmp,n);
		flag=cmpare(l,ltmp,tmp,ctmp);
		if(flag==1)
		{    	break;
			break;
		}
	}
	return n;
}



void main()
{	int t;
	//long int ;
	//char ;
	int chs;
	long int n,nxt;

	int tmp[10],l;
	long int chl;
	//char chstr;
	fstream f,o;


	clrscr();

	f.open("asinput.in",ios::in);
	o.open("asoutput.out",ios::out|ios::app);

	f>>chs;
	cout<<chs;
	t=chs;
	cout<<endl;
	for(int i=1;i<=t;i++)
	{       for(int z=0;z<10;z++)
		{       tmp[z]=0;
		}
		f>>chl;
		n=chl;
		//cout<<n<<endl;
		l=parse(tmp,n);
		//cout<<"tl"<<l<<endl;
		nxt=generate(n,tmp,l);
		//cout<<endl<<"next"<<nxt;

		o<<"Case #"<<i<<": ";
		o<<nxt<<endl;
	}

	f.close();
	o.close();
	getch();
}