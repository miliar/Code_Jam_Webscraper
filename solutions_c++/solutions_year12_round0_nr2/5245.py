#include<iostream.h>
#include<conio.h>
#include<stdio.h>
#define max 26
// input string is in lower case
int i,j;
int testcase;
int ans[2000],k;
int sp;
int min;
int score,s1,s2,s3,rem,result;
struct input
{
    int ipstr[350];
    input *next;
};
input *ptr,*ip;

int cal()
{
	      input *p;
	      p=ip;
	      sp=p->ipstr[1];
	      min=p->ipstr[2];
	      result=0;
	    //  cout<<"\nmin:"<<min;
	     // cout<<"\nSp:"<<sp;
	      for(j=3;j<p->ipstr[0]+3;j++)
	      {
	       //	cout<<"\nr:"<<result<<" sp:"<<sp;
	       //	cout<<" >"<<p->ipstr[j]<<"<";
		score=p->ipstr[j];
		s1=s2=s3=score/3;
		rem=score%3;
      //		cout<<"\ns1:"<<s1<<" s2:"<<s2<<" rem:"<<rem<<endl;

		if(sp>0)
		{

			if(rem==2)
			{
				if(s1+rem>=min && s1+rem<=10 )
				{
					result++;
					sp--;
					continue;
				}
				if(s1+1>=min)
				{
					result++;
					continue;
				}
			}

		}
		else
		if(sp==0 && rem==2)
		{
			if(s1+1>=min)
			{
				result++;
				continue;
			}

		}

		if(rem==1 && s1+rem>=min )
		{
		      result++;
		      continue;

		}
		if(rem==0)
		{

			if(s1>=min)
			{
			    result++;
			    continue;

			}
			else
			if(s1>0 && sp>0)
			{
			   s1=s1-1;
			   s3=s3+1;
			   if(s3>=min)
			   {
				result++;
				sp--;
				continue;
			   }
			}
		   }

	      }
	      return result;

}
void main()
{
	clrscr();

	cin>>testcase;
	ptr=new input;
	ptr->next=NULL;
	ip=ptr;
	k=0;
	for(i=1;i<=testcase;i++,k++)
	{
	      cin>>ptr->ipstr[0];
	      cin>>ptr->ipstr[1];
	      cin>>ptr->ipstr[2];
	      for(j=0;j<ptr->ipstr[0];j++)
		 cin>>ptr->ipstr[j+3];

	      ans[k]=cal();
	//      cout<<"\n----->"<<ans[k];
	      /*
	      ptr->next=new input;
	      ptr=ptr->next;
	      ptr->next=NULL;

	      */

	}
	ptr=ip;
      //	clrscr();
	for(k=0;k<testcase;k++)
	{
	      cout<<"\nCase #"<<k+1<<": "<<ans[k];

	}
	//clrscr();
	/*
	for(i=1;i<=testcase;i++)
	{

	      cout<<"\nCase #"<<i<<": ";
	      sp=ptr->ipstr[1];
	      min=ptr->ipstr[2];
	      result=0;
	     // cout<<"\nmin:"<<min;
	      //cout<<"\nSp:"<<sp;
	       for(j=3;j<ptr->ipstr[0]+3;j++)
	      {
		cout<<result;
		cout<<" >"<<ptr->ipstr[j]<<"<";
		score=ptr->ipstr[j];
		s1=s2=s3=score/3;
		rem=score%3;
	       //	cout<<"\ns1:"<<s1<<" s2:"<<s2<<" rem:"<<rem<<endl;
		if(s1>=min)
		{
		    result++;
		    continue;
		}

		if(sp>0 && rem==2)
		{
			if(s1+rem>=min && s1+rem!=10 )
			{
				result++;
				sp--;
				continue;
			}
			if(s1+1>=min)
			{
				result++;
				continue;
			}

		}
		else
		if(sp==0 && rem==2)
		{
			if(s1+1>=min)
			{
				result++;
				continue;
			}

		}

		if(rem==1 && s1+rem>=min )
		{
		      result++;
		      continue;

		}
		if(rem==0)
		{
		   s1=s1-1;
		   s3=s3+1;
		   if(s3>=min)
		   {
				result++;
				continue;
		   }
		}
	      }
	      cout<<result;
	      ptr=ptr->next;

	}
	*/
	getch();

}