#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main()
{
    int nCases;
    cin>>nCases;
    int count = 1;
    
	while(count <= nCases)
    {
	 			vector<int> V1;
				vector<int> V2;
				V1.clear();
				V2.clear();
				
				int n;
				cin>>n;
				
				for(int i=0;i<n;i++)
				{		
						int temp;
						cin>>temp;
						V1.push_back(temp);
				}
				
				for(int i=0;i<n;i++)
				{		
						int temp;
						cin>>temp;
						V2.push_back(temp);
				}
				
				vector <int> V3, V4, V5;
				V3.clear();V4.clear();V5.clear();
				
				sort(V1.begin(),V1.end());
				sort(V2.begin(),V2.end());
				
				reverse(V2.begin(),V2.end());
				int sum = 0;
				for(int i=0;i<n;i++)
						sum += (V1[i]*V2[i]);
						
				cout<<"Case #"<<count<<": "<<sum<<endl;		
				count++;
    }           
    
    return(1);
} 
