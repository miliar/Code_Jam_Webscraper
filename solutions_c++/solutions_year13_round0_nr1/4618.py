#include<cstdio>
#include<iostream>
using namespace std;
char a[5][5];
bool vertical(char c)
{
int count =0,i,j;
for(i=0;i<4;i++)
{
	count=j=0;
		while(j<4 && (a[j][i]==c || a[j][i]=='T'))
		{count++;j++;}
		if(count==4)
		return 1;
}
return 0;
}

bool horizontal(char c)
{
int count=0,i,j;
for(i=0;i<4;i++)
{
        count=j=0;
        //for(j=0;j<4;j++)
        //{
                while(j<4 && (a[i][j]==c || a[i][j]=='T'))
                {count++;j++;}
                if(count==4)
                return 1;
        //}
}
return 0;
}

bool diagonal(char c)
{
int count=0,i=0,j=0;
while(i<4 && j<4 && (a[i][j]==c || a[i][j]=='T'))
{
count++;
i++;j++;
}
if(count==4)
return 1;
count=0;i=0;j=3;
while(i<4 && j>=0 && (a[i][j]==c || a[i][j]=='T'))
{
count++;
i++;j--;
}
if(count==4)
return 1;
}


bool filled()
{
int i,j;
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
if(a[i][j]=='.')
return 0;
}
return 1;
}

int main()
{
int n,m,t,i,j,k=0;
//cin>>t;
scanf("%d",&t);
while(t--)
{
getchar();
for(i=0;i<4;i++)
{
	for(j=0;j<4;j++)
	{
		a[i][j]=getchar();
	}
	getchar();
}

k++;
cout<<"Case #"<<k<<": ";
if(vertical('X') || horizontal('X') || diagonal('X'))
{
cout<<"X won\n";
}
else if(vertical('O') || horizontal('O') || diagonal('O'))
cout<<"O won\n";
else if(filled())
cout<<"Draw\n";
else
cout<<"Game has not completed\n";
}
return 0;
}
