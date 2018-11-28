#include<iostream>
using namespace std;
int main()
{
	int t,total;
	char ch;

	FILE * fp,*fp1;
	fp=fopen("B-small-attempt1.in","r");
	fp1=fopen("B-Output-attempt1.txt","w");
	fscanf(fp,"%d",&t);
	
	total=t;
	
	while(t--)
	{
		
		fscanf(fp,"%c",&ch);
		int com,opp,n,i=0,k=0,j;
		fscanf(fp,"%d",&com);
		fscanf(fp,"%c",&ch);
		char * c=new char[3*com];
		for(i=0;i<3*com;i++)
			fscanf(fp,"%c",&c[i]);

		fscanf(fp,"%d",&opp);
		fscanf(fp,"%c",&ch);
		char * o = new char[2*opp];
		for(i=0;i<2*opp;i++)
			fscanf(fp,"%c",&o[i]);

		fscanf(fp,"%d",&n);
		fscanf(fp,"%c",&ch);
		char *a=new char[n];
		for(i=0;i<n;i++)
			fscanf(fp,"%c",&a[i]);

		cout<<c<<endl;
		cout<<o<<endl;
		cout<<a<<endl;
		
		char * res = new char[n];
			i=0;
		res[k]=a[i];
		for(i=1;i<n;i++)
		{
			res[++k]=a[i];

			if(com==1)
			{
				if((res[k]==c[0]&&res[k-1]==c[1])||(res[k]==c[1]&&res[k-1]==c[0]))
				{
					res[--k]=c[2];
					
					
				}
			}

			if(opp==1)
			{
				if(res[k]==o[0])
				{
					for(j=k-1;j>=0;j--)
						{
							if(res[j]==o[1])
							{
								k=-1;
								
							}
						}


				}
				if(res[k]==o[1])
				{
					for(j=k-1;j>=0;j--)
						{
							if(res[j]==o[0])
							{
								k=-1;
								
							}
						}


				}
			}

			
			
			
				
			
		}

		


		fprintf(fp1,"Case  #%d: [",total-t);
if(k!=-1)
fprintf(fp1,"%c",res[0]);
		for(i=1;i<=k;i++)
			fprintf(fp1,", %c",res[i]);
		fprintf(fp1,"]\n");

	}
	fclose(fp);
	fclose(fp1);

}