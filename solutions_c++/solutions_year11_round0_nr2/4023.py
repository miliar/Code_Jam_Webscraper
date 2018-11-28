#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>

#define MAX 1000
#define MAX4 32800 	// Limits acc to the  problem .
#define MAX3 32800


#define SMALL
//#define LARGE


using namespace std;

int k=0 ;			// Output string lenght pointer . 


void reverse (char *s)
{
  char *t = s;
 
  while (*t != '\0') t++;
  while (s < t)
  {
    int c = *s;
    *s++ = *--t;
    *t = c;
  }
}

int check_invoke(char out[MAX4],char invoke[3])
{
		
					// invoke[2]=T invode[1]=F invoke[0]=Q

	char temp3[3]={ '\0'};
	strcpy(temp3,invoke);

	//printf("-%c-",temp);
	temp3[2]='\0';
	
	 char rev[2]={'\0' };
        strcpy(rev,temp3);
        reverse(rev);
        //printf("%s",rev);



	char temp2[3]={'\0'};
	int l=strlen(out);
	//printf("-%d-",l);
	temp2[0]=out[l-2];		// temp2 contains the last 2 characters from out .
	temp2[1]=out[l-1];
	temp2[2]='\0';

	//printf("%s-%s-%s\n",temp2,temp3,rev);
	if( !strcmp(temp2,temp3) || !strcmp(rev,temp2))
	{
		// Put temp into out[l-2] and replace out[l-1] with null.
		out[l-2]=invoke[2];
		out[l-1]='\0';
		//printf("%s-",out);
		temp3[2]=invoke[2];	
		temp3[3]='\0';
		return 1;
	}
	
	temp3[2]=invoke[2];
	temp3[3]='\0';

	return 0;
}
	
int check_oppose( char out[MAX4],char oppose[2])
{
	
	//printf("%s-",oppose);
	if( (strchr(out,oppose[0])!=NULL) && (strchr(out,oppose[1]) !=NULL ))
		return 1;
	
	return 0;
}


int main()
{

	#ifdef SMALL
		freopen("B-small-attempt0.in","rt",stdin);
    		freopen("out.txt","wt",stdout);
	#endif

	#ifdef LARGE
		freopen("","rt",stdin);
     	        freopen("large_out.txt","wt",stdout);
	#endif

	

	

	int count=1;
	int t;

	cin>>t;

	while(count <= t)
	{
		fflush(stdin);	
		k=0;
		char out[MAX4]={ '\0' };	
		char invoke[MAX][3]={'\0'};
		char oppose[MAX][2]={'\0'};
		char in[MAX3];

		int invoke_c,oppose_c;
		
		cin>>invoke_c;
		
		for(int i=0;i<invoke_c;i++)
			scanf("%s",invoke[i]);
		fflush(stdin);	
		
		cin>>oppose_c;
		for(int i=0;i<oppose_c;i++)
			scanf("%s",oppose[i]);
		
		fflush(stdin);

		int N;

		cin>>N;
		scanf("%s",in);
		
		fflush(stdin);
	
		for(int i=0;i<N;i++)
		{
			
			out[k++]=in[i];			// enter in the out string.
			out[k]='\0';
			//printf("-%s-",out);
			// Check with invoke . 

			if(strlen(out) >= 2 )
			{
				//printf("INSIDE\n");
				for(int i=0;i<invoke_c;i++)
				{
					if(check_invoke(out,invoke[i])) 		// Done with the invoke stuff .
					{
						k=k-1;
						break;
					}
				}
				
				//Checking for opposing strings . 
				for(int i=0;i<oppose_c;i++)
				{
					if(check_oppose(out,oppose[i]))
   					{
						k=0;
						//strcpy(out,"");
						break;
					}
				
				}
			}
		} // End of for 
		out[k]='\0';
		printf("Case #%d: [",count);
		for(int i=0;i<k-1;i++)
			printf("%c, ",out[i]);
		if(isalpha(out[k-1]))
			printf("%c]\n",out[k-1]);
		else
			printf("]\n");
		count++;
		
	}//end while 						
				

	

	return 0;
}
