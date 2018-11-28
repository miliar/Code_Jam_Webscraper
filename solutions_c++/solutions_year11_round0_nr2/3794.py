#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
	int l,t,c1,d,n,i;
	scanf("%d",&t);
	l=1;
	while(l<=t)
	{
			char a,b,c;
		char a2[2];
		scanf("%d",&c1);
		if(c1==1){
	scanf("\t%c%c%c",&a,&b,&c);}
	scanf("\t%d",&d);
	if(d==1){
	scanf("\t%s",a2);
	}
	scanf("\t%d",&n);
	char r[n];
	scanf("\t%s",r);
	if(c1==0 && d==0)
	{
             printf("Case ");
													printf("#");
												printf("%d",l);
											printf(":");
												printf(" ");
												printf("[");
             for(i=0;i<n;i++)
             {
                            	char u=' ';
													char u1=',';
													if(i!=(n-1))
													{
													printf("%c%c%c",r[i],u1,u);
													}
													if(i==(n-1))
													{
														printf("%c",r[i]);
														}
														 }
														 printf("]");
														 cout<<endl;
														 l++;
                                                      }
                      else
                      {                                
	int k,flag;
	char g[]="111111111111111111111111111111";
	g[0]=r[0];
	for(i=1;i<n;i++)
	{
		flag=1;
		if((r[i]==a && g[i-1]==b) || (r[i]==b && g[i-1]==a))
		{
			g[i-1]=c;
			g[i]='1';
			 }
			  else
			  {
                  if(a2[1]!=' ' && a2[0]!=' ')
                  {
				  for(k=i-1;k>=0;k--)
				  {
					  if((r[i]==a2[1] && g[k]==a2[0] ) || (r[i]==a2[0] && g[k]==a2[1]))
					  {
							  flag=0;
							  break;
							  }
                                  }
                                  }
									     if(flag==0)
									     {
										     for(k=0;k<=i;k++)
										     {
											     g[k]='1';
											     }
											      }
											      if(flag==1)
											      {
												      g[i]=r[i];
												      }
												           }
												            }
												            /* print */
												            int count=0;
												            char r1[30];
												            for(k=0;k<30;k++)
												            {
													            if(g[k]!='1')
													            {
														       r1[count]=g[k];
														       count++;
														       }
												}
												printf("Case ");
													printf("#");
												printf("%d",l);
											printf(":");
												printf(" ");
												printf("[");
												l++;
												for(i=0;i<count;i++)
												{
													char u=' ';
													char u1=',';
													if(i!=(count-1))
													{
													printf("%c%c%c",r1[i],u1,u);
													}
													if(i==(count-1))
													{
														printf("%c",r1[i]);
														}
														 }
														 printf("]");
														 cout<<endl;
														 }
													
                                                      }        
									 
								 return(0);
								 }
								 
						
	
	
