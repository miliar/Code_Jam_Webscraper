#include<iostream>
#include<cstdio>
#include<vector>
#include<cstring>
#include<string>
#include<fstream>
typedef long long int ll;
using namespace std;
int main()
{
	char a[]="yhesocvxduiglbkrztnwjpfmaq";
	/*fstream myfile ("xyz.in");*/
	char filename[]="A-small-attempt2";
	char infile[32], outfile[32];
	
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	int t=0,l;
	fscanf(fp,"%d\n", &t);
	for(int j=1;j<=t;j++){
			char s[150];
		
			fgets(s,150,fp);
			
			 l = strlen(s);
		
        fprintf(ofp, "Case #%d: ", j);
		for(int i=0;i<l;i++)
		{
			if(s[i]>96 && s[i]<123)
			{
				//myfile<<a[s[i]-97];	
				fputc(a[s[i]-97],ofp);
			}
			else if(s[i]==32){
				//myfile<<" ";
				fputc(32,ofp);
			}
				
		}
		{fputc(10,ofp);}
		//myfile<<"\n";	



	}
	//system("pause");
	return 0;
}
