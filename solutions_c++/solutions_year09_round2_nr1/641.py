#include <iostream>
#include <algorithm>
using namespace std;
double ans,nile[10000];
char kriteria[1000][1000];
char d[100][100];
int x;

bool cek(int a,int b){
     int zz=min(strlen(kriteria[a]),strlen(d[b]));
     zz--;
     bool ok=1;
     for (int k=0;k<=zz;k++)
     if (kriteria[a][k]!=d[b][k]) return 0;
     
     return 1;
     
     }
void baca(int pos){
     char buff,b2;
     
      scanf("%c",&buff);
     while (buff!='(') scanf("%c",&buff);
      
      scanf("%lf",&nile[pos]);
      scanf("%c",&b2);
     while (b2==' ' || b2=='\n') scanf("%c",&b2);
      kriteria[pos][0]=b2;
      
      if (b2!=')')
      {int wew=1;
      
      scanf("%c",&b2);
     while (b2!=' ' && b2!='\n') {kriteria[pos][wew]=b2; scanf("%c",&b2);wew++;}
      
      baca(pos*2); baca(pos*2+1); 
      scanf("%c",&buff);
     while (buff!=')') scanf("%c",&buff);
                           
     }
    //cout<<pos<<" "<<kriteria[pos]<<endl;
      
      
      }

void itung(int pos){
     ans*=nile[pos];
     if (kriteria[pos][0]==')') printf("%.7lf\n",ans);
     else{
          bool yey=0;
               for (int j=1;j<=x;j++){
               //cout<<kriteria[pos]<<" "<<d[j]<<endl;
               if (cek(pos,j)) yey=1;
               }
          if (yey) itung(pos*2); else itung(pos*2+1);
          }
     }

int main(){
   freopen("A.txt","r",stdin);
freopen("A.out","w",stdout);
    
int T,aa;
scanf("%d",&T);
for (int ii=1;ii<=T;ii++)
{
    scanf("%d",&aa);    
    cout<<"Case #"<<ii<<":"<<endl;
    baca(1);
    char gp[100];
    int NN;
    //cout<<"udah vaca"<<endl;
    scanf("%d",&NN);
    for (int iii=1;iii<=NN;iii++){//cout<<NN<<endl;
    scanf("%s",gp);
    scanf("%d",&x);
    for (int i=1;i<=x;i++)
    scanf("%s",d[i]);
    ans=1.00;
    itung(1);
    }
    
    }
    //system("pause");
    }
