#include<cstdio>
#include<cstdlib>

int ans[]={0,5,27,143,751,935,607,903,991,335,47,943,471,55,447,463,991,95,607,263,151,855,527,743,351,135,407,903,791,135,647};

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int T;
	scanf("%d",&T);
	

	for(int t=1;t<=T;t++){
		int n;
		scanf("%d",&n);
		
		printf("Case #%d: %03d\n",t,ans[n]);
	}
	
	
   // system("PAUSE");
    //return EXIT_SUCCESS;
    return 0;
}
