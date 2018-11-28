#include <iostream>
#include <cstdio>

using namespace std;
int a[100001];
int n,l,h;


void work(){
     scanf("%d%d%d",&n,&l,&h);
     memset(a,0,sizeof a);
     for (int i=1;i<=n;i++)
         scanf("%d",&a[i]);
         
     /*int check=1;    
     for (int i=1;i<=n;i++)
         for (int j=1;j<=n;j++)
             if (a[i]%a[j]!=0 && a[j]%a[i]!=0)
                {check=0;printf("%d %d\n",a[i],a[j]);}*/
     //printf("%d\n",check);       
     for (int i=l;i<=h;i++){
         int c=1;
         for (int j=1;j<=n;j++)
             if (i%a[j]!=0 && a[j]%i!=0)
                {c=0;break;}
         if (c)
            {printf("%d\n",i);return;}
     }
     printf("NO\n");
     return;
}

int main(){
	freopen("B.out","w",stdout);
	int t;
    cin >> t;
	for (int i=1;i<=t;i++){
		cout << "Case #"<< i << ": ";
		work();
	}
	//system("pause");
	return 0;
}
/*
Simple Input:
 
*/
