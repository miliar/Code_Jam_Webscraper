#include<iostream>
using namespace std;

 using   namespace  std;

 const   int  MAXN  =   508 ;
 int  uN, vN;   // u,ｖ数目  
 bool  g[MAXN][MAXN]; // g[i][j] 表示 xi与yj相连  
 int  xM[MAXN], yM[MAXN];  //  输出量  
 bool  chk[MAXN];  // 辅助量 检查某轮 y[v]是否被check  
 
 
 bool  SearchPath( int  u)
{
    int  v;
     for  (v = 0 ; v < vN; v ++ )
     {
        if  (g[u][v]  &&   ! chk[v])
        {
           chk[v]  =   true ;
           if  (yM[v]  ==   - 1   ||  SearchPath(yM[v])) 
           {
              yM[v]  =  u;
              xM[u]  =  v;
              return   true ;
           } 
       } 
    } 
    return   false ;
} 
 
int  MaxMatch()
{
   int  u;
   int  ret  =   0 ;
   memset(xM,  - 1 ,  sizeof (xM));
   memset(yM,  - 1 ,  sizeof (yM));
   for  (u = 0 ; u < uN; u ++ )
   {
      if  (xM[u]  ==   - 1 )
      {
         memset(chk,  false ,  sizeof (chk));
         if  (SearchPath(u)) ret ++ ;
      } 
   } 
   return  ret;
} 
 
 int  main()
  {
    freopen("C:\\Documents and Settings\\v-guozh\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Documents and Settings\\v-guozh\\Desktop\\out.txt","w",stdout);
  
     int n;
     scanf("%d",&n);
     int  i, j, k;
     char c[12][12]; 
     for(i=1; i<=n; i++){
        int  tU, tV, num=0;
        scanf("%d%d%d",&uN,&vN);
        memset(g,  false ,  sizeof (g));
        for(j=0; j<uN; j++){
            scanf("%s",c[j]);
            for(k=0; k<vN; k++) if(c[j][k]=='.') num++;
        }
        for(j=uN-1; j>=0; j--){
            for(k=0; k<=vN-1; k++){
                if(c[j][k]=='.'){
                    if(k-1>=0 && c[j][k-1]=='.'){
                        g[vN*j+k][vN*j+k-1] = true;
                    }
                    if(k+1<vN && c[j][k+1]=='.'){
                        g[vN*j+k][vN*j+k+1] = true;
                    }
                    if(j-1>=0 && k-1>=0 && c[j-1][k-1]=='.'){
                        g[vN*(j-1)+k-1][vN*j+k] = true;
                        g[vN*j+k][vN*(j-1)+k-1] = true;
                    }
                    if(j-1>=0 && k+1<vN && c[j-1][k+1]=='.'){
                        g[vN*(j-1)+k+1][vN*j+k] = true;
                        g[vN*j+k][vN*(j-1)+k+1] = true;
                    }
                }
            }
        }
        k = uN*vN;
        uN = vN = k;
        k = MaxMatch();
        printf("Case #%d: %d\n",i,num-k+k/2);
    }
     return   0 ; 
}  
