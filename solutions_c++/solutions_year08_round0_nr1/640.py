#include <stdio.h>
#include <string.h>

char names[105][105];

char query[105];
bool tag[105];


int Find(char q[],char ns[][105],int num)
{
	int i;
     for(i=0;i<num;i++)
		 if(strcmp(q,ns[i])==0)
			 return i;
     return -1;
}

int main()
{
  // freopen("A-small-attempt1.in.txt","r",stdin);
   //freopen("A-small-attempt1.out.txt","w",stdout);
   freopen("A-large.in.txt","r",stdin);
    freopen("A-large.out.txt","w",stdout);
	int n,q,s,i,j,p,result,num,index,ci;


   scanf("%d",&n);
   for(p=0;p<n;p++)
   {
       scanf("%d",&s);
	   getchar();
	   for(i=0;i<s;i++)
	   {
		   gets(names[i]);
       //     printf("%s\n",names[i]);
	   }
       scanf("%d",&q);
	   getchar();
       for(j=0;j<s;j++)
		   tag[j]=false;
       num=0;
       result=0;
       ci=-1;
	   for(i=0;i<q;i++)
	   {

		   gets(query);
           index=Find(query,names,s);
		   if(index!=-1&&tag[index]==false&&index!=ci)
		   {
			   tag[index]=true;
			   num++;
		   }

		   if((ci==-1&&num==s)||(ci!=-1&&num==s-1))
		   {
			   result++;
               num=0;
			   for(j=0;j<s;j++)
		          tag[j]=false;
			   ci=index;
		   }
	   }
       printf("Case #%d: %d\n",p+1,result);
   }

}