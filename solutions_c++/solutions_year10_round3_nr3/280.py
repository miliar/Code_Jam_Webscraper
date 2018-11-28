#include<iostream>
#include<vector>

using namespace std;
int a[40][40];
char s[40];
int n,m;
int che(int ii,int jj,int si){  
    if( ii+si> n || jj+si > m ) return 0; 
   // if( si==2  ) cout<<ii<<" startt "<<jj<<endl;
    for(int i=ii;i<ii+si;i++)
      for(int j=jj;j<jj+si;j++){ // if( si==2  ) cout<<i<<" ' "<<j<<endl;
         if( a[i][j]==1 ){
            if( i-1>=ii && a[i-1][j]!=0 ) return 0;
            if( j-1>=jj && a[i][j-1]!=0 ) return 0;
         }
         else  if( a[i][j]==0 ){
            if( i-1>=ii && a[i-1][j]!=1 ) return 0;
            if( j-1>=jj && a[i][j-1]!=1 ) return 0;
         }
         else return 0;
      }
    //  if( si==2  ) cout<<ii<<" : "<<jj<<endl;
      return 1;
}
int find(int si){
    int r=0;
    for(int i=0;i<n;i++)
      for(int j=0;j<m;j++){
          if( a[i][j]<2 && che(i,j,si) ){ 
              r++; // if( si==4 ) cout<<i<<" "<<j<<endl;
              for(int ii=0;ii<si;ii++)
               for(int jj=0;jj<si;jj++) a[i+ii][j+jj]=9;
          }
      }
      return r;
}
int main(){    freopen("input.cpp","r",stdin);  freopen("output.cpp","w",stdout);
    int _=1; int t;scanf("%d",&t);
    while( t-- ){
      scanf("%d %d",&n,&m);
      memset(a,55,sizeof(a));
      for(int i=0;i<n;i++){
        scanf("%s",s); ///cout<<s<<endl;
        for(int j=0;j<m/4;j++){
          char ch=s[j];  
          if( ch<='9' && ch>='0' ) ch-='0';
          else ch-='A'-10; 
          for(int k=0;k<4;k++){
             if( ch & (1<<(4-k-1) ) ) a[i][j*4+k]=1;
             else a[i][j*4+k]=0;
          }
        }
      }
     /* for(int i=0;i<n;i++){
               for(int j=0;j<m;j++) cout<<a[i][j]<<" ";
               cout<<endl;
               }*/
      vector<int> a,b;
      for(int si=min(n,m);si>0;si--){
         int r=find(si);
         if( r) { a.push_back(r); b.push_back(si); }
      }
    
      printf("Case #%d: %d\n",_++,a.size());
      for(int i=0;i<a.size();i++)
        printf("%d %d\n",b[i],a[i]);
      
    
    }
    
    //cout<<"\nTime take :: "<<clock()<<" ::ms"<<endl;while(true);
    return 0;
}
