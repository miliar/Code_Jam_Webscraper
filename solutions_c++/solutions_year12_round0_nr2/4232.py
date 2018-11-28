#include<iostream>
#define ch(x) x?1:0
using namespace std;
int elem_max[3], elem_min[3], inp[3];

int validity(int j, int p){
    int diff = elem_max[j] -(inp[j] - (elem_min[j]+elem_max[j]));
    //cout<<diff<<endl;
    if (!diff && elem_max[j] && (elem_max[j]+1 >= p))
             return 1;
    return 0;
}
             
int main()
    {
          int i, j, t, n, s, p, count;
          int ans;
          freopen("B-large.in","rt",stdin);
          freopen("B-large.out","wt",stdout);
          cin>>t;
          for(i=0; i<t; i++){
                   ans = 0;
                   cin>>n>>s>>p;
                   for(j=0; j<n; j++){
                            cin>>inp[j];
                            elem_min[j] = inp[j]/3;
                            elem_max[j] = ch((inp[j] - 3*elem_min[j])); 
                            elem_max[j] += elem_min[j];
                            //cout<<elem_min[j]<<elem_max[j]<<endl;
                            if(elem_max[j] >= p)      ans++;
                            else if(s){
                                 count = validity(j,p);
                                 ans += count;
                                 if (count) s--;
                                 }
                            }
                   cout<<"Case #"<<i+1<<": "<<ans<<endl;
                   }
          return 0;
    }
          
                   
                   
                           
