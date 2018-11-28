#include<stdio.h>
#include<conio.h>
char arrO[100][3];
char arrB[100][3];
int find_no_of_seconds(int k ,int l,int no)
{	int j = 0,m = 0,n = 1,flag = 0,bbutton_no = 1,obutton_no = 1,bbuttonflag = 0,obuttonflag = 0;
	int next_button_no = 0;
	for(int i = 1;;i++)
	{

		flag = 0;
		if(j < l)
	       {
		if(arrB[j][1] == bbutton_no && arrB[j][2] == n) //Push the button
		{
		  flag = 1;

		  if(arrB[j+1][1] < arrB[j][1])
		      bbuttonflag = 1;

		      j++;

		}
		else if(arrB[j][1] > bbutton_no && bbuttonflag == 0)						//Move the button
		{
		    bbutton_no++;

	       }
	       else if(bbuttonflag == 1)
	       {
		   bbutton_no--;
		   if(bbutton_no == arrB[j][1])
		     bbuttonflag = 0;
	       }
	       }
	       if(m < k)
	       {
		if(arrO[m][1] == obutton_no && arrO[m][2] == n) //Push the button
		{
		   flag = 1;

		   if(arrO[m+1][1] < arrO[m][1])
		     {
		      obuttonflag = 1;
		      }
		   m++;

		}
		else if(arrO[m][1] > obutton_no && obuttonflag == 0)						//Move the button
		{

		      obutton_no++;

		}
		else if(obuttonflag == 1)
		{
			obutton_no--;
			if(obutton_no == arrO[m][1])
			   obuttonflag = 0;
		}
		}
		if(flag == 1)
		{
			n++;
		}
		if(n > no)
		{
			break;
		}

	}
	return i;
}
int main()
{
    freopen("in.txt" ,"r+",stdin);
    freopen("out.txt" ,"w+",stdout);
    int num_of_cases = 0;
    char ch;
    int button_no;
    int no_of_buttons;
    int serial_no = 1;
    int no_of_seconds;
    scanf("%d",&num_of_cases);
    for(int i=0;i<num_of_cases;i++)
    {
      serial_no = 1;
      scanf(" %d ",&no_of_buttons);
      for(int j=0,k=0,l=0;j<no_of_buttons;j++)
      {

       scanf("%c %d ",&ch,&button_no);
      // printf("%c %d\n",ch,button_no);
       if(ch == 'O' || ch == 'o')
       {
			arrO[k][0] = 'O';
			arrO[k][1] = button_no;
			arrO[k][2] = serial_no;
			k++;
       }
       else if(ch == 'b' || ch == 'B')
       {
			arrB[l][0] = 'B';
			arrB[l][1] = button_no;
			arrB[l][2] = serial_no;
			// printf("%c %d %d\n",arrB[l][0] ,arrB[l][1],arrB[l][2]);
			l++;
       }
       serial_no++;
      }
      no_of_seconds = find_no_of_seconds(k,l,no_of_buttons);
      printf("Case #%d: %d\n",i+1 ,no_of_seconds);

    }
      fclose(stdin);
      fclose(stdout);

    return 1;
}
