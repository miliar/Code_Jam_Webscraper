#include<iostream>
#include<cstring>

# define X "X won"
# define O "O won"
# define G "Game has not completed"
# define D "Draw"

using namespace std;
int main()
{

int n,i=0,j,k,p=0,q=0,r=0,s=0,p1,q1,r1,s1,count=0,result=0;
cin>>n;
char a[5][5],ch;
char a1[5];
cin.get(ch);

for(i=0;i<n;i++)
{
	result=0;
     count=0;
for(j=0;j<5;j++)
{
cin.getline(a[j],5);
a1[j]=a[j][j];
}

for(j=0;j<4;j++)
{
	
    p=0;q=0;r=0;s=0;	
	for(k=0;k<4;k++)
	{
		if(a[j][k]=='X')
		p++;
		if(a[j][k]=='O')
		q++;
		if(a[j][k]=='T')
		r++;
		if(a[j][k]=='.')
		s++;
	}
	if(r==0)
	{
		if(p==4)
		{
		cout<<"Case #"<<i+1<<": "<<X<<"\n";
        result++;
	    }
        if(q==4)
        {
        cout<<"Case #"<<i+1<<": "<<O<<"\n";
	    result++;
	    }
    }
    if(r==1)
    {
		if(p==3)
		{
			cout<<"Case #"<<i+1<<": "<<X<<"\n";
            result++;
        }
        if(q==3)
        {
        cout<<"Case #"<<i+1<<": "<<O<<"\n";
        result++;
	    } 
    }
    if(s>0)
    count=1;
}

if(!result)
{
for(j=0;j<4;j++)
{
    p=0;q=0;r=0;s=0;	
	for(k=0;k<4;k++)
	{
		if(a[k][j]=='X')
		p++;
		if(a[k][j]=='O')
		q++;
		if(a[k][j]=='T')
		r++;
		if(a[k][j]=='.')
		s++;
	}
	if(r==0)
	{
		if(p==4)
		{
		cout<<"Case #"<<i+1<<": "<<X<<"\n";
        result=1;
	    }
        if(q==4)
        {
        cout<<"Case #"<<i+1<<": "<<O<<"\n";
        result=1;
        }
    }
    if(r==1)
    {
		if(p==3)
	    {
	 	cout<<"Case #"<<i+1<<": "<<X<<"\n";
        result=1;
         }
        if(q==3)
         {
        cout<<"Case #"<<i+1<<": "<<O<<"\n";
        result=1;
         }
     }
}
}
if(!result)
{
p=q=r=s=0;
for(j=0;j<4;j++)
{
	    if(a1[j]=='X')
		p++;
		if(a1[j]=='O')
		q++;
		if(a1[j]=='T')
		r++;
		if(a1[j]=='.')
		s++;

}
if(r==0)
{
if(p==4)
{
cout<<"Case #"<<i+1<<": "<<X<<"\n";
result=1;
}
if(q==4)
{
cout<<"Case #"<<i+1<<": "<<O<<"\n";
result=1;
}
}
if(r==1)
{
if(p==3)
{
cout<<"Case #"<<i+1<<": "<<X<<"\n";
result=1;
}
if(q==3)
{
cout<<"Case #"<<i+1<<": "<<O<<"\n";
result=1;
}
}
}
if(!result)
{
	p1=q1=r1=s1=0;
a1[0]=a[0][3];
a1[1]=a[1][2];
a1[2]=a[2][1];
a1[3]=a[3][0];
for(j=0;j<4;j++)
{
	    if(a1[j]=='X')
		p1++;
		if(a1[j]=='O')
		q1++;
		if(a1[j]=='T')
		r1++;
		if(a1[j]=='.')
		s1++;
}
if(r1==0)
{
if(p1==4)
{
cout<<"Case #"<<i+1<<": "<<X<<"\n";
result=1;
}
if(q1==4)
{
cout<<"Case #"<<i+1<<": "<<O<<"\n";
result=1;
}
}
if(r1==1)
{
if(p1==3)
{
cout<<"Case #"<<i+1<<": "<<X<<"\n";
result=1;
}
if(q1==3)
{
cout<<"Case #"<<i+1<<": "<<O<<"\n";
result=1;
}
}
}

if(result==0)
{
	if(count==0)
	cout<<"Case #"<<i+1<<": "<<D<<"\n";
    else
    cout<<"Case #"<<i+1<<": "<<G<<"\n";
}

for(j=0;j<5;j++)
a[j][0]='\0';

}
return 0;
}
