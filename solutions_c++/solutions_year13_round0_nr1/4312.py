//BISMILLAHIR RAHMANIR RAHIM
#include<stdio.h>
int main()
{
	FILE *f1,*f2;
	f1=fopen("in.txt","r");
	f2=fopen("out.txt","w");
	char st[6][6];
	int t,cs=1,i,j,x,y,z,fg,px,py;
	fscanf(f1,"%d",&t);
	while(t--)
	{
		for(i=0;i<4;i++)
			fscanf(f1,"%s",st[i]);
		for(i=fg=px=py=0;i<4;i++)
		{
			for(j=x=y=z=0;j<4;j++)
			{
				if(st[i][j]=='X')
					x++;
				else if(st[i][j]=='O')
					y++;
				else if(st[i][j]=='T')
					z++;
				else
					fg=1;
			}
			if(x==4||(x==3&&z==1))
				px|=1;
			if(y==4||(y==3&&z==1))
				py|=1;
		}
		for(i=0;i<4;i++)
		{
			for(j=x=y=z=0;j<4;j++)
			{
				if(st[j][i]=='X')
					x++;
				else if(st[j][i]=='O')
					y++;
				else if(st[j][i]=='T')
					z++;
				else
					fg=1;
			}
			if(x==4||(x==3&&z==1))
				px|=1;
			if(y==4||(y==3&&z==1))
				py|=1;
		}
		for(i=x=y=z=0;i<4;i++)
		{
			if(st[i][i]=='X')
				x++;
			else if(st[i][i]=='O')
				y++;
			else if(st[i][i]=='T')
				z++;
			else
				fg=1;
		}
		if(x==4||(x==3&&z==1))
				px|=1;
			if(y==4||(y==3&&z==1))
				py|=1;
		for(i=x=y=z=0,j=3;i<4;i++,j--)
		{
			if(st[i][j]=='X')
				x++;
			else if(st[i][j]=='O')
				y++;
			else if(st[i][j]=='T')
				z++;
			else
				fg=1;
		}
		if(x==4||(x==3&&z==1))
			px|=1;
		if(y==4||(y==3&&z==1))
			py|=1;
		fprintf(f2,"Case #%d: ",cs++);
		if((px&&py)||(px==0&&py==0&&fg))
			fprintf(f2,"%s\n","Game has not completed");
		else if(px)
			fprintf(f2,"%s\n","X won");
		else if(py)
			fprintf(f2,"%s\n","O won");
		else
			fprintf(f2,"%s\n","Draw");
	}
	fclose(f1);
	fclose(f2);
	return 0;
}