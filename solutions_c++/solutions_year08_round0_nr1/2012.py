#include<iostream.h>
#include<stdio.h>
#include<conio.h>
#include<string.h>
#define SEARCH_MAX 10
#define QUERY_MAX 100

int switches;  // number of switches required
int change;


struct
	{
		char sr[50];
		int flag;
	}srch[SEARCH_MAX];

	char query[QUERY_MAX][50];	//srch - name of search engines
										//query - name of queries


void initialize()          //to initialize flag to 0
{
  for(int i=0;i<SEARCH_MAX;i++)
		srch[i].flag=0;
}

void main()
{
	int i,j,n;  //n - no of test cases

	int s=0,q=0;     //s - no of search engines
					 //q - no of queries




	FILE *fp,*fp1;

	clrscr();
	fp = fopen("search.txt","r");
	fp1 = fopen("search_out.txt","w");
	fscanf(fp,"%d",&n);  //reading the no of test cases
	cout<<"n:  "<<n<<"\n";

	for(j=1;j<=n;j++)
	{
		fscanf(fp,"%d",&s);
		cout<<"no of search engines:  "<<s<<endl;
		fgets(srch[0].sr,50,fp);
		for(i=0;i<s;i++)
		{
			//istream::getline(fp,srch[i].sr,'\n');
			fgets(srch[i].sr,50,fp);
		  //fscanf(fp,"%s",srch[i].sr);
			cout<<"#"<<i<<" "<<srch[i].sr<<"\n";
		}
		initialize();

		fscanf(fp,"%d",&q);
		cout<<"no of queries:  "<<q<<"\n";
      fgets(query[0],50,fp);
		for(i=0;i<q;i++)
		{
			//istream::getline(fp,query[i]);
			//fscanf(fp,"%s",query[i]);
			fgets(query[i],50,fp);
			cout<<"#"<<i<<" "<<query[i]<<"\n";

			for(int k=0;k<s;k++)
			{
				if(!(strcmp(query[i],srch[k].sr)))
				{
					if(!(srch[k].flag))
					{
						srch[k].flag=1;
						change++;
					}

					if(change==s)
					{
						switches++;
						initialize();
						change =1;

						srch[k].flag=1 ;
					}
				}
			}
		}
  cout<<"\nNumber of switches required:  "<<switches<<endl;
  fprintf(fp1,"Case #%d: %d\n",j,switches);
  switches=0;
  change = 0;
  }

}

