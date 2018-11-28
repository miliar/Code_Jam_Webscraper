#include<stdio.h>
int main(){
	int t,k;
	scanf("%d",&t);
	for(k=0;k<t;k++){
		int c,d,n,i,cc,oc,j,fn,on;
		char co[220],opp[150],ele[110],f[110],cv,o[110],cf;
		scanf("%d",&c);
		cc=0;
		for(i=0;i<c;i++){
			scanf(" %c%c%c",&co[cc],&co[cc+1],&co[cc+2]);
			cc+=3;
			co[cc++]=co[cc-2];
			co[cc++]=co[cc-4];
			co[cc++]=co[cc-3];
		}
		scanf("%d",&d);
		oc=0;
		for(i=0;i<d;i++){
			scanf(" %c%c",&opp[oc],&opp[oc+1]);
			oc+=2;
			opp[oc++]=opp[oc-1];
			opp[oc++]=opp[oc-3];
		}
		/* printf("co %d c=%d\n",cc,c);
		 for(i=0;i<cc;i++)
		                  printf("%c ",co[i]);
	                    printf("opp %d d=%d\n",oc,d);
                     for(i=0;i<oc;i++)
                                      printf("%c ",opp[i]);*/

		scanf("%d ",&n);
        fn=0;on=0;cv=' ';cf=' ';
        int lastOpp=0;
		for(i=0;i<n;i++){
			scanf("%c",&ele[i]);
			f[fn++]=ele[i];
                        /* for(int l=0;l<=i;l++){
                                 printf("ele[%d]= %c",l,ele[l]);
                                 }
                         for(int q=0;q<fn;q++)
                         printf("  f[%d]= %c \n",q,f[q]);*/
			//if(fn>1){
			if(ele[i]==cv){
				fn-=2;
				f[fn++]=cf;
				if(lastOpp==1)     on--;
                cv=' ';cf=' ';
			}
			else{ 
                cv=' ';cf=' ';
				for(j=0;j<on;j++){
					if(ele[i]==o[j]){
						fn=0;
						on=0;
						break;
					//	cv=' ';
					}
				}
				if(fn>0){
					for(j=0;j<cc;j+=3){
						if(co[j]==f[fn-1]){
							cv=co[j+1];
							cf=co[j+2];
							break;
						}
					}
                    lastOpp=0;
					for(j=0;j<oc;j+=2){
						if(opp[j]==f[fn-1]){
							o[on++]=opp[j+1];
							lastOpp=1;
							break;
                        }
					}
				}
			}
		/*	printf("cv =%c\n",cv);
			printf("o =");
            for(j=0;j<on;j++)
                             printf("o[%d]=%c ",j,o[j]);*/
		//	}
		/*	else{
                  cv=' ';cf=' ';
				for(j=0;j<cc;j+=3){
					if(co[j]==f[0]){
						cv=co[j+1];
						cf=co[j+2];
					}
				}
				for(j=0;j<oc;j+=2){
					if(opp[j]==f[0])
						o[on++]=opp[j+1];
				}
			}*/
			                   
		}
		printf("Case #%d: [",k+1);
		for(i=0;i<fn-1;i++){
			printf("%c, ",f[i]);
		}
		if(fn>0)
			printf("%c",f[fn-1]);
		printf("]\n");
	}
	return 0;
}
