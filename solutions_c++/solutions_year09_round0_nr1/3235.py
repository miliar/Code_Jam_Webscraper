#include<iostream.h>
#include<string.h>
#include<conio.h>
#include<fstream.h>
void main()
{
       fstream fp("C:\\mytest.txt",ios::in);
       char a[500],dir[25][10],temp[20];
       int lk,d,n,i,j,k,l,status[25],cnt,tmp,tmp1,len;
       clrscr();

       fp>>lk>>d>>n;
       for(i=0;i<d;i++)
       {
	    fp>>dir[i];
       }
       /*for(i=0;i<d;i++)
       {
	    cout<<dir[i];
	    cout<<endl;
       } */
       for(i=0;i<n;i++)
       {
	      fp>>a;
	      j=0;
	      k=0;
	      for(tmp=0;tmp<25;tmp++)
	      {
		   status[tmp]=1;
	      }
	      len=strlen(a);
	      while(j<len)
	      {
		    if(a[j]=='(')
		    {
			  j++;
			  l=0;
			  while(a[j]!=')')
			  {
			       temp[l]=a[j];
			       l++;
			       j++;
			  }
			  for(tmp=0;tmp<d;tmp++)
			  {
			       for(tmp1=0;tmp1<l;tmp1++)
			       {
				     if(dir[tmp][k]==temp[tmp1]&&status[tmp]==1)
					    break;
			       }
			       if(tmp1==l)
				status[tmp]=0;
			  }
		    }
		    else
		    {
			  for(tmp=0;tmp<d;tmp++)
			  {
				 if(dir[tmp][k]!=a[j]&&status[tmp]==1)
				    status[tmp]=0;
			  }

		    }
		    j++;
		    k++;
	      }
	      cnt=0;
	      for(tmp=0;tmp<d;tmp++)
	      {
		     if(status[tmp]==1)
			 cnt++;
	      }
	      cout<<"Case #"<<(i+1)<<": "<<cnt<<endl;
       }
       getch();
}