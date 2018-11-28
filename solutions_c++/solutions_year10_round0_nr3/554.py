#include<vector>
#include <cstdio>
#include <cstdlib>
#include<cstring>
using namespace std;

int main() {
    char finname[] = "C-large.in";
    //char finname[] = "C-small.in";
    //char finname[] = "C_rand.in";
    //char finname[] = "../B_test.in";
    FILE *fp;    
    if((fp=fopen(finname,"r")) == NULL) {
        printf("File not found\n");
        exit(0);
    }
    fclose(fp);
    freopen(finname,"r",stdin);
    freopen(strcat(finname,".outFile"),"w",stdout);
    int tc,rcycle,r,n,k,curi,nextIndex[1000];
    int stat[1000];
    unsigned long long int profit,cycleProfit;
    vector<vector<unsigned long long int> >gvalue(1000,vector<unsigned long long int>(1000));
    scanf("%d",&tc);   
    for(int tci=0;tci<tc;tci++) {
        scanf("%d%d%d",&r,&k,&n);        
        for(int j=0;j<n;j++)
            scanf("%llu",&gvalue[0][j]);
        
		for(int j=1;j<n;j++)
			gvalue[0][j]=gvalue[0][j]+gvalue[0][j-1];
        
		for(int i=1;i<n;i++) 
            for(int j=i;j<n;j++)
                gvalue[i][j] = gvalue[0][j]-gvalue[0][i-1];
		
		for(int i=1;i<n;i++) 
            for(int j=0;j<i;j++)
				gvalue[i][j] = gvalue[0][n-1]-(gvalue[0][i-1]-gvalue[0][j]);

        for(int i=0;i<n;i++) {            
            for(int j=i;;) {
                if(gvalue[i][j] == k) {
                    nextIndex[i]=j;
                    break;
                }
                else if(gvalue[i][j] > k) {
                    if(j==0)
                        nextIndex[i]=n-1;
                    else
                        nextIndex[i]=j-1;
                    break;
                }
                j=(j+1)%n;
                if(j==i) {
                    if(j==0)
                        nextIndex[i]=n-1;
                    else
                        nextIndex[i]=i-1;
                    break;
                }
            }
        }
        curi=0;profit=0;cycleProfit=0;
        int tCycle=0,aCycle=0,newcuri,tempi,i;
        memset(stat,-1,sizeof(int)*n);
        stat[curi]=1;
        while(1) {
            curi=(nextIndex[curi]+1)%n;
            tCycle++;
            if(stat[curi]<0)
                stat[curi]=1;
            else
                break;
        }
        newcuri=curi;
        while(1) {
            cycleProfit+=gvalue[newcuri][nextIndex[newcuri]];
            newcuri=(nextIndex[newcuri]+1)%n;
            aCycle++;
            if(newcuri==curi)
                break;
        }
        tempi=0;i=0;
        while(tempi!=curi && i<r){
            profit+=gvalue[tempi][nextIndex[tempi]];
            i++;
            tempi=(nextIndex[tempi]+1)%n;
        }
        profit += ((r-i)/aCycle)*cycleProfit;
        for(int k=0;k<(r-i)%aCycle;k++) {
            profit+=gvalue[curi][nextIndex[curi]];
            curi=(nextIndex[curi]+1)%n;
        }        
        printf("Case #%d: %llu\n",tci+1,profit);
    }
    return 0;
}

