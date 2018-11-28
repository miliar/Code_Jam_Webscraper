#include<iostream>
#include<cstdio>
#include<vector>
#include<cstring>
#include<memory.h>
typedef long long int ll;
using namespace std;
int main()
{
    int a[1004];
    for(int i=1;i<1004;i++)
    {
         char buff[45],c[45];
         itoa(i,buff,10);
         int l = strlen(buff);
		 for(int j=0;j<l;j++)
		 {
		     c[((j-1)+l)%l]=buff[j];
 		}  
            c[l]='\0';
           //cout<<buff<<"  "<<c<<endl;
            a[i]=atoi(c);
           // cout<<a[i]<<endl;
    }
    char filename[]="C-small-attempt0";
	char infile[32], outfile[32];
    strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
    FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
    
  int t=0,n,m;
  fscanf(fp, "%d", &t);
  //cin>>t;
  for(int j=0;j<t;j++){
          fscanf(fp, "%d %d", &m, &n);
          int count=0;
        for(int i=m;i<=n;i++)
		{
		    if(a[i]!=i && a[i]>=m && a[i]<=n )
		    {
		    	if(i>a[i])
		    	{
		    	  if(i!=a[a[i]])
		    	   count++;
	    		}
	    		else
    			count++;
    		}
		} 
	//	cout<<count<<endl;
		fprintf(ofp, "Case #%d: %d\n", j+1,count);


  }
  //system("pause");
return 0;
}
