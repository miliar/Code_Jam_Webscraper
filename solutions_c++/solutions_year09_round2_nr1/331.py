/*
TASK: decision_tree Code Jam '09 1B
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char str[110][1000]; //for animals

char tree[11000][1000]; //the tree
int isleaf[11000];
double weight[11000];
int child[11000][2];
int ccount[11000];

int stack[11000],top=0; //tree creation process
int indexcount=0;

int main()
{
    int cases,i,j,n,cc,k,a,cur,x,parent;
    int l;
    double ans;
    int state; //0 = waiting for (, 1 = waiting for num, 2 = waiting for string/)
    
    char buffer[1000];
    char temp[1000];
    
    scanf("%d", &cases);
    
    for(cc=0;cc<cases;cc++)
    {
        scanf("%d\n", &l);
        
        state=0;
        indexcount=0;
        top=0;
        
        for(i=0;i<11000;i++)
        {
            isleaf[i]=0;
            ccount[i]=0;
        }
        
        for(i=0;i<l;i++)
        {
            gets(buffer);
            k=strlen(buffer);
            
            j=0; 
            
            while(1)
            {
//                printf("j = %d\n", j);
                
//                printf("state = %d  | stack[top] = %d\n", state, stack[top-1]);
                
                while(buffer[j]==' ' && j<k)
                    j++;
            
                if(j==k) break;
            
                if(state==0)
                {
                    if(buffer[j]==')')
                    {
                        top--;
                        j++;
                        continue;
                    }

                    j++;
                    state=1;
                }
                else if(state==1)
                {
                    if(buffer[j]==')')
                    {
                        top--;
                        j++;
                        continue;
                    }
                    
                    if(top>0)
                    {
                        parent = stack[top-1];
                        child[parent][ ccount[parent]++] = indexcount;
                    }
                    stack[top++]=indexcount;
                    
                    for(x=0;x<k-j;x++)
                    {
                        if(! (buffer[x+j]=='.' || (buffer[x+j]>='0' && buffer[x+j]<='9') ) ) //not a number
                        {
                            temp[x]=0;
                            break;
                        }
                        temp[x]=buffer[x+j];
                    }
                    sscanf(temp, "%lf", &weight[indexcount]);
                    j=x+j;
                    
                    state = 2;
                }
                else if(state==2)
                {
                    if(buffer[j]==')')
                    {
                        j++;
                        isleaf[indexcount]=1;
                        state=0;
                        indexcount++;
                        top--;
                    }
                    else
                    {
                        for(x=0;x<k-j;x++)
                        {
                            if(! (buffer[x+j]>='a' && buffer[x+j]<='z') ) //not a character
                            {
                                temp[x]=0;
                                break;
                            }
                            temp[x]=buffer[x+j];
                        }
                        temp[x]=0;
//                        printf("temp %s\n", temp);
                        sscanf(temp, "%s", &tree[indexcount]);
                        j=x+j;
                        
                        indexcount++;
                        state = 0;
                    }
                }
            
            }
            
        } //done input reading (finally)
        
/*        for(i=0;i<indexcount;i++)
        {
            if(isleaf[i]==0)
                printf("Node %d<%lf>: [%d,%d] / %s\n", i,weight[i],child[i][0],child[i][1],tree[i]);
            else
                printf("Node %d<%lf>\n",i,weight[i]);
        }*/
            
        
        scanf("%d", &a);

        printf("Case #%d:\n", cc+1);

        for(i=0;i<a;i++)
        {
            scanf("%s", buffer);
            scanf("%d", &n);
            
            ans=1;
            
            for(j=0;j<n;j++)
                scanf("%s", str[j]);
            
            cur = 0;
            while(1)
            {
                ans*=weight[cur];

//                printf("traverse %d ans %lf\n", cur, ans);

                if(isleaf[cur])
                    break;

                for(j=0;j<n;j++)
                {
                    if(strcmp(tree[cur],str[j])==0) //same
                    {
                        cur=child[cur][0];
//                        printf("moved to %d\n", cur);
                        break;
                    }
                }
                if(j==n) //doesn't have this
                {
                    cur=child[cur][1];
//                    printf("moved to %d\n", cur);
                }
            }
            
            printf("%.10lf\n", ans);
        }
    }
    
    
    return 0;
}
