
#include<stdio.h> 
#include<math.h> 
#include<string.h> 
#include<stdlib.h> 
#include<iostream>
#include<map>

using namespace std;

map<string,int> m;


int main() 
{ 
	int n,s,q,ans,sum;
	bool u[102];
	char t[120],last[120];
	int ri=1;
	scanf("%d",&n);
	while(n--){
		m.clear();
		scanf("%d",&s);
		gets(t);
	//	printf("%d\n",s);
		for (int i=0;i<s;++i)
		{
			gets(t);
		//	puts(t);
			string str(t);
			m.insert(make_pair(str,i));
		}
		scanf("%d",&q);
		gets(t);
		memset(u,0,sizeof(u));
		ans=0;
		sum=0;
	//	printf("%d\n",q);
		strcpy(last,"");
		while(q--)
		{
			gets(t);
		//	puts(t);
			if (strcmp(last,t)==0)
				continue;
			strcpy(last,t);

			string str(t);
			int i=m.find(str)->second;
			
			if (u[i]==0)
				{
					u[i]=1;
					sum+=1;
					if (sum==s)
						{
					//	printf("change\n");
							ans++;
							sum=1;
							for (int j=0;j<s;++j)
								u[j]=0;
							u[i]=1;
					}
				}
		//	printf("sum=%d\n",sum);
			}
		
		printf("Case #%d: %d\n",ri++,ans);
		}
	
			
								
			
	

//	system("PAUSE");
	return 0;
	
} 


