#include<cstdio>
#include<cstring>

using namespace std;


int main(){
    
	char filename[32];
	int ind=0;
	const int N=50, T=100;
	int K;
	char infile[32], outfile[32],line[N+1];
	int i, j, k, l, ncases, m, t;
	int no[2]={1};
	int curr;
	int R=1, B=-1, G=0;
	int a[N][N]={0};
	int level[N]={0};
   	int n,s,e,w,ne,nw,se,sw;
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	printf("%s", infile);
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
    fscanf(fp,"%d",&ncases);
    for (i = 0; i < ncases; i += 1)
    {
        fscanf(fp,"%d %d",&m, &K);
        for (j = 0; j < m; j++)
        {
	        fscanf(fp,"%s",line);
	        for(l=0;l<m;l++){
		    	if(line[l]=='R') a[l][m-1-j]=1;
	        	else {
	        		if(line[l]=='B') 			a[l][m-1-j]=-1;
					else a[l][m-1-j]=0;
				}
	        }
	  	}
	  	int ss=0;
        for(l=0;l<m;l++)
        {
        	ss=0;
        	for (j=m-1;j>=0;j--){
        		if(a[j][l]!=0){
        			level[m-1-ss]=a[j][l];
        			ss++;
 				}
 			}
        	for (j=0;j<m;j++){
        		a[j][l]=level[j]; 
        		level[j]=0;
 			}
	  	}/*
        for(l=0;l<m;l++)
        {
        	for (j=0;j<m;j++){
		        printf("%d",a[j][l]);
	        }printf("\n");
	  	}*/
	  	int counter=0;
 	    no[0]=no[1]=1;
        for (j = 0; j < m; j++)
        {
	        for(l=0;l<m;l++)
	        {
	        	curr=a[j][l];
	        	if(curr==-1)	ind=1;
	        	else	ind=0;
	        	if(curr!=0 && no[ind])
	        	{
			    	n=s=e=w=ne=nw=se=sw=1;
			    	for(k=1;k<K;k++){
			    		if(k+l<m && a[j][k+l]==curr)
			    			e++;
			    		else break;
			    	}
			    	for(k=1;k<K;k++){
			    		if(l-k>=0 && a[j][l-k]==curr)
			    			w++;
			    		else break;
			    	}
			    	for(k=1;k<K;k++){
			    		if(j+k<m && a[j+k][l]==curr)
			    			n++;
			    		else break;
			    	}
			    	for(k=1;k<K;k++){
			    		if(j-k>=0 && a[j-k][l]==curr)
			    			s++;
			    		else break;
			    	}
			    	for(k=1;k<K;k++){
			    		if(k+l<m && k+j<m && a[j+k][k+l]==curr)
			    			ne++;
			    		else break;
			    	}
			    	for(k=1;k<K;k++){
			    		if(l-k>=0 && k+j<m && a[j+k][l-k]==curr)
			    			nw++;
			    		else break;
			    	}
			    	for(k=1;k<K;k++){
			    		if(l-k>=0 && j-k>=0 && a[j-k][l-k]==curr)
			    			sw++;
			    		else break;
			    	}
			    	for(k=1;k<K;k++){
			    		if(l+k<m && j-k>=0 && a[j-k][k+l]==curr)
			    			se++;
			    		else break;
			    	}
			    	if(n>=K || e>=K || s>=K || w>=K || ne>=K || nw>=K || se>=K || sw>=K){
			    		no[ind]=0;
			    		//printf("%d%d%d%d%d%d%d%d\n",n, e, s, w, ne, nw, se, sw);
			    	}
			    }
	        }
	  	}
        fprintf(ofp,"Case #%d: ",i+1);
	  	if(no[0] && no[1]) 		fprintf(ofp,"Neither\n");
	  	if(no[0] && !no[1]) 	fprintf(ofp,"Blue\n");
	  	if(!no[0] && !no[1]) 	fprintf(ofp,"Both\n");
	  	if(!no[0] && no[1]) 	fprintf(ofp,"Red\n");
    }

    fclose(fp);
    fclose(ofp);
    
    return 0;
}

