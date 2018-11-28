#include<stdio.h>
#include<math.h>
#include<string.h>

int nr[100];

long long int calc(int len,int baza)
{
	int i;
	long long int sec=0;

	for(i=0;i<len;i++)
		sec+=(long long int) nr[i]*pow(baza,len-i-1);
	return sec;
}		
	

long long int solve(char s[70])
{
	int i,len,frecv[100],baza=0,val[100],curent;

	len=strlen(s)-1;
	memset(frecv,0,sizeof(frecv));

	for(i=0;i<len;i++)
	{
		if(s[i]>='0' && s[i]<='9')
			frecv[s[i]-'0']++;
		else
			frecv[s[i]-'a'+10]++;
	}

	for(i=0;i<100;i++)
		if(frecv[i]>0)
			baza++;
	if(baza==1)
		baza=2;
	memset(frecv,0,sizeof(frecv));
	if(s[0]>='0' && s[0]<='9')
	{
		val[s[0]-'0']=1;
		frecv[s[0]-'0']++;
	}
	else
	{
		val[s[0]-'a'+10]=1;
		frecv[s[0]-'a'+10]++;
	}

	curent=0;
	
	for(i=1;i<len;i++)
	{
		if(s[i]>='0' && s[i]<='9')
		{
			if(frecv[s[i]-'0']==0)
			{
				val[s[i]-'0']=curent;
				frecv[s[i]-'0']++;
				if(curent==0)
					curent=2;
				else
					curent++;
			}
		}
		else
		{
			if(frecv[s[i]-'a'+10]==0)
			{
				val[s[i]-'a'+10]=curent;
				frecv[s[i]-'a'+10]++;
				if(curent==0)
					curent=2;
				else
					curent++;
			}
		}
	}

	memset(nr,0,sizeof(nr));
	for(i=0;i<len;i++)
	{
		if(s[i]>='0' && s[i]<='9')
			nr[i]=val[s[i]-'0'];
		else
			nr[i]=val[s[i]-'a'+10];
	}
	return calc(len,baza);
}
	

int main()
{
	int t,i;
	FILE *f=fopen("base.in","r");
	FILE *g=fopen("base.out","w");
	char s[70];

	fscanf(f,"%i\n",&t);
	for(i=0;i<t;i++)
	{
		fgets(s,70,f);
		fprintf(g,"%s%i%s%lli\n","Case #",i+1,": ",solve(s));
	}
	fclose(f);
	fclose(g);
	return 0;
}		

	
	