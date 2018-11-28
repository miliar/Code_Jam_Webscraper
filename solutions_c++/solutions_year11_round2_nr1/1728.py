#include<iostream>
#include<vector>
#include<fstream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<map>
#include<iomanip>

using namespace std;

int main()
{
    
     freopen("A12.in","r",stdin);
    freopen("output1.txt","w",stdout);
        int t;
        scanf("%d",&t);
    for(int i = 0; i < t; i++){
        int n;
        scanf("%d",&n);
        vector<string> v;
        for(int j = 0; j < n;j++){
            string s;
            cin>>s;
        //   scanf("%s",&s);
            v.push_back(s);
        }
        vector<double> WP;
       for(int j = 0; j < v.size();j++){
            string s ;
            s = v[j];
            double w = 0;
            int win = 0,play = 0;
            for(int k = 0; k < s.size();k++){
                if(s[k] != '.'){
                    if(s[k] == '1')
                       win++;
                     play++;  
                }
            }
            if(play != 0)
            w = (double)win/(double)play;
            else
            play = 0;
            WP.push_back(w);
        }
        
       
        
        
         vector<double> OWP;
        for(int j = 0; j < v.size();j++){
            string s ;
            s = v[j];
            double w = 0;
            int play1 = 0;
            for(int k = 0; k < s.size();k++){
                if((s[k] != '.') && (k != j)){
                    string s1 = v[k];
                    double newp = 0;
                    int win = 0,play = 0;
                    for(int l = 0; l < s1.size();l++){
                         if((s1[l] != '.') && (l != j)){
                            if(s1[l] == '1')
                              win++;
                              play++;
                        }    
                    }
                    if(play != 0)
                    newp = (double)win/(double)play;
                    else
                    newp = 0;
                    w += newp;
                    play1++;  
                }
            }
            if(play1 != 0)
            w = w/(double)play1;
            else
            w = 0;
            OWP.push_back(w);
        }
      
        vector<double> OOWP;
        
         for(int j = 0; j < v.size();j++){
            string s ;
            s = v[j];
            double w = 0;
            int play = 0;
            for(int k = 0; k < s.size();k++){
                if((s[k] != '.') && (k != j)){
                    w += OWP[k];
                    play++;  
                }
            }
            if(play != 0)
            w = w/(double)play;
            else 
            w = 0;
            OOWP.push_back(w);
        }
       
        
        vector<double> final;
         for(int j = 0; j < v.size();j++){
            double rank = 0;
            rank = 0.25*(WP[j]) + 0.5*(OWP[j]) + 0.25*(OOWP[j]);
            final.push_back(rank);
            
        }
        cout<<"Case #"<<i+1<<":"<<endl;
        for(int j = 0; j < v.size();j++){
            cout<<setprecision(12)<<final[j]<<endl;
            
        }
        
        
        
    }
       return 0;
  //  system("pause");
}
