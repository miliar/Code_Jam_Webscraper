#include<stdio.h>
#include<string.h>

struct dirnode {
	char name[101];
	char parent[100]; }directory [6000];
int complete, size,directorycount, mkdircount,newdirectories, totaldirs,i,j,k,l,m,n;
char directoryline[101], parentdir[101],currentdir[101];
int exists(char dir[],char parent[])
{

	int aux;

//	printf("Exists? %s - %s\n",dir, parent);
	for (aux=0;aux<totaldirs;aux++)
	{
		if ((strcmp(dir,directory[aux].name)==0)&&(strcmp(parent,directory[aux].parent)==0))
		{
			return 1;
		}
	}
	
	return 0;
}

int add(char dir[],char parent[])
{
//	printf("Add? %s - %s\n",dir, parent);
	strcpy(directory[totaldirs].parent,parent);
	strcpy(directory[totaldirs].name,dir);
	totaldirs++;
	return 1;
}


void main()
{
int cases, index_cases;

//freopen("A-small-attempt0.in" , "rt" , stdin ) ;
//freopen("A-small-attempt0.out" , "wt" , stdout ) ;
freopen("A-large.in" , "rt" , stdin ) ;
freopen("A-large.out" , "wt" , stdout ) ;

cases = 0;
//read the number of test cases 
scanf("%d",&cases);
//printf("Cases = %d\n",cases);


//Loop through all the cases
for (index_cases=0 ; index_cases<cases; index_cases++)
{
	//read the number of existing directories
	scanf("%d",&directorycount);
//	printf("N directories=%d\n",directorycount);
	 //read the new dirs
	scanf("%d",&newdirectories);
//	printf("New =%d\n",newdirectories);
	mkdircount = 0;
	totaldirs = 0;
	//loop through directories
	for(i=0;i<directorycount;i++)
	{
		// read directory
		scanf("%s",&directoryline);
//		printf("Line = %s - %d\n",directoryline,strlen(directoryline));
		// parse directory
		size = strlen(directoryline);
		parentdir[0]='/';
		parentdir[1]=0;
		for (l=1,j=1;j<size;)
		{
			
			for(k=0,complete=0;(j<size)&&(complete==0);k++,j++)
			{
				if(directoryline[j]!='/')
				{
					currentdir[k]=directoryline[j];
				}
				else
				{
					currentdir[k] = 0;
					complete =1;
					//check if exits
					if (!exists(currentdir,parentdir))
					{
						//add it if not
						add(currentdir,parentdir);
					}
					if (l>1)
					{
						parentdir[l] = '/';
						l++;
					}
					for(m=0; m<k ;l++,m++)
					{
						parentdir[l]=currentdir[m];
					}
					parentdir[l] = 0;
				}
			}
			if (complete==0)
			{
				currentdir[k]=0;
				if (!exists(currentdir,parentdir))
				{
					//add it if not
					add(currentdir,parentdir);
				}
			}
		}
	}
// create directories
	//read directory
	//parse directory counting how many created
	for(i=0;i<newdirectories;i++)
	{
		// read directory
		scanf("%s",&directoryline);
//		printf("Line = %s\n",&directoryline);
		// parse directory
		size = strlen(directoryline);
		parentdir[0]='/';
		parentdir[1]=0;
		for (l=1,j=1;j<size;)
		{
			
			for(k=0,complete=0;(j<size)&&(complete==0);k++,j++)
			{
				if(directoryline[j]!='/')
				{
					currentdir[k]=directoryline[j];
				}
				else
				{
					currentdir[k] = 0;
					complete =1;
					//check if exits
	//				printf("%s - %s\n",currentdir, parentdir);
					if (!exists(currentdir,parentdir))
					{
						//add it if not
						add(currentdir,parentdir);
						mkdircount++;
					}
					if (l>1)
					{
						parentdir[l] = '/';
						l++;
					}
					for(m=0; m<k ;l++,m++)
					{
						parentdir[l]=currentdir[m];
					}
					parentdir[l] = 0;
				}
			}
			if (complete==0)
			{
				currentdir[k] = 0;
//				printf("%s - %s\n",currentdir, parentdir);

				if (!exists(currentdir,parentdir))
				{
					//add it if not
					add(currentdir,parentdir);
					mkdircount++;
				}
			}
		}
	}
//	printf("Inicio\n");
//	for (n=0;n<totaldirs;n++)
//	{
//		printf("%s %s\n",directory[n].parent, directory[n].name);
//	}





	printf("Case #%d: %d\n",index_cases+1, mkdircount );
}
fclose(stdin) ;
fclose(stdout) ;

}