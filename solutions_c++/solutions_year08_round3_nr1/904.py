
#include<stdio.h>
int partition(int n[],int left,int right);
void quicksort(int n[], int left,int right)
{
int dp;
if (left<right) {

    /*
    ���������Ҫ�����ĺ���������������˵�ģ����ǰ�����С��53������
    ��������ߣ���ķ����ұߣ�Ȼ�󷵻�53��������������е�λ�á�
    */
    dp=partition(n,left,right);

    quicksort(n,left,dp-1);

    quicksort(n,dp+1,right); //���������ǵݹ���ã��ֱ�����53��ߵ�������ұߵ�����
}
}

   
int partition(int n[],int left,int right)
{
int lo,hi,pivot,t;

pivot=n[left];
lo=left-1;
hi=right+1;

while(lo+1!=hi) {
    if(n[lo+1]<=pivot)
      lo++;
    else if(n[hi-1]>pivot)
      hi--;
    else {
      t=n[lo+1];
      n[++lo]=n[hi-1];
      n[--hi]=t;
    }
}

n[left]=n[lo];
n[lo]=pivot;
return lo;
}

int readint(FILE *lp); //���ļ�����һ����void main()
void main()

{   
	int N,P,K,L,total;
	int readint(FILE *lp);
	void writeint(int number,FILE *lp);
	FILE *finput,*foutput;
	
    finput=fopen("A-small-attempt2.in","r");
    foutput=fopen("A-small-attempt2.out","w");
	//int test[17]={0,1,2,3,1,2,1,3};
    //find(3,7,1,test);
	//printf("%d",total);
	//printf("%d\n",cmpstring("ds","ds"));

	N=readint(finput);
	//printf("%d",N);
	int i,j,k,m,time,num;
    int letter[1002];
	for(i=1;i<=N;i++) 
	{  total=0;
		P=readint(finput);
		K=readint(finput);
		L=readint(finput);
		for(j=1;j<=L;j++) letter[j]=readint(finput);
       quicksort(letter,1,L);
	    
       time=L/K;
	   num=L;
	   for(j=1;j<=time;j++)
	   {
		
			for(m=1;m<=K;m++)
			{
				total=total+j*letter[num];
				num--;
			}
	   }
     
		for(j=1;j<=num;j++)
		{
		total+=letter[j]*(time+1);
		
		}

		
       
	   
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

int readint(FILE *lp) //���ļ�����һ������
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

 


///////////////////////////////////////////////////////////////////////////////////////////////

