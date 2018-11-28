# include <iostream>
# include <cstdio>
# include <sstream>
# include <vector>
# include <algorithm>
# include <queue>
# include <map>
# include <cstring>
# include <fstream>

using namespace std;

ifstream in("C-small-attempt0.in");
ofstream out("out.txt");

int solve(int p,int q,int pris[])
{
        
        int arr[101]={0};
        int mini,ind,ret = 999999999;
                
       	do{
        //for each day
		
		for(int i = 1;i<=p;i++)	arr[i]=i;
		int c = 0;
            for(int i = 0;i<q;i++)
            {
                
                   arr[pris[i]]=-1;
                       
                   //count to the left
                    for(int j = pris[i]-1;j>=1;j--){
                            if(arr[j]==-1)  break;                
                            else c++;
                        }
                    for(int j = pris[i]+1;j<=p;j++)
                    {
                        if(arr[j]==-1)  break;
                        else c++;   
                    }
            }

		ret = min(ret,c);	
       	}while(next_permutation(pris,pris+q)); 
        return ret;
}


int main()
{
    int cas = 0;
    int T;
    in>>T;
    
    while(T--)
    {
        int   P,Q,pris[11];
        in>>P>>Q;
        
        for(int i = 0;i<Q;i++)
            in>>pris[i];
            
     out<<"Case #"<<++cas<<": "<<solve(P,Q,pris)<<endl;   
    }    
 
 return 0;   
}

