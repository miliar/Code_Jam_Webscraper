#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<map>
#include<string>
#include<vector>
using namespace std;
int l,d,n,sum;
char str[100000];
string res[20];
char a[5005][20];
int main()
{
	int i,j,count,k,f;
	FILE *in,*out;
	out=fopen("out.txt","w");
	in=fopen("ina.in","r");
	while(fscanf(in,"%d%d%d",&l,&d,&n)==3)
	{
		for(i=0;i<d;i++)
		{
            fscanf(in,"%s",a[i]);
		}
		count=0;
		for(i=0;i<n;i++)
		{
			fscanf(in,"%s",str);
			count++;
			sum=0;
			for(j=0;j<20;j++)
            {
                res[j]="";
            }
            int len=strlen(str),step=0;
            j=0;
            while(j<len)
            {
                if(str[j]=='(')
                {
                    for(k=j+1;k<len;k++)
                    {
                        if(str[k]==')')
                        {
                            j=k+1;
                            step++;
                            break;
                        }
                        else
                        {
                            res[step]+=str[k];
                        }
                    }
                }
                else
                {
                   res[step]+=str[j];
                   j++;
                   step++;
                }
            }
            for(j=0;j<d;j++)
            {
                bool flag=false;
                for(k=0;k<l;k++)
                {
                    bool flag1=false;
                    for(f=0;f<res[k].size();f++)
                    {
                        if(a[j][k]==res[k][f])
                        {
                            flag1=true;
                            break;
                        }
                    }
                    if(!flag1)
                    {
                        flag=true;
                        break;
                    }
                }
                if(!flag)
                {
                    sum++;
                }
            }
			fprintf(out,"Case #%d: %d\n",count,sum);
		}
	}
	return 0;
}
