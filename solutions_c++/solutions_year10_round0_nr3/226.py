#include<stdio.h>
#include<memory.h>

long long num[1010];
int n,t;
long long r,val,key;
long long f[1010];
int st[1010],a,b;
int main(){
	freopen("C-large.in","r",stdin);
	
	freopen("Cin.txt","w",stdout);
    scanf("%d",&t);
   // printf("%d\n",t);
    int ccount = 0;
	while(t--){
	     scanf("%I64d %I64d %d",&r,&val,&n);
	    // printf("%I64d %I64d %d\n",r,val,n);
	     for(int i=0;i<n;i++)
	         scanf("%I64d",&num[i]);
	    // for(int i=0;i<n;i++)
	   //      printf("%I64d ",num[i]);
	   //  printf("\n");
	     int now = 0;
	     //memset(f,0,sizeof(f));
	     for(int i=1;i<=n+1;i++)
	        f[i] = 0;
		 for(int i=1;i<=n+1;i++){
		     st[i] = now;
		    
			 long long cccount = num[now];
			 int p = 1;
			 now = (now + 1)%n;
			 while(cccount + num[now]<=val&&p<n){
			      cccount += num[now];
			      now  =  (now + 1)%n;
			      p++;
			 }
			 f[i] = cccount;
		 }
	/*	 for(int i=1;i<=n+1;i++)
		    printf("%I64d ",f[i]);
		 printf("\n");
		 for(int i=1;i<=n+1;i++)
		    printf("%d ",st[i]);
		 printf("\n");
		*/
		 for(int i=1;i<=n+1;i++){
		     int found =  0;
			 for(int j=1;j<i;j++){
			      if(st[i]==st[j]){
				      b = i;
				      a = j;
				      found   =  1;
				      break;
				  }
			 }
			 if(found == 1)
			     break;
		 }
		// printf("a: %d   b: %d\n",a,b);
		 key = b-a;
		 long long ave = 0;
		 for(int i=a;i<=b-1;i++)
		    ave += f[i];
		 
		 long long ans = 0;
		 for(int i=1;i<a;i++)
		    ans += f[i];
	//	 printf("ans : %I64d \n",ans);
		 r -= (a-1);
		 ans += (r/key)*ave;
	//	 printf("ans : %I64d \n",ans);
		 long long mod  = r%key;
		 //if(r>b)
	//	 printf("mod : %I64d\n",mod);
		 for(int i=1;i<=mod;i++){
		    // printf("%d ",a  + i);
			 ans += f[a-1  + i];
		 }
	//	 printf("ans : %I64d \n",ans);
	//	 printf("\n");
		 printf("Case #%d: %I64d\n",++ccount,ans);
	}
//	while(1);
	return 0;
}
