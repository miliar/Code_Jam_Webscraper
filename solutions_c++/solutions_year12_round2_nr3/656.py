#include<iostream>
#include<stdio.h>
#include<map>
#include<vector>
#include<cmath>
using namespace std;


int main(){
    int cases;
    cin>>cases;
    for(int kases=1; kases<=cases; kases++){
            int N;
            int score[10000];
            cin>>N;
            for(int i=0;i<N;i++)
                    cin>>score[i];
            int found=0;
            
            map <int, vector<int> > M;
            for(int i=1;i< pow(2.0,N);i++){
                    int j=0;
                    int temp=i;
                    int subSum=0;
                    vector<int> mark(10000, 0);
                    
                    while(temp){
                                int rem = temp%2;
                                if(rem){
                                       subSum+=score[j];
                                       mark[j]=1;
                                }
                                j++;
                                temp/=2;
                    }
                    if( M.find(subSum)!=M.end() ){
                        cout<<"Case #"<<kases<<": "<<endl;
                        vector<int> firstVal = M[subSum];
                        for(int k=0;k<N;k++)
                                if(firstVal[k])
                                   cout<<score[k]<<" ";
                        cout<<endl;
                        for(int k=0;k<N;k++)
                                if(mark[k])
                                   cout<<score[k]<<" ";
                        cout<<endl;
                        found=1;
                        break;
                    }
                    else
                        M[subSum] = mark;
            }
            if(!found){
                      cout<<"Case #"<<kases<<": "<<endl;
                      cout<<"Impossible\n";
            }
    }
    return 0;   
}
