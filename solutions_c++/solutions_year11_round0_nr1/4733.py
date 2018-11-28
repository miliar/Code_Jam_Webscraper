#include <cstdlib>
#include <cstdio>
#include <cmath>




int main(int argc, char *argv[])
{      
							int st[101][2];

int jg[101],jgu=0;
					
	int t,n;
	char c;
	FILE *pp;  
			pp=fopen("A-large.in","rb");		   
		fscanf (pp, "%d", &t);
	while(t--)
	{
	fscanf (pp,"%d", &n);
	  for(int i=0;i<n;i++)
	  {
				fscanf (pp, " %c ", &c);
				if(c=='B')
				st[i][0]=0;
				else
				st[i][0]=1;
				fscanf (pp, "%d", &st[i][1]);
				} 
				int sum=0,bljia=0,oljia=0;
				int p[2][1]={{1},{1}};
				for(int i=0;i<n;i++)
				{
					
					if(st[i][0]==0)
					{
						int l=abs(p[0][0]-st[i][1])+1;  
								if(l>oljia)
								{
									bljia=bljia+l-oljia;						                 
									sum=sum+l-oljia;
									 oljia=0;  
									}
								else
								{
									
									 oljia=0;
									 bljia++;
									sum++;
									}							
								p[0][0]=st[i][1];	
								
								}	
						else
						{
							int l=abs(p[1][0]-st[i][1])+1;
				if(l>bljia)
								{
									oljia=oljia+l-bljia;				         
									sum=sum+l-bljia; 
									 bljia=0;
									}
								else
								{
									
									bljia=0;
									oljia++;
									sum++;
									}									
								p[1][0]=st[i][1];	
							}
						
					}
	  jg[jgu++]=sum;   
	
	}
	fclose(pp);
	 FILE *pl;
			pl=fopen("A-large.out","wb");
	   
	   for(int i=0;i<jgu;i++)
	   {                  
					fprintf(pl,"Case #%d: %d\n",i+1,jg[i]);
					
					}
	   fclose(pl);         
				 
      
}
