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
    
    freopen("B12.in","r",stdin);
    freopen("output1.txt","w",stdout);
    int t ;
    scanf("%d",&t);
    for(int i = 0; i < t; i++){
        
        int n;
        scanf("%d",&n);
        map<string,char> m;
        for(int j = 0; j < n ;j++){
            string s,s1;
            cin>>s;
            s1 = s.substr(0,s.size()-1);
            sort(s1.begin(),s1.end());
            m[s1] = s[s.size()-1];
        }
        map<string,int> m1;
        int d;
        scanf("%d",&d);
        
        for(int j = 1; j <= d;j++){
            string s;
            cin>>s;
            sort(s.begin(),s.end());
            m1[s] = j;
        }
        
        int c;
        string ss;
        //scanf("%d%s",&c,&ss);
        cin>>c;
        cin>>ss;
        string ans;
        string temp,temp1,temp2;
       
        for(int j =1; j< ss.size();j++ ){
            temp.clear();
             temp.push_back(ss[j-1]);
             
        
            temp.push_back(ss[j]);
          
        //    cout<<"  "<<temp1<<endl;
  /*          if(temp1.size() == 0){
                temp1.push_back(ss[j-1]);
                temp1.push_back(ss[j]);
            }
            else{
               // temp1.erase(1,1); 
               // temp1.push_back(ss[j]);
               temp2[1] = ss[j];
               temp1 = temp2;
            }*/
            //string ss2;
           // ss2.push_back(m[temp]);
           // cout<<ss2<<" "<<ss2.size()<<endl;
         //  cout<<ss <<" "<<j<<endl;
           temp2 = temp1;
           sort(temp.begin(),temp.end());
           sort(temp1.begin(),temp1.end());
            char ch = m[temp];
            if((int)ch>64 && (int)ch<98){
                ss[j-1] = m[temp];
               // cout<<j<<endl;
                ss.erase(j,1);
                j=1;
              //  temp1[0] = m[temp];
            }
            
            for(int k = 0 ; k < j;k++){
             string t1;
             t1.push_back(ss[k]);
             t1.push_back(ss[j]);
             sort(t1.begin(),t1.end());               
             if(m1[t1] != 0){
                ss = ss.substr(j+1,ss.size()-j+1);
             //   cout<<ss<<endl;
            //    temp1.clear();
                j=0;
                break;
            }
            }
            
            
       // cout<<ss<<endl;
        }
        if(ss.size() > 0){
            cout<<"Case #"<<i+1<<": [";
            for(int j = 0; j <ss.size()-1;j++){
                cout<<ss[j]<<", ";
            }
            cout<<ss[ss.size()-1]<<"]"<<endl;
        }
        else
           cout<<"Case #"<<i+1<<": []"<<endl;
    }
   return 0;
  //  system("pause");
}
