
#include<stdio.h>
#include<string.h>

//#define LMT 256


int smin(char str[],int n)
{
	int min=0;
	for(int ii=1;ii<n;ii++)
	{
		for(int jj=0;jj<52;jj++)
			if(str[ii*52+jj]<str[min*52+jj])
			{
				min=ii;
				break;
			}
			else if(str[ii*52+jj]>str[min*52+jj])
				break;
	}
	return min;
}
bool sequ(char*stra,char*strb)
{
	int ii=52;
	while(ii--,stra[ii]==strb[ii]&&ii>=0)
	{
	}
	if(ii==-1)return true;
	return false;
}
bool greater(char*stra,char*strb)
{
	int ii=0;
	while(ii<52)
	{
		if(stra[ii]>strb[ii])
			return true;
		else if(stra[ii]<strb[ii])
			return false;
		ii++;
	}
	return false;
}
void firsec(char str[],int n,int &fir,int&sec)
{
	fir=0;sec=1;
	for(int jj=0;jj<52;jj++)
	{
		if(str[jj]<str[52+jj])
		{
			fir=1;sec=0;
			break;
		}
		else if(str[jj]>str[52+jj])
			break;
	}	
	for(int ii=2;ii<n;ii++)
	{
		for(int jj=0;jj<52;jj++)
		{
			if(str[ii*52+jj]>str[sec*52+jj])
			{
				sec=ii;
				if(jj!=0&&str[fir*52+jj-1]!=0)break;
				while(jj<52)
				{
					if(str[ii*52+jj]>str[fir*52+jj])
					{
						sec=fir;
						fir=ii;
					}
					else if(str[ii*52+jj]<str[fir*52+jj])
						break;
					jj++;
				}
				break;
			}
			else if(str[ii*52+jj]<str[sec*52+jj])
				break;

		}	
	}

}

void ssub(char*strbg,char*strsm)
{
	int ii=52-1,s=0;
	while(ii>=0)
	{
		if((strbg[ii]-=strsm[ii]+s)<0)
		{
			strbg[ii]=10+strbg[ii];
			s=1;
		}
		else
			s=0;
		ii--;
	}
}
void sadd(char*strbg,char*strsm)
{
	int ii=52-1,s=0;
	while(ii>=0)
	{
		if((strbg[ii]+=strsm[ii]+s)>=10)
		{
			strbg[ii]-=10;
			s=1;
		}
		else
			s=0;
		ii--;
	}
}

int gcd(char* str,int n)
{
	if(n==1)return 0;
	int f,s,fp=0;
	firsec(str,n,f,s);
	for(int ii=0;ii<52;ii++)
		if(str[ii+52*s]!=0)fp=1;
		
	if(fp==0)return f;

	while(!sequ(str+f*52,str+s*52))
	{
		firsec(str,n,f,s);
		ssub(str+f*52,str+s*52);
		
	}
return f;
}

//long long compt(int r,int n,int k,int*buf)
//{
//
//
//}

int main(int argc, char* argv[])
{
	int l,i,j;
	char ch,pch,cch;
	FILE*fr,*fw;
	char*strr,*strw,*sbuf,*sbufb;
	int N,K,R;
	strr= "B-small-attempt2.in";
	strw= "B-small-attempt2.out";

	fr=fopen(strr,"r");
	if(fr==NULL)
	{
		printf("fopen failed:%s\n",strr);
		return 1;
	}
	fw=fopen(strw,"w");
	if(fr==NULL)
	{
		printf("fopen failed:%s\n",strw);
		fclose(fr);
		return 2;
	}

	ch=fgetc(fr);
	l=0;
	while(ch>='0'&&ch<='9')
	{
		l*=10;
		l+=ch-'0';
		ch=fgetc(fr);
	}
	i=0;
	sbufb=new char[52*1000*2];
	sbuf=sbufb+52*1000;
	while(++i<=l)
	{
		pch=0;
		fprintf(fw,"Case #%d: ",i);

		fscanf(fr,"%d",&N);
		fgetc(fr);
		for(int ii=0;ii<52*1000*2;ii++)
			sbufb[ii]=0;
		int ns=0,nc;
		for(int ii=0;ii<N;ii++)
		{
			nc=0;
			ch=fgetc(fr);
			while(ch>='0'&&ch<='9')
			{
				sbufb[(ns)*52+nc]=ch;
//				sbuf[(ns)*52+nc]=ch-'0';
				ch=fgetc(fr);
				nc++;
			}
			int len=strlen(sbufb+(ns)*52);

			for(int jj=0;jj<52;jj++)
				sbuf[(ns)*52+jj]=0;
			for(int jj=0;jj<len;jj++)
				sbuf[(ns+1)*52-len+jj]=sbufb[(ns)*52+jj]-'0';
			len=52;
			while(len>0){sbufb[(ns+1)*52-len]=sbuf[(ns+1)*52-len];len--;}
			ns++;
		}
		int min=smin(sbuf,N);
		for(int ii=0;ii<N;ii++)
		{
			if(ii==min)continue;
			ssub(sbuf+ii*52,sbuf+min*52);
		}
		ssub(sbuf+min*52,sbuf+min*52);
		for(int ii=min*52;ii<52*(N-1);ii++)
			sbuf[ii]=sbuf[ii+52];
		N--;

//		if(i==11)
//			i=i;

		int ngcd=
		gcd(sbuf,N);



		int tmp;
		//min=smin(sbufb,N);
		if(min==0)
			tmp=1;
		else
			tmp=0;
		for(int ii=tmp*52;ii<tmp*52+52;ii++)
			sbufb[ii]=0;
		while(greater(sbufb+min*52,sbufb+tmp*52))
		{
			sadd(sbufb+tmp*52,sbuf+ngcd*52);
		}
		
		//ssub(sbufb+tmp*52,sbuf+ngcd*52);
		ssub(sbufb+tmp*52,sbufb+min*52);
		int m;
		m=0;
		while(!sbufb[tmp*52+m]&&m<52-1)m++;
		for(int ii=m;ii<52;ii++)
			sbufb[tmp*52+ii]+='0';
		sbufb[tmp*52+52]=0;
		fputs(sbufb+tmp*52+m,fw);
		//fgets(buf,LMT,fr);
		fputc('\n',fw);
		//printf("%d",i);
	}
	fclose(fw);
	fclose(fr);

	return 0;
}

