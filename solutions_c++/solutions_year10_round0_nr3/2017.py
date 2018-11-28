#include<stdio.h>
#include<iostream>
#include<string.h>

using namespace std;

// Global Variables
unsigned long long int r, k, sum, tot, ans, a[1000], b[1000];
int n;

int main()
{
    // File Handling
    char filename[32];
	char infile[32]="C-large.in";
	FILE *fp=fopen(infile, "r");
    
    // Local Variables
    int cases, tc, i, j, p, pos[1000];
    
    // Engine
    fscanf(fp, "%d", &cases);
	for(tc=1;tc<=cases;tc++)
	{
        p=0; sum=0; ans=0, tot=0;
        fscanf(fp, "%d%d%d", &r, &k, &n);
        for (i=0;i<n;i++) { fscanf(fp, "%d", &a[i]); tot+=a[i]; }
        j=0;
        if (tot>k)
        {
            for (i=0;i<n;i++) 
            {
                b[i]=0;
                for (j=i;b[i]<=k;j++)
                    {
                        j%=n;
                        b[i]+=a[j];
                    }
                b[i]-=a[--j];
                pos[i]=j;
            }                 
             
            ans=0; j=0; 
            for(i=0; i<r; i++) 
            { 
                ans+=b[j];
                j=pos[j];
            }
        }
        else ans=tot*r;
       	cout<<"Case #"<<tc<<": "<<ans<<endl;
     }
 return 0;
}
