#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int n;
	cin>>n;
	char ch;
	int i=0;
	char a[200];
	getchar();
	for(int j=0;j<n;j++)
	{
		i=0;
      
	while((ch=getchar())!='\n')
	{
		if(ch=='a')
		a[i++]='y';
		else if(ch=='b')
		a[i++]='h';
		else if(ch=='c')
		a[i++]='e';
		else if(ch=='d')
		a[i++]='s';
		else if(ch=='e')
		a[i++]='o';
 		else if(ch=='f')
		a[i++]='c';
		else if(ch=='g')
		a[i++]='v';
		else if(ch=='h')
		a[i++]='x';
		else if(ch=='i')
		a[i++]='d';
		else if(ch=='j')
		a[i++]='u';
		else if(ch=='k')
		a[i++]='i';
		else if(ch=='l')
		a[i++]='g';
		else if(ch=='m')
		a[i++]='l';
		else if(ch=='n')
		a[i++]='b';
		else if(ch=='o')
		a[i++]='k';
		else if(ch=='p')
		a[i++]='r';
 		else if(ch=='r')
		a[i++]='t';
		else if(ch=='s')
		a[i++]='n';
		else if(ch=='t')
		a[i++]='w';
		else if(ch=='u')
		a[i++]='j';
		else if(ch=='v')
		a[i++]='p';
		else if(ch=='w')
		a[i++]='f';
		else if(ch=='x')
		a[i++]='m';
		else if(ch=='y')
		a[i++]='a';
		else if(ch=='z')
		a[i++]='q';
		else if(ch=='q')
		a[i++]='z';

		else
		a[i++]=ch;


		if(i==1)
		cout<<"Case #"<<j+1<<": ";

		cout<<a[i-1];
	}
	cout<<endl;
}

    /*    a['a']=y
		b=h abcdefghijklmnopqrstuvwxy
		c=e
		d=s
		e=o
		f=c
		g=v
		h=x
		i=d
		j=u
		k=i
		l=g
		m=l
		n=b
		o=k
		p=r
		r=t
		s=n
		t=w
		u=j
		v=p
		w=f
		x=m
		y=a
		z=q



	
	*/
	//cin>>n;
	//cin>>n;
 	return 0;
}
