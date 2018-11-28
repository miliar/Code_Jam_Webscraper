// QR_A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "QR_A.h"

using namespace std;

int L=0,D=0,N=0;

char ** dict;
bool IsLetterHere(char ch,int position)
{
	if(ch=='\0')return false;
	for(int i=0;i<D;i++)
	{
		if(ch==dict[i][position])
		{
			return true;
		}
	}
	return false;
}
bool CharInStr(char ch,char * str)
{
	if(str==NULL)
		return false;
	if(str[0]=='\0')
		return false;
	int length=strlen(str);
	for(int i=0;i<length ;i++)
		if(str[i]==ch)
			return true;
	return false;
}

int match(char * str)
{
	int i=0,j=0,k=0;
	char ** letters=new char *[L+1];
	letters[0]=new char[256];
	memset(letters[0],0,255);
	char tmp;
	bool isgroup=false;
	int count=0;
	for(i=0;i<strlen(str);i++)
	{
		tmp=str[i];
		if(tmp=='\n'||tmp=='\r')
		{
			continue;
		}		
		else if(tmp=='(')
		{
			isgroup=true;
		}
		else if(tmp==')')
		{
			isgroup=false;
			letters[++j]=new char[256];
			memset(letters[j],0,255);
			k=0;
		}
		else
		{
			if(isgroup)
			{
				if(IsLetterHere(tmp,j))
				{
					letters[j][k]=tmp;
					k++;
					letters[j][k]='\0';
				}
			}
			else
			{
				if(!IsLetterHere(tmp,j))
					return 0;
				letters[j][k]=tmp;
				k++;
				letters[j][k]='\0';
				letters[++j]=new char[256];
				memset(letters[j],0,255);
				k=0;
			}
		}
	}
	int diclen;
	for(int i=0;i<D;i++)
	{
		diclen=strlen(dict[i]);
		for(j=0;j<L;j++)
		{
			if(! CharInStr( dict[i][j],letters[j]) )
				break;
		}
		if(j>=diclen)
			count++;
	}
	return count;
}

int _tmain(int argc, TCHAR* argv[], TCHAR* envp[])
{
	FILE * fp=fopen("A-small-attempt1.in","r");
	if(!fp)
	{
		printf("file error!\n");
		return 0;
	}
	fscanf(fp,"%d %d %d",&L,&D,&N);
	
	dict=new char *[D+1];
	char * buf;
	int i=0;
	//Build Dictionary
	i=0;
	while(i<D)
	{
		buf=new char[256];
		memset(buf,0,255);
		
		fgets(buf,255,fp);
		if(buf[0]=='\0'||buf[0]=='\r'||buf[0]=='\n')
			continue;
		dict[i]=new char[16];
		memset(dict[i],0,15);
		if(buf[strlen(buf)-1]=='\n')
			buf[strlen(buf)-1]='\0';
		strncpy(dict[i],buf,strlen(buf)+1);
		
		delete [] buf;
		i++;
	}
	
	i=0;
	int k;
	FILE * fpout=fopen("A-small-attempt1.out","w");
	while(i<N)
	{
		buf=new char[256];
		memset(buf,0,255);
		fgets(buf,255,fp);
		if(buf[0]=='\0'||buf[0]=='\r'||buf[0]=='\n')continue;
		k=match(buf);
		fprintf(fpout,"Case #%d: %d\n",i+1,k);
		printf("Case #%d: %d\n",i+1,k);
		delete [] buf;
		i++;
	}
	fclose(fpout);
	fclose(fp);
	return 0;
}
