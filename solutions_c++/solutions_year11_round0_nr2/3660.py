#include<stdio.h>
#include<iostream>
#include<vector>
using namespace std;

int main(){
        int m,caseno=1;
        cin>>m;
        while(m--){
                int combn,oppn,i,j,len,k,flag;
                char combns[100][100],oppns[100][100];
                cin>>combn;
                char a,b,c;
                string input,output="";
				for(i=0;i<100;i++)
					for(j=0;j<100;j++){
						combns[i][j]=-1;
						oppns[i][j]=-1;
					}
                for(i=0;i<combn;i++){
                        cin>>a>>b>>c;
                        combns[(int)a-'A'][(int)b-'A']=c;
			combns[(int)b-'A'][(int)a-'A']=c;
                }
                cin>>oppn;
                for(i=0;i<oppn;i++){
                        cin>>a>>b;
                        oppns[(int)a-'A'][(int)b-'A']=1;
			oppns[(int)b-'A'][(int)a-'A']=1;
                }
                cin>>len;
                cin>>input;
		//cout<<len;
		//cout<<input;
		i=0;k=1;
		int t1,t2,start=0;
		output+=input[0];
		for(i=1;i<len;i++){
		//	cout<<" i is "<<i<<" output "<<output<<" \n";
			j=i-1;
			if(k==0){
                                        output+=input[i];
                                        k++;
                                        continue;
                         }
			 if(combns[(int)input[j]-'A'][(int)input[i]-'A']!=-1){
                                        output[k-1]=combns[(int)input[j]-'A'][(int)input[i]-'A'];
					input[i]=combns[(int)input[j]-'A'][(int)input[i]-'A'];
					input[j]=combns[(int)input[j]-'A'][(int)input[i]-'A'];
				//		 cout<<" i is "<<i<<" output "<<output<<" \n";
					continue;
                         }
			 output+=input[i];
			k++;
		//	cout<<" i is "<<i<<" output "<<output<<" \n";
			while(j>=start){
				if(oppns[(int)input[j]-'A'][(int)input[i]-'A']==1){
					output="";
					k=0;
		//			cout<<" i is "<<i<<" j is "<<j;
					start=i+1;
					break;
				}
				j--;
			}
		}
		cout<<"Case #"<<caseno++<<":"<<" [";
		for(i=0;i<output.size();i++){
			cout<<output[i];
			if(i<output.size()-1){
				cout<<", ";
			}
		}
		cout<<"]\n";

    }
 return 0;
 }
