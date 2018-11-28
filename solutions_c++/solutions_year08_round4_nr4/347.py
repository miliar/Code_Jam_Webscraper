#include<string>
#include<algorithm>
using namespace std;
int go()
{ 
	char m[1010],ind[6]={1,2,3,4,5,6},m2[1010];
   int h,n,i,k,l,j,min,tot;
   scanf("%d",&n);
   for(h=1;h<=n;h++)
   {
       scanf("%d",&k);
       scanf("%s",m);
       l = strlen(m);
       min=2000000;
       do{
            for(j=0;j<l/k;j++){
            for(i=0;i<k;i++)
            {
                m2[i+j*k]=m[(ind[i]-1)+j*k];
            }
        	}
        	tot=1;
           for(i=1;i<l;i++)
           {
               if(m2[i]!=m2[i-1])tot++;
           }
           if(tot<min)min=tot;
       }while(next_permutation(ind, ind+k));
        printf("Case #%d: %d\n",h,min); 
	}
	return 0; 
}
int main(){
   
   freopen("D-small-attempt0.in", "r", stdin); 
	freopen("ans.txt", "w", stdout); 
	go(); 
	return 0; 
}
