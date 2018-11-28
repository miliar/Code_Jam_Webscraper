//written on C++ (compatible with DevC++ / MS Visual C++ 6)
#include<stdio.h>

int main()
{
	char aa[15][27],dict[5000][16],word[500];
	int a[15],a0[15],ap[15],d,i,j,k,kk,l,n,n1,ok,ok1;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d %d %d\n",&l,&d,&n);
	for(i=0;i<d;i++)scanf("%s",&dict[i]);
	for(i=1;i<=n;i++)
	{
		scanf("%s",&word);
		for(j=0;j<l;j++)
		{
			a[j]=0;ap[j]=0;
			if(!j)a0[j]=0;
			if(j)a0[j]=a0[j-1]+(2*ap[j-1])+a[j-1];
			if(word[a0[j]]!='('){a[j]=1;aa[j][0]=word[a0[j]];aa[j][1]=0;}
			if(word[a0[j]]=='(')
			{
				k=a0[j]+1;ap[j]=1;
				while(word[k]!=')'){aa[j][a[j]]=word[k];a[j]++;k++;}
				aa[j][a[j]]=0;
			}
		}
		n1=0;
		for(j=0;j<d;j++)
		{
			ok=1;
			for(k=0;k<l;k++)
			{
				ok1=0;
				for(kk=0;kk<a[k];kk++){if(dict[j][k]==aa[k][kk]){ok1=1;break;}}
				if(!ok1){ok=0;break;}
			}
			if(ok)n1++;
		}
		printf("Case #%d: %d\n",i,n1);
	}
	return 0;
}