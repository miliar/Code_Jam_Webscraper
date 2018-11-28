#include<iostream.h>
#include<conio.h>
int drainto(int map[100][100],int a,int b, int m, int n);
struct basin{
		int p;
		int q;
	    };
struct output{
		int m;
		int n;
		char c[105][105];
	     };
void main()
{
	int T, H, W, map[100][100], pos, x, y,c,s;
	int i,j,k;
	basin bas[26];
	output out[100];
	cin>>T;
	for(i=0;i<T;i++)
	{
		cin>>H;
		cin>>W;
		for(pos=0;pos<26;pos++)
		{
			bas[pos].p=-1;
			bas[pos].q=-1;
		}
		for(j=0;j<H;j++)
			for(k=0;k<W;k++)
				cin>>map[j][k];
		for(j=0;j<H;j++)
			for(k=0;k<W;k++)
			{
				pos=1;
				x=j;y=k;
				while(pos)
				{     	pos=drainto(map,x,y,H,W);
					switch(pos)
					{
						case 1:x--;break;
						case 2:y--;break;
						case 3:y++;break;
						case 4:x++;break;
					}
				}
				c=0;s=-1;
				while(c>=0)
				{
					s++;
					c=bas[s].p;
					if(bas[s].p==x&&bas[s].q==y)
					{
						c=-2;break;
					}
				}
				if(c==-1)
				{
					bas[s].p=x;
					bas[s].q=y;
				}
				out[i].m=H;
				out[i].n=W;
				out[i].c[j][k]='a'+s;

			}


	}
	j=0;k=0;
	for(i=0;i<T;i++)
	{
		cout<<"Case #"<<i+1<<":\n";
		for(j=0;j<out[i].m;j++)
		{
			for(k=0;k<out[i].n;k++)
			{
				cout<<out[i].c[j][k]<<" ";
			}
			cout<<"\n";
		}
	}
}
int drainto(int map[100][100], int a ,int b, int m, int n)
{
	int pos, small;
	small=map[a][b];
	pos=0;
	if(a&&map[a-1][b]<small)
	{
		small=map[a-1][b];
		pos=1;
	}
	if(b&&map[a][b-1]<small)
	{
		small=map[a][b-1];
		pos=2;
	}
	if((n-1-b)&&map[a][b+1]<small)
	{
		small=map[a][b+1];
		pos=3;
	}
	if((m-1-a)&&map[a+1][b]<small)
	{
		small=map[a+1][b];
		pos=4;
	}
	return pos;
}

