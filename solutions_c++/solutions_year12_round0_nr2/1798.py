#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<cstdio>
using namespace std;


   
int main()
{
 	freopen("2.in","r",stdin);
 	freopen("o.out","w",stdout);
 	int n,i,j,num,count;
 	cin>>n;
 	vector< vector<int>  > lists(n);
    for(i=0;i<n;i++){
	   cin>>num;
	   lists[i].push_back(num);
      for(j=0;j<lists[i][0]+2;j++){
			   cin>>num;
        lists[i].push_back(num);
		}
		}
    for(i=0;i<n;i++){
		for(j=3,count=0;j<lists[i][0]+3;j++)
		if(lists[i][2]>1){
		  if(lists[i][j]>=3*lists[i][2]-2)
		    count++;
          else 
		       if(lists[i][j]<3*lists[i][2]-4);
               else 
			     if(lists[i][1]>0){
			   		count++;
			   		lists[i][1]--;
					}
					}
		 else if(lists[i][2]==0)  count++;
		      else 
			    if(lists[i][j]==0);
				else count++;  
		cout<<"Case #"<<i+1<<": "<<count<<endl;
		}
             
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 //	system("pause");
 	return 0;
}
