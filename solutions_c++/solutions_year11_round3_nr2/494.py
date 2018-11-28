#include<iostream>
#include<vector>
#include<fstream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<map>

using namespace std;

int main()
{
    
    freopen("B21.in","r",stdin);
    freopen("output1.txt","w",stdout);
    int t ;
    scanf("%d",&t);
    for(int i = 0; i < t; i++){
        
        int l,t1,n,c;
        scanf("%d%d%d%d",&l,&t1,&n,&c);
        vector<int> cs;
        for(int j = 0; j < c;j++){
          int num;
          scanf("%d",&num);
          cs.push_back(num);
        }
        
        vector<int> dis,dur;
        vector< vector<int> > sor;
        int sum = 0;
        int ttime = 0;
        for(int j = 0; j < n;j++){
            vector<int> v1;
            dis.push_back(cs[j%cs.size()]);
            ttime += 2*dis[j]; 
            dur.push_back(sum);
            v1.push_back(dis[j]);
            v1.push_back(2*sum);
            sor.push_back(v1);
            sum += dis[j];
        }
     //   cout<<ttime<<endl;
        //sort(sor.rbegin(),sor.rend());
        vector<int> save;
        for(int j = 0; j < n; j++){
            int ch  = 0;
            ch = sor[j][1] - t1;
            int s1 = 0;
            if(ch < 0){
                ch = abs(ch);
                s1 = sor[j][0] - ch*0.5;
                save.push_back(s1);
                
            }
            else
               save.push_back(sor[j][0]);
        }
        sort(save.rbegin(),save.rend());
        for(int j =0; j < l;j++){
            ttime -= save[j];
        }
        
        cout<<"Case #"<<i+1<<": "<<ttime<<endl;
        
    }
 //   system("pause");
    return 0;
}
