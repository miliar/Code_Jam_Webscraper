#include<iostream.h>
#include<fstream.h>
#include<string.h>
#include<conio.h>

int test_case, i ,*no_nonbase, j, *no_opp, *len_invoke;
char ***nonbase, ***opp, **invoke, **final_str;

int check_nonbase(char , int, int);
int check_opp(char a[] , int);

void main()
{
	int check, k;
	ifstream inf("input.in");
   ofstream opf("one.o");

   inf>> test_case;
   no_nonbase=new int [test_case];
   len_invoke = new int[test_case];
   no_opp = new int[test_case];
	nonbase= new char ** [test_case];
   opp = new char ** [test_case];
   invoke = new char * [test_case];
   for(i=0 ; i<test_case ; i++)
   {
   	inf>>no_nonbase[i];
      nonbase[i] = new char *[no_nonbase[i]];
      for(j=0 ; j<no_nonbase[i] ; j++)
      	nonbase[i][j]= new char[4];
      j=0;
      while(j<no_nonbase[i])
      {
      	inf>>nonbase[i][j];
         j++;
      };
      inf>>no_opp[i];
      opp[i]= new char*[no_opp[i]];
      for(j=0 ; j<no_opp[i] ; j++)
      	opp[i][j] = new char[3];
      j=0;
      while(j<no_opp[i])
      {
      	inf>>opp[i][j];
         j++;
      };
      inf>>len_invoke[i];
      invoke[i] = new char [len_invoke[i]+1];
      inf>>invoke[i];
   }
   cout<<no_nonbase[76]<<nonbase[76][0]<<no_opp[76]<<opp[76][0]<<len_invoke[76]<<invoke[76];
   getch();

   final_str=new char* [test_case];
   for(i=0 ; i<test_case ; i++)
   {
   	final_str[i] = new char[len_invoke[i]+1];
   	opf<<"Case #"<<(i+1)<<": [";
      final_str[i][0]=invoke[i][0];
//      final_str[i][0]='\0';
	if(len_invoke[i]>1)
   {
      for(j=1 ,k=1; j<len_invoke[i] ; j++,k++)
      {
      	check = check_nonbase(invoke[i][j], i , k);
         if (check)
         	k--;
         final_str[i][k+1]='\0';
         check= check_opp(final_str[i], i);
         if(check)
         {
         	j++;
         	final_str[i][0]=invoke[i][j];
            k=0;
            final_str[i][1]='\0';
         }
      }
      }
      else
    {
      	final_str[i][0]='\0';

    }

          j=0;
      while(final_str[i][j]!='\0')
      {
      	if (j==0)
         	opf<<final_str[i][j];
         else
      		opf<<", "<<final_str[i][j];
         j++;
      };
      opf<<"]"<<endl;
   }





   for(i=0 ; i<test_case ; i++)
   {
   	for(j=0 ;j<no_nonbase[i] ; j++)
      	delete [] nonbase[i][j];
      for(j=0 ; j<no_opp[i] ; j++)
      	delete [] opp[i][j];
   	delete [] nonbase[i];
      delete [] opp[i];
      delete [] invoke[i];
      delete [] final_str[i];
   }
   delete [] opp;
   delete [] final_str;
   delete [] no_nonbase;
   delete [] no_opp;
   delete [] nonbase;
   delete [] len_invoke;
}

int check_nonbase(char a, int i, int j)
{
   int k, check=0;
   char  replace=0;
   k=0;
   while(  k<no_nonbase[i] )
   {
   	if(a== nonbase[i][k][0]||a==nonbase[i][k][1])
      {
      	if(nonbase[i][k][0] == nonbase[i][k][1])
         	goto special;
      	if(final_str[i][j-1]!=a)
         {
         	special:
         	if(final_str[i][j-1]== nonbase[i][k][0]||final_str[i][j-1]==nonbase[i][k][1])
            {
            	replace = nonbase[i][k][2];
               check = 1;
               goto down;
            }
         }
      }
      k++;
	};
   down:
   if(check)
   {
   	final_str[i][j-1]=replace;
      return 1;
   }
   else
   {
   	final_str[i][j]=a;
      return 0;
   }

}

int check_opp(char a[] , int i)
{
	int k=0, j, count1=0, count2=0;
	while( k<no_opp[i] )
   {
   	for(j=0 ; j<strlen(a) ; j++)
      {
      	if(a[j]==opp[i][k][0])
         {
         	count1++;
         }
         if(a[j]==opp[i][k][1])
         {
         	count2++;
         }
      }
      if(count1 && count2)
      	goto down;
      else
      {
      	count1=0;
         count2=0;
      }

   	k++;
   };
   down:
   if(count1 && count2)
   {
   	delete [] final_str[i];
      final_str[i]= new char[len_invoke[i]+1];
      return 1;
   }
   return 0;

}