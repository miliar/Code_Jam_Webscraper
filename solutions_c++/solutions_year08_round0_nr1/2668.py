#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<fstream>
#include<stdlib.h>
using namespace std;
int main(){


        ifstream fin("input");
        int ans[100];
        string inp;
        getline(fin,inp);
        int tot=atoi(inp.c_str());

        for(int r=0;r<tot;r++){
                map<string,int> a;
                int n;
                string tn;
                getline(fin,tn);
                n=atoi(tn.c_str());
                string temp;
                for(int i=0;i<n;i++){
                        getline(fin,temp);
                        a[temp]=i;
                }
                int nt;
                getline(fin,temp);
                nt=atoi(temp.c_str());
                int x[100];
                for(int i=0;i<n;i++)
                        x[i]=0;
                int tc=0;
                int count=0;
                for(int i=0;i<nt;i++){
                        getline(fin,temp);
                        int l=a[temp];
                        if(x[l]==0){
                                x[l]=1;
                                tc++;
                        }

                        if(tc==n){
                                tc=1;
                                for(int j=0;j<n;j++)
                                        x[j]=0;
                                x[l]=1;
                                count++;
                        }
                }

                ans[r]=count;
        }
        for(int r=0;r<tot;r++){
                cout<<"Case #"<<r+1<<": "<<ans[r]<<endl;
        }

}
