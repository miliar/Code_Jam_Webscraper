#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <algorithm>

#include <memory.h>

#define INPUT_FILE "C-small-attempt3.in"

using namespace std;

int gcd(int a,int b)
{
	// assume a>b
	while(b!=0)
	{
		a%=b;
		swap(a,b);
	}
	return a;
}

int main()
{
	FILE* fin=fopen(INPUT_FILE,"r");
	char output_file[1024];
	char log_file[1024];
	strcpy(output_file,INPUT_FILE);
	strcpy(strrchr(output_file,'.'),".out");
	strcpy(log_file,INPUT_FILE);
	strcpy(strrchr(log_file,'.'),".log");
	FILE* fout=fopen(output_file,"w");
	FILE* flog=fopen(log_file,"w");

	int num_cases;
	fscanf(fin,"%d",&num_cases);
	for(int k=0;k<num_cases;++k)
	{
		int num_tones,low,high;
		int tones[10000];
		fscanf(fin,"%d %d %d",&num_tones,&low,&high);
		for(int i=0;i<num_tones;++i) fscanf(fin,"%d",&tones[i]);

		sort(tones,tones+num_tones);
		
		printf("Case #%d: ",k+1);
		fprintf(fout,"Case #%d: ",k+1);

		bool tone_found=false;
		for(int i=low;i<=high;++i)
		{
			bool tone_ok=true;
			for(int j=0;j<num_tones;++j)
			{
				if(tones[j]%i!=0 && i%tones[j]!=0)
				{
					tone_ok=false;
					break;
				}
			}
			if(tone_ok)
			{
				printf("%d\n",i);
				fprintf(fout,"%d\n",i);
				tone_found=true;
				break;
			}
		}
		if(!tone_found)
		{
			printf("NO\n");
			fprintf(fout,"NO\n");
		}

/*		int lcm=1;
		bool tone_found=false;
		for(int i=0;;++i)
		{
			if(lcm>high) break;

			// lcm=LCM of tones[0]~tones[i-1]
			if(low<=lcm)
			{
//				if(i>0 && lcm==tones[i-1]) break;
//				if(i<num_tones && lcm==tones[i]) break;

				int top_gcd=0;
				for(int j=i;j<num_tones;++j)
				{
					top_gcd=gcd(top_gcd,tones[j]);
				}
				if(top_gcd%lcm==0)
				{
					printf("%d\n",lcm);
					fprintf(fout,"%d\n",lcm);
					tone_found=true;
					break;
				}
			}

			if(i==num_tones) break;
			int g=gcd(lcm,tones[i]);
			lcm=lcm*tones[i]/g;
		}
		if(!tone_found)
		{
			printf("NO\n");
			fprintf(fout,"NO\n");
		}*/
	}
	fclose(flog);
	fclose(fout);
	fclose(fin);
}
