#include <iostream>
using namespace std;
#define fo(i,n) for(i=0; i<n; i++)
#define fi(i,n) for(i=1; i<=n; i++)
char s[70][70];
int i,j,n,m,t,k,l,tt,p;
bool bo1,bo2;

main()
{
      freopen("input.txt","r",stdin);
      freopen("output.txt","w",stdout);
      scanf("%d",&t);
      fo(tt,t){
        scanf("%d%d\n",&n,&m);
        fo(i,n) gets(s[i]);
        
        fo(i,n){
            p=0;
            for(j=n-1; j>=0; j--){
                s[i][j+p]=s[i][j];
                if (s[i][j]=='.') p++;
            }
            fo(j,p) s[i][j]='.';
        }
        bo1=bo2=0;
        
        fo(i,n){
           fo(j,n){
              if (s[i][j]=='R'){
                  p=1; k=j+1;
                  while (k<n && s[i][k]=='R') k++,p++;
                  k=j-1;
                  while (k>=0 && s[i][k]=='R') k--,p++;
                  if (p>=m){ bo1=1; continue; }
                  
                  k=i-1; p=1;
                  while (k>=0 && s[k][j]=='R') k--, p++;
                  k=i+1;
                  while (k<n && s[k][j]=='R') k++, p++;
                  if (p>=m){ bo1=1; continue; }
                  
                  k=i-1; l=j-1; p=1;
                  while (k>=0 && l>=0 && s[k][l]=='R') k--,l--,p++;
                  k=i+1; l=j+1;
                  while (k<n && l<n && s[k][l]=='R') k++,l++,p++;
                  if (p>=m){ bo1=1; continue; }
                  
                  k=i-1; l=j+1; p=1;
                  while (k>=0 && l<n && s[k][l]=='R') k--,l++,p++;
                  k=i+1; l=j-1;
                  while (k<n && l>=0 && s[k][l]=='R') k++,l--,p++;
                  if (p>=m){ bo1=1; continue; }
                  
              } else
              if (s[i][j]=='B'){
                  p=1; k=j+1;
                  while (k<n && s[i][k]=='B') k++,p++;
                  k=j-1;
                  while (k>=0 && s[i][k]=='B') k--,p++;
                  if (p>=m){ bo2=1; continue; }
                  
                  k=i-1; p=1;
                  while (k>=0 && s[k][j]=='B') k--, p++;
                  k=i+1;
                  while (k<n && s[k][j]=='B') k++, p++;
                  if (p>=m){ bo2=1; continue; }
                  
                  k=i-1; l=j-1; p=1;
                  while (k>=0 && l>=0 && s[k][l]=='B') k--,l--,p++;
                  k=i+1; l=j+1;
                  while (k<n && l<n && s[k][l]=='B') k++,l++,p++;
                  if (p>=m){ bo2=1; continue; }
                  
                  k=i-1; l=j+1; p=1;
                  while (k>=0 && l<n && s[k][l]=='B') k--,l++,p++;
                  k=i+1; l=j-1;
                  while (k<n && l>=0 && s[k][l]=='B') k++,l--,p++;
                  if (p>=m){ bo2=1; continue; }
              }
           }
        }
        printf("Case #%d: ",tt+1);
        if (bo1 && !bo2) cout<<"Red"<<endl;
        else if (bo1 && bo2) cout<<"Both"<<endl; else
        if (!bo1 && bo2) cout<<"Blue"<<endl; else
        cout<<"Neither"<<endl;
        fo(i,n) fo(j,n) s[i][j]='.';
      }
}
