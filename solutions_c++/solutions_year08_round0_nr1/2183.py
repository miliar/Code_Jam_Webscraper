
#include<stdio.h>
int readint(FILE *lp); //从文件读入一个整数
void writeint(int number,FILE *lp);//向文件输入一个整数
void readstring(char out[],FILE *lp);//从文件读入一个字符串
void writestring(char in[],FILE *lp);
int cmpstring(char s1[],char s2[]);//比较两个字符串，相等返回1，否则返回0
void find(int s,int Q,int beginnum,short Qline[]);
int total=0;

void main()
{   int N,S,Q;
	int readint(FILE *lp);
	void writeint(int number,FILE *lp);
	FILE *finput,*foutput;
	char temp[101];
    finput=fopen("A-large(2).in","r");
    foutput=fopen("A-large(2).out","w");
	//int test[17]={0,1,2,3,1,2,1,3};
    //find(3,7,1,test);
	//printf("%d",total);
	//printf("%d\n",cmpstring("ds","ds"));

	N=readint(finput);
	//printf("%d",N);
	int i,j,k;
    char engine[101][101];
	short test[1001];
	for(i=1;i<=N;i++) 
	{  total=0;
	   S=readint(finput);
       for(j=1;j<=S;j++)
	   {
		   readstring(engine[j],finput);
		   //fprintf(foutput,"%s\n",engine[j]);
	   }
	   char temp1[101];
	   Q=readint(finput);
	 
	   for(j=1;j<=Q;j++)
	   {   readstring(temp1,finput);
		   k=1;
		   while(cmpstring(temp1,engine[k])==0) k++;
		   test[j]=k;
		   //fprintf(foutput,"%s %d\n",temp1,k);
	   }
	   find(S,Q,1,test);
       fprintf(foutput,"Case #%d: %d",i,total);
	   
	   fputc(10,foutput);
	}
    //readint(finput);
	/*for(int i=0;i<=100;i++)
	{
	readstring(temp,finput);
	printf("%s\n",temp);
	}*/
	//char c;
	//writeint(-846,foutput);
	//printf("%d",readint(finput));
	//fprintf(foutput,"%d",readint(finput));
	/*while((c=fgetc(finput))!=10)
	{
		fputc(c,foutput);
       
	}*/
	//c=fgetc(finput);
	//fputc(c,foutput);
	fclose(finput);
	fclose(foutput);
}
///////////////////////////////////////////////////////////////////////////////////////////////

int readint(FILE *lp) //从文件读入一个整数
{
	char c;
	int sum=0;
	c=fgetc(lp);
	while((c>='0')&&(c<='9'))
	{   sum*=10;
	    sum+=c-'0';
		c=fgetc(lp);
	}
	return sum;
}
///////////////////////////////////////////////////////////////////////////////////////////////


void writeint(int number,FILE *lp)//向文件输入一个整数
{
	char string[10];
	int i=0,temp;
	temp=number;
	if(number<0)
	{
		fputc('-',lp);
	
		temp=-number;
	}
	while(temp/10!=0)
	{
		string[i]=temp%10+48;
		i++;
		temp/=10;
	}
	string[i]=temp%10+48;
	for(int j=i;j>=0;j--)
		fputc(string[j],lp);
	
}

///////////////////////////////////////////////////////////////////////////////////////////////


void readstring(char out[],FILE *lp)//从文件读入一个字符串
{  char ch;
   
   int i=0;
   ch=fgetc(lp);
   while(ch!=10)
   { out[i]=ch;
     i++;
	 ch=fgetc(lp);
   }
   out[i]='\0';
   
}
///////////////////////////////////////////////////////////////////////////////////////////////
int cmpstring(char s1[],char s2[])//比较两个字符串，相等返回1，否则返回0
{
  int i=0;
  while((s1[i]!='\0')&&(s1[i]==s2[i]))
  {
	  i++;
	  
  }
  if ( (s1[i]==s2[i]) && (s1[i]=='\0') )
	  return 1;
  return 0;
}
///////////////////////////////////////////////////////////////////////////////////////////////
void find(int s,int Q,int beginnum,short Qline[]) 
{   
    short sflag[101]; //s 个标志序列
	int i=beginnum,flag=s,j;
	
	for(j=1;j<=s;j++)//标志序列置零
	{
       sflag[j]=0;
	}
	while((flag>0)&&(i<=Q))
	{   

		if(sflag[Qline[i]]==0)
		{
			sflag[Qline[i]]=1;
			flag--;
		}
		
        i++;
	}
	if(flag==0)
	{
		total++;
	    find(s,Q,i-1,Qline);
	}
	
}
///////////////////////////////////////////////////////////////////////////////////////////////
void writestring(char in[],FILE *lp)
{   int i=0;
	char cl;
	cl=in[i];
	while(cl!='\0')
	{
		fputc(cl,lp);
        i++;
	}
}