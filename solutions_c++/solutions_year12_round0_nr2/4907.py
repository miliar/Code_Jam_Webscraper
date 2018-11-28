#include<iostream>
#include<cstdio>
#include<vector>
#include<cstring>
#include<algorithm>
typedef long long int ll;
using namespace std;
int main()
{
	int p[35][3];
	p[0][0]=0;p[0][1]=0;p[0][2]=0;
	p[1][0]=0;p[1][1]=0;p[1][2]=1;
	p[30][0]=10;p[30][1]=10;p[30][2]=10;
	p[29][0]=9;p[29][1]=10;p[29][2]=10;
	p[28][0]=9;p[28][1]=9;p[28][2]=10;
	for(int i=2;i<28;i++)
	{
		int z=i/3;
		if(i%3==0){
			p[i][0]=z-1;
			p[i][1]=z;
			p[i][2]=z+1;
		}else 	if(i%3==1){
			p[i][0]=z-1;
			p[i][1]=z+1;
			p[i][2]=z+1;
		}else 	if(i%3==2){
			p[i][0]=z;
			p[i][1]=z;
			p[i][2]=z+2;
		}
		//cout<<p[i][0]<<" "<<p[i][1]<<" "<<p[i][2]<<endl;
	}	
	char filename[]="B-small-attempt1";
	char infile[32], outfile[32];
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int t=0,n,s,px;
	fscanf(fp, "%d", &t);
	for(int j=0;j<t;j++){
		vector <int> x;
		 fscanf(fp, "%d %d %d ", &n, &s,&px);
		for(int i=0;i<n;i++)
		{
			int asd;
			fscanf(fp, "%d ", &asd);
			x.push_back(asd);
		}
		sort(x.begin(),x.end());
		int count=0;
		for(int i=0;i<n;i++)
		{
			int z=x[i];
			int a,b,c;
			a=p[z][0] ;
			b=p[z][1] ; 
			c=p[z][2] ;
			if(z>27){
				count++;
				continue;
			}
			if(s==0)
			{
				if((c-1)>=px || b>=px)
				{
					count++;
				}


			}else{
				if(c>=px){
					count++;
					s--;
				}
			}

		}

		fprintf(ofp, "Case #%d: %d\n", j+1,count);
	}
	//system("pause");
	return 0;
}
