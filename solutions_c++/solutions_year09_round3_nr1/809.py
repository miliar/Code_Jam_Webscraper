#include<stdio.h>
#include<algorithm>
#include<string.h>

using namespace std;

int main()
{
	int i,j,k,slen;
	int T,n;
	char s[70];
	long long sol[70];
	long long Ans,B;

	scanf("%d", &T);
	for(n=0;n<T;n++)
	{
		scanf("%s", s);
		slen=strlen(s);
//		printf("%s  %d\n", s,slen);

		for(i=0;i<slen;i++)
			sol[i]=-1;

		for(i=0,k=1;i<slen;i++)
		{
			if(sol[i]==-1){

				sol[i]=k;
				for(j=i+1;j<slen;j++)
				{
					if(s[i]==s[j]){
						sol[j]=k;
					}
				}
				if(k==1)
					k=0;
				else if(k==0)
					k=2;
				else 
					k++;
			}
			
		}
		if(k==0) k=2;

		for(i=0;i<slen;i++){
			s[i]=sol[i]+'0';
		}
		s[i]='\0';
//		printf("%s\n", s);

		B=1;
		Ans=0;
		for(i=slen-1;i>=0;i--)
		{
			Ans+=sol[i]*B;
			B*=k;
		}

		printf("Case #%d: %lld\n", n+1, Ans);

	}


	return 0;
}