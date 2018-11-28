#include <stdio.h>
#define MAX 205
typedef struct{
   bool *arc[MAX];
   int m;
   int n;
   int vexnum;
   int arcnum;
}BiGraph;

void Init(BiGraph &G){
  
	int i,j;
	for(i=0;i<MAX;i++)
	{
         G.arc[i]=new bool[MAX];
         for(j=0;j<MAX;j++)
          G.arc[i][j]=false;
	}

}

void Renew(BiGraph &G)
{
	int i,j;
   

    for(i=0;i<G.vexnum;i++)
		for(j=0;j<G.vexnum;j++)
			G.arc[i][j]=false;
}

void pr(BiGraph &G)
{
   int i,j;
   for(i=0;i<G.m;i++)
   {
	   printf("\n");
	   for(j=0;j<G.n;j++)
		 {
			 if(G.arc[i][j]==true)
				 printf("1 ");
			 else
				 printf("0 ");
		 }


   }

   
}


typedef struct{
   int vex;
   int tag;
 }SignType ;
void ChangeM(int m,int match[],int& ednum,SignType last,SignType sign[]);
void  Matching(BiGraph G,int match[],int& ednum);//匈牙利算法
void Build(BiGraph &G,bool *road[]);

     
bool OK(int temp[][50],int from,int to,int k)
{
	int i;
     for(i=0;i<k;i++)
		 if(temp[from][i]>=temp[to][i])
			 break;
     if(i==k)
		 return true;
	 return false;
}

int main()
{
    freopen("C-large.in.txt","r",stdin);
    freopen("C-large.out.txt","w",stdout);

	int i,j,k,ednum,rnum,pnum,from,to,casenum,p;
	int match[1100];
    bool* road[MAX];
    BiGraph G;
	Init(G);
	int temp[205][50];

    for(i=0;i<MAX;i++)
        road[i]=new bool[MAX];
		
    
   scanf("%d",&casenum);
    
    for(p=0;p<casenum;p++)
	{
		scanf("%d%d",&pnum,&k);
        G.vexnum=pnum;
    	G.m=pnum;
    	G.n=pnum;
 
		Renew(G);
		for(i=0;i<pnum;i++)
		   for(j=0;j<pnum;j++)
		    	road[i][j]=false;

        for(i=0;i<pnum;i++)
			for(j=0;j<k;j++)
                scanf("%d",&temp[i][j]);

        for(i=0;i<pnum;i++)
		   for(j=0;j<pnum;j++)
			   if(i!=j)
			   {
                    if(OK(temp,i,j,k))
						road[i][j]=true;
			   }



		Build(G,road);
		ednum=0;
//		for(i=0;i<G.m;i++)
//			for(j=0;j<G.n;j++)
//				if(G.arc[i][j]==true)
//					printf("(%d,%d)\n",i+1,j+1);
        Matching(G,match,ednum);
        printf("Case #%d: %d\n",p+1,pnum-ednum);
        
    }

   /*
    for(p=0;p<casenum;p++)
	{
		scanf("%d%d",&pnum,&rnum);
        G.vexnum=pnum;
    	G.m=pnum;
    	G.n=pnum;
 
		Renew(G);
		for(i=0;i<pnum;i++)
		   for(j=0;j<pnum;j++)
		    	road[i][j]=false;


        for(i=0;i<rnum;i++)
		{
               scanf("%d%d",&from,&to);
			   road[from-1][to-1]=true;
		}



		Build(G,road);
		ednum=0;
//		for(i=0;i<G.m;i++)
//			for(j=0;j<G.n;j++)
//				if(G.arc[i][j]==true)
//					printf("(%d,%d)\n",i+1,j+1);
        Matching(G,match,ednum);
        printf("%d\n",pnum-ednum);
        
    }
*/

	return 0;

}


void Build(BiGraph &G,bool *road[])
{
	int i,j;
	


    for(i=0;i<G.vexnum;i++)
	   for(j=0;j<G.vexnum;j++)
		    G.arc[i][j]=road[i][j];
		

    return;
}


void  Matching(BiGraph G,int match[],int& ednum)//匈牙利算法match的长度不小于图的总顶点数
{
      
       bool istaged[MAX*2];
	 SignType sign[MAX*2];
	SignType temp;
	int signnum;
	int outnum;
	int i;
	bool tag;
	
	ednum=0;
	for(i=0;i<MAX*2;i++)
	 	match[i]=-1;
           
		


	do{
		tag=false;
    signnum=0;
    outnum=0;

    for(i=0;i<MAX*2;i++)
         istaged[i]=false;

	for(i=0;i<G.m;i++)
	{
         
		if(match[i]==-1)
		{
			sign[signnum].vex=i;
            sign[signnum].tag=-1;
		    istaged[i]=true;
			signnum++;
		}

	}
   
	while(outnum<signnum)//还有未标号的点
	{
         temp=sign[outnum++];
        // printf("now scan %d(tag %d)\n",temp.vex,temp.tag);
        // getchar();
         if(temp.vex-G.m<0)
         {
                for(i=0;i<G.n;i++)
				{
				       if(G.arc[temp.vex][i]==true&&istaged[G.m+i]==false)
					   {
                             sign[signnum].vex=G.m+i;
                             sign[signnum].tag=outnum-1;
		                   	 istaged[sign[signnum].vex]=true;
							 signnum++;
                             
					   }
				
				}
		 }
		 else 
		 {
              
                 if(match[temp.vex]!=-1&&istaged[match[temp.vex]]==false)
				 {
                         sign[signnum].vex=match[temp.vex];
                         sign[signnum].tag=outnum-1;
		               	 istaged[sign[signnum].vex]=true;
                         signnum++;
				 }
				 else//找到增长路径
                 {
                      ChangeM(G.m,match,ednum,temp,sign);  
                      tag=true;
					  break;
				 }


         }


    }
/*	printf("now the match is \n");
    int p,n;
	for(p=0;p<G.m;p++)
    {		
		 if(match[p]!=-1)
              printf("(%d,%d) (%d,%d)\n",p,match[p],match[p],match[match[p]]);
	
       printf("\n");
	}*/

	}while(tag==true);

   //如果未找到增长路径，该匹配即为最大匹配
    return;
}

void ChangeM(int m,int match[],int& ednum,SignType last,SignType sign[])
{
   
	SignType temp=last;
  
     while(temp.tag!=-1)
	 {
        
		 if(temp.vex-m>=0)
		 {
			 match[temp.vex]=sign[temp.tag].vex;
			 match[sign[temp.tag].vex]=temp.vex;
		 }
		 
		 temp=sign[temp.tag];
	 }
     ednum++;
	 return;
}

