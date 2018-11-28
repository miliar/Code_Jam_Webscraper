# include<iostream>
# include<fstream>
# include<string>
# include<vector>
# include<algorithm>
# include<iomanip>

using namespace std;


main()
{
FILE *fp,*fp1;
fp=fopen("A-small.in.txt","r");
if(fp==NULL)
puts("cannot open file");

int i,f,j,k,tc;
long long int n,A,B,C,D,cx,cy,x0,y0,M,tr[1001]={0},X[100001],Y[100001];
fscanf(fp,"%d",&tc);

for(f=1;f<=tc;f++)
      {
	
	fscanf(fp,"%lld %lld %lld %lld %lld %lld %lld %lld",&n,&A,&B,&C,&D,&x0,&y0,&M);
	X[0] = x0; Y[0] = y0;
	for(i=1;i<n;i++){
  	X[i] = (A * X[i-1] + B)%M;
  	Y[i] = (C * Y[i-1] + D)%M;}
  	for(i=0;i<n;i++)
		{
		for(j=i+1;j<n;j++)
			{
			for(k=j+1;k<n;k++)
				{
				cx=(X[i]+X[j]+X[k])%3;
				cy=(Y[i]+Y[j]+Y[k])%3;
				if((cx==0)&&(cy==0))
				tr[f]++;
				}
			}
		}
	
	}

fp1=fopen("output.txt","w");
for(i=1;i<=tc;i++)
	{
	printf("\nCase #%d: %lld",i,tr[i]);
	fprintf(fp1,"Case #%d: %lld\n",i,tr[i]);
	}
fclose(fp1);
}
