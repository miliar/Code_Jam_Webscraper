#include<iostream>
#include<vector>
using namespace std;
main(){
       int l,d,n,i,j,k,ii,jj;
       vector<string> v;
       scanf("%d %d %d",&l,&d,&n);
       string str;
       while(d--){
                  cin>>str;
                  v.push_back(str);
       }
       for(i=1;i<=n;i++){
                         cin>>str;
                         vector<string> vf;
                         int flag=0;k=-1;
                         for(j=0;j<str.size();j++){
                                                   string ss;
                                                   if(str[j]=='('){
                                                                   j++;k++;
                                                                   while(str[j]!=')'){
                                                                                      ss+=str[j]; j++;                
                                                                   }
                             //                                      cout<<ss<<endl;
                                                                   vf.push_back(ss);
                                                                   /*bool pre=false;
                                                                   for(ii=0;ii<ss.size();ii++){
                                                                                               for(jj=0;jj<v.size();jj++){
                                                                                               if(ss[i]==v[jj][k]){
                                                                                                                   pre=true;
                                                                                                                   break;
                                                                                               }
                                                                                               }
                                                                   }
                                                                   cout<<pre<<endl;
                                                                   */             
                                                   }else{
                                                         ss+=str[j];
                                                         vf.push_back(ss);
                                                   }
                                                   
                         }        
                         /*for(k=0;k<vf.size();k++){
                                                   cout<<vf[k]<<" ";
                         } */       
                          int cnt=0;bool pre;
                          for(k=0;k<v.size();k++){
                                                  for(ii=0;ii<v[i].size();ii++){
                                                                                pre=false;
                                                                                for(j=0;j<vf[ii].size();j++){
                                                                                if(vf[ii][j]==v[k][ii]){pre=true;break;}
                                                                                
                                                                                }
                                                                                if(pre!=true){
                                                                                              break;
                                                                                }
                                                  }
                                                  if(pre==true)cnt++;
                          }              
                                     cout<<"Case #"<<i<<":"<<" "<<cnt<<endl;
                         //j=str.find_first_of('(');
                         //cout<<j<<endl;
       }
                  
       //system("pause");
}
