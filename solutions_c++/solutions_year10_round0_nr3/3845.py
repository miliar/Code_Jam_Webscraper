#include<stdio.h>
#include<iostream.h>
#include<memory.h>
#include<string.h>
int r,k,n,tc;
int testCase,ride,i,tmp,hold,pos,tmppos;
double sum,totp,cost;

int pg[1000];
int main()
{
	char filename[32];
	char infile[32], outfile[32];
	//char *ch;
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	fscanf(fp, "%d", &tc);
	//char* ch = "%d%d%d";
	//fscanf(fp,"%d%d%d" , &r, &k, &n);
	//cout<<r<<" "<<k<<" "<<n<<" "<<tc;
	//double j = 100000000000000000;
	//cout<<;
	for(testCase=1;testCase<=tc;testCase++) // number of testcases
	{
		fscanf(fp,"%d%d%d" , &r, &k, &n);
		for(i=0;i<n;i++)	
		{
			fscanf(fp, "%d",&tmp);
			pg[i]=tmp;
			//if(testCase==2)cout<<pg[i]<<" "; 
		}
		//do the initializing
		ride = 1; pos = 0; totp =0; sum = 0; cost = 0; hold =-1;
		//initialized for each tc
		while(ride<=r)
		{
			sum = pg[pos]; hold =-1;
			tmppos=pos;//no checking as per limit gi = k
			while (sum <=k && pos!=hold) 
			{
				hold = tmppos;
				//cout<<pos<<"\n";
				if(pos==(n-1))
					pos = 0;
				else
					pos++;
				totp=sum;
				//cout<<totp<<" -"<<pos<<"\n";
				sum = sum + pg[pos];				
			}//one ride per tc
			cost = cost+ totp;
			ride ++;
		}//all rides per tc
		fprintf(ofp, "Case #%d: %g\n", testCase, cost);
	}//end of tc for-loop

return 0;
}