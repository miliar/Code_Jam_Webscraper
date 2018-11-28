#include<stdio.h>
#include<iostream.h>
//#include<string.h>

void main()
{       FILE *fw,*fr;
	char r[100],p[100];
	int t,n,i,j,pos_o=1,pos_b=1,ans=0,l_o=0,l_b=0;
	

	fr = fopen("d:/a.txt.in","rb");
	fscanf(fr,"%d",&t);
	fw=fopen("d:/a1.txt","w+");

	for(i=0;i<t;i++)
	{
		fscanf(fr,"%d", &n);
		fflush(stdin);
		pos_o=1;
		pos_b=1;
		ans=0;
		l_o=0;
		l_b=0;
		for(j=0;j<n;j++)
		{
			fflush(stdin);
				do{
					fscanf(fr,"%c",&r[j]);
				}while(r[j]==' ');
			fflush(stdin);
			fscanf(fr,"%d",&p[j]);
			fflush(stdin);
			
		}
		int k,z=0,y=0,b1=1,o1=1;
		for(k=0;k<n;k++)
		{ //printf("\nj==%d",j);

			if(r[k]=='O')
			{z++;
				if(p[k]<pos_o)
				{ int t;
				t=pos_o;
				pos_o=p[k];
				p[k]=t;

				if(y>1)
					{l_b=b1-1;
					}

					else if(z>1)
					{l_b=0;
					}

					y=0;
					l_o=p[k]-pos_o+1;
				
					if(l_o>l_b)
						{
								l_o=l_o-l_b;
								//pos_o=p[k];
							//	printf("\nl_o=%d",l_o);
								//fprintf(fw,"\npos_0=%d\n",pos_o);
						}
					
					else
						{		//pos_o=p[k];
								l_o=1;
							//	printf("\nl_o=%d",l_o);
								//fprintf(fw,"\npos_0=%d\n",pos_o);
						}
					if(z>0)
					{o1=o1+l_o;
					}
				}
				else
				{
				
				
					if(y>1)
					{l_b=b1-1;
					}

					else if(z>1)
					{l_b=0;
					}

					y=0;
					l_o=p[k]-pos_o+1;
				
					if(l_o>l_b)
						{
								l_o=l_o-l_b;
								pos_o=p[k];
							//	printf("\nl_o=%d",l_o);
								//fprintf(fw,"\npos_0=%d\n",pos_o);
						}
					
					else
						{		pos_o=p[k];
								l_o=1;
							//	printf("\nl_o=%d",l_o);
								//fprintf(fw,"\npos_0=%d\n",pos_o);
						}
					if(z>0)
					{o1=o1+l_o;
					}
				}
				ans=ans+l_o;
				//fprintf(fw,"ans_0=%d",ans);


			}

			else if(r[k]=='B')
			{	y++;
				if(p[k]<pos_b)
					{ int t;
					t=pos_b;
					pos_b=p[k];
					p[k]=t;


					if(z>1)
					{l_o=o1-1;
					}
				
					else if(y>1)
					{	
						l_o=0;
					}	
					z=0;
	
					l_b=p[k]-pos_b+1;

					if(l_b>l_o)
					{	l_b=l_b-l_o;
					//	printf("\nl_b=%d",l_b);
					//pos_b=p[k];
					//fprintf(fw,"\npos_b=%d\n",pos_b);
					}
					else
					{	//pos_b=p[k];
						l_b=1;
					//	printf("\nl_b=%d",l_b);
						//fprintf(fw,"\npos_b=%d\n",pos_b);
					}	
				
					if(y>0)
					{b1=b1+l_b;
					}
					}
			
				else
				{
					if(z>1)
					{l_o=o1-1;
					}
				
					else if(y>1)
					{	
						l_o=0;
					}	
					z=0;
	
					l_b=p[k]-pos_b+1;

					if(l_b>l_o)
					{	l_b=l_b-l_o;
					//	printf("\nl_b=%d",l_b);
					pos_b=p[k];
					//fprintf(fw,"\npos_b=%d\n",pos_b);
					}
					else
					{	pos_b=p[k];
						l_b=1;
					//	printf("\nl_b=%d",l_b);
					//fprintf(fw,"\npos_b=%d\n",pos_b);
					}	
				
					if(y>0)
					{b1=b1+l_b;
					}
				}
				ans+=l_b;
				//fprintf(fw,"ans_b=%d",ans);

			}
			
		}
		fprintf(fw,"Case #%d: %d\n",i+1,ans);
		printf("\nCase #%d: %d",i+1,ans);
		


	}


}