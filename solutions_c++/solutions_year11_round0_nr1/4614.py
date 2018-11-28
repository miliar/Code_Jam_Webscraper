#include<stdio.h>
#include<conio.h>
FILE *f;
int ocur=1;
int onext=0;
int bnext=0;
int bcur=1;
int sec=0;
void func(char bot[],int move[] ,int len)
{
  int i=0;
  for(i=0;i<len;i++)
  {
	if(bot[i]=='O')
	{
	 while(ocur!=move[i])
	 {
	  if((bcur<bnext) && bnext<=100)
		bcur++;
	  if((bcur>bnext) && bnext!=0)
		bcur--;
	  if(ocur<move[i])
		ocur++;
	  if(ocur>move[i])
		ocur--;
	  sec++;
	 }
	 if(ocur==move[i])
	 {
		sec++;
		if((bcur<bnext) && bnext<=100)
			bcur++;
		if((bcur>bnext) && bnext!=0)
			bcur--;
	 }
	 int j=i+1;
	 while((bot[j]!='O') && (j<len))
		 j++;
	 onext=move[j];
	}
	if(bot[i]=='B')
	{
	 while(bcur!=move[i])
	 {
	  if((ocur<onext) && onext<=100)
		ocur++;
	  if((ocur>onext) && onext!=0)
		ocur--;
	  if(bcur<move[i])
		bcur++;
	  if(bcur>move[i])
		bcur--;
	  sec++;
	 }
	 if(bcur==move[i])
	 {	sec++;
		if((ocur<onext) && onext<=100)
			ocur++;
		if((ocur>onext) && onext!=0)
			ocur--;
	 }
	 int j=i+1;
	 while((bot[j]!='B') && (j<len))
		 j++;
	 bnext=move[j];
	}
  }
}
void main()
{
 clrscr();
 FILE *f1;
 f=fopen("large.in","r");
 f1=fopen("op.txt","w");
 if(f==NULL)
	printf("file not exists");

 int test_num=0;
 fscanf(f,"%d",&test_num);
// printf("%d",test_num);
 int t=1;
 while((!feof(f)) && (t<=test_num))
 {
	int num_moves=0,k=1,seq_move[120];
	char seq_char[120];
	fscanf(f,"%d",&num_moves);
	while(k<=num_moves)
	{
	 char bot='a';
	 int move=0;
	 fscanf(f," %c",&bot);
	 fscanf(f,"%d",&move);
	 printf("read:-%d__%d__%c__%d",t,k,bot,move);
	 seq_char[k-1]=bot;
	 seq_move[k-1]=move;
	 k++;
	}
//	getch();
	int l=0;
	while(seq_char[l]!='O')
		l++;
	onext=seq_move[l];
	l=0;
	while(seq_char[l]!='B')
		l++;
	bnext=seq_move[l];

	func(seq_char,seq_move,num_moves);
	ocur=1;
	bcur=1;

	printf("\ncase#%d:%d\n",t,sec);
	fprintf(f1,"Case #%d: %d\n",t,sec);
	sec=0;
	t++;
 }
 fclose(f1);
 fclose(f);
 getch();
}