#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
typedef pair<int,int> PII;
int tc,p,m[100],price[12][1500],isi[12][1500];

void process (int depth, int ke, int sisa, int num,int left, int right){
     if ((num < left) || (num > right))return;
     if (sisa == 0) return;
     isi[depth][ke] = 1;
     int mid = (left+right)/2;
     process(depth+1,ke*2,sisa-1,num,left,mid);
     process(depth+1,ke*2+1,sisa-1,num,mid+1,right);
}

int main(){
 scanf("%d",&tc);
 for (int ti = 1; ti <= tc; ti++){
     vector<PII> v;
     scanf("%d",&p);
     for (int i = 0; i < (1<<p); i++){
         scanf("%d",&m[i]);    
         v.push_back(make_pair(m[i],i));
     }    
     memset(isi,0,sizeof(isi));
     for (int i = p-1; i >= 0; i--){
         for (int j = 0; j < (1<<i); j++){
             scanf("%d",&price[i][j]);    
         }
     }
     sort(v.begin(),v.end());
     for (int i = 0; i < v.size(); i++){
         process(0,0, p-v[i].first,v[i].second,0,(1<<p)-1);
     }
     int res = 0;
     for (int i = p-1; i >= 0; i--){
         for (int j = 0; j < (1<<i); j++){

             if (isi[i][j]) res++;
         }

     }
     printf("Case #%d: %d\n",ti,res);
 }   
}
