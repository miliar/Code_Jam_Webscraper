#include<stdio.h>
#include<iostream.h>
#include<string.h>
#include<stdlib.h>


struct tinfo
{
	int ah;
	int am;
	int dh;
	int dm;
	bool uflag;
};
int n,na,tat,nb,nat,nbt;
struct tinfo *nainfo,*nbinfo;

void display()
{
	int i;
	for(i=0;i<na;i++)
	{
		printf("%d:%d   %d:%d\n",nainfo[i].ah,nainfo[i].am,nainfo[i].dh,nainfo[i].dm );
	}
	for(i=0;i<nb;i++)
	{
		printf("%d:%d   %d:%d\n",nbinfo[i].ah,nbinfo[i].am,nbinfo[i].dh,nbinfo[i].dm );
	}
}

void setvalue(char *str,struct tinfo *sinfo,int p)
{
	char val[5];

	memset(val,0x00,sizeof(val));
	val[0]=str[0];
	val[1]=str[1];
	sinfo[p].ah = atoi(val);
	memset(val,0x00,sizeof(val));
	val[0]=str[3];
	val[1]=str[4];
	sinfo[p].am  = atoi(val);
	memset(val,0x00,sizeof(val));
	val[0]=str[6];
	val[1]=str[7];
	sinfo[p].dh  = atoi(val);
	memset(val,0x00,sizeof(val));
	val[0]=str[9];
	val[1]=str[10];
	sinfo[p].dm  = atoi(val);
	sinfo[p].uflag = false;

}

void numoftr()
{
	long atime=0;
	long dtime=0;
	int i,j;
	int mindef,pos,iflag;
	
	nat = na;
	nbt = nb;
	
	for(i=0;i<na;i++)
	{
		dtime = nainfo[i].ah *60 + nainfo[i].am ;
		mindef = 25*60;
		iflag=false;
		for(j=0;j<nb;j++)
		{
			atime = nbinfo[j].dh *60 + nbinfo[j].dm  + tat;
			
			if(nbinfo[j].uflag == false && dtime >= atime && mindef > (dtime-atime))
			{
				iflag=true;
				mindef=dtime-atime;
				pos=j;
			}
		}
		if(iflag==true)
		{
			nat--;
			nbinfo[pos].uflag = true;
		}
	}

	for(i=0;i<nb;i++)
	{
		dtime = nbinfo[i].ah *60 + nbinfo[i].am ;
		mindef = 25*60;
		iflag=false;
		for(j=0;j<na;j++)
		{
			atime = nainfo[j].dh *60 + nainfo[j].dm  + tat ;
			if(nainfo[j].uflag == false && dtime >= atime && mindef > (dtime-atime))
			{
				iflag=true;
				mindef=dtime-atime;
				pos=j;
			}
		}
		if(iflag==true)
		{
			nbt--;
			nainfo[pos].uflag = true;
		}
	}
}

int main()
{
	int i,j;
	char str[50];
	FILE *ptr;


	if((ptr=fopen("Result.txt","w+"))==NULL)
	{
		cout<<"File opening Error\n";
		return -1;
	}

	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&tat);
		scanf("%d%d",&na,&nb);
		nainfo = new tinfo[na];
		nbinfo = new tinfo[nb];
		for(j=0;j<na;j++)
		{
			memset(str,0x00,sizeof(str));
			cin.getline(str,50,'\n');
			setvalue(str,nainfo,j);
		}
		for(j=0;j<nb;j++)
		{
			memset(str,0x00,sizeof(str));
			cin.getline(str,50,'\n');
			setvalue(str,nbinfo,j);
		}
		display();
		numoftr();
		printf("Case #%d: %d %d\n",i+1,nat,nbt);
		fprintf(ptr,"Case #%d: %d %d\n",i+1, nat,nbt); 
		delete []nainfo;
		delete []nbinfo;
		
	}
	return 0;
}